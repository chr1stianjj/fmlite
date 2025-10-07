import os
import json
from pathlib import Path

# --- CONFIGURATION ---
ROOT = Path(__file__).resolve().parents[1]  # fmlite root
AI_SUMMARY_DIR = ROOT / "ai-summary"
AI_SUMMARY_FILE = AI_SUMMARY_DIR / "ai-summary.txt"
PURPOSE_FILE = AI_SUMMARY_DIR / "purpose.json"

SOURCE_FOLDERS = [
    ROOT / "backend",
    ROOT / "frontend" / "src" / "core"
]
SOURCE_FILES = [
    ROOT / "frontend" / "src" / "app.js"
]
INCLUDE_EXTENSIONS = (".py", ".js", ".ts", ".html", ".css", ".json")

INTRO_TEXT = """This entire text was run from fmlite/ai-summary/createSummary.py and turned into a text message you are now seeing.
What you see here is an overview of the 'fmlite' project’s source code and documented file purposes written in the author's own words.
The purposes are stored in a separate purpose.json file in the same folder as the script and is updated by me as i learn more about development in general, as i am still a beginner.
Files marked 'PURPOSE_NOT_DEFINED' have no documented purpose yet.

After reading this text in full, write back the total number of PURPOSE_NOT_DEFINED files, and explain in 125 words or less a summary of what this project is about and what it does.

"""

# ---------------- HELPERS ----------------

def load_purposes():
    """Load existing purpose.json if it exists."""
    if not PURPOSE_FILE.exists():
        return {}
    with open(PURPOSE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return {k.replace("\\", "/"): v for k, v in data.items()}

def is_included(file_path: Path) -> bool:
    return file_path.suffix in INCLUDE_EXTENSIONS

def collect_files():
    """Return sorted list of relative files to include."""
    files = []
    for folder in SOURCE_FOLDERS:
        for root_dir, _, filenames in os.walk(folder):
            for f in sorted(filenames):
                path = Path(root_dir) / f
                if is_included(path):
                    files.append(path.relative_to(ROOT))
    for f in SOURCE_FILES:
        if f.exists() and is_included(f):
            files.append(f.relative_to(ROOT))
    return sorted(files)

def update_purposes(files, existing_purposes):
    """Merge new files into purposes, preserving existing entries."""
    updated = existing_purposes.copy()
    for f in files:
        f_str = str(f).replace("\\", "/")
        if f_str not in updated:
            updated[f_str] = "PURPOSE_NOT_DEFINED"
    return updated

def build_tree(files, purposes):
    """Build a text tree with purposes."""
    tree = {}
    for file in files:
        parts = list(file.parts)
        subtree = tree
        for part in parts[:-1]:
            subtree = subtree.setdefault(part, {})
        subtree[parts[-1]] = purposes.get(str(file).replace("\\", "/"), "PURPOSE_NOT_DEFINED")

    def render(subtree, prefix=""):
        lines = []
        items = list(subtree.items())
        for i, (name, val) in enumerate(items):
            connector = "└─" if i == len(items)-1 else "├─"
            if isinstance(val, dict):
                lines.append(f"{prefix}{connector} {name}/")
                extension = "   " if i == len(items)-1 else "│  "
                lines.extend(render(val, prefix + extension))
            else:
                lines.append(f"{prefix}{connector} {name} : {val}")
        return lines

    lines = [f"{ROOT.name}/"]
    lines.extend(render(tree, prefix=""))
    return "\n".join(lines)

# ---------------- TECH STACK ----------------

def load_frontend_stack():
    pkg_file = ROOT / "frontend" / "package.json"
    if not pkg_file.exists():
        return {}
    with open(pkg_file, "r", encoding="utf-8") as f:
        pkg = json.load(f)
    frontend = {
        "Framework": "",
        "UI library": "",
        "HTTP client": "",
        "Bundler / Scripts": {}
    }
    deps = pkg.get("dependencies", {})
    dev_deps = pkg.get("devDependencies", {})
    scripts = pkg.get("scripts", {})
    
    # Basic detection
    if "react" in deps:
        frontend["Framework"] = f"React {deps['react']}"
    if "@mui/material" in deps:
        frontend["UI library"] = f"@mui/material {deps['@mui/material']}"
    if "axios" in deps:
        frontend["HTTP client"] = f"axios {deps['axios']}"
    frontend["Bundler / Scripts"] = scripts
    return frontend

def load_backend_stack():
    backend = {
        "Language": "Python 3.x",
        "Framework": "",
        "ORM / DB tools": "",
        "Scripts / Entrypoints": {}
    }
    # detect main scripts
    backend_dir = ROOT / "backend"
    if (backend_dir / "framework" / "main.py").exists():
        backend["Scripts / Entrypoints"]["main.py"] = "application entry"
    if (backend_dir / "database" / "generateData.py").exists():
        backend["Scripts / Entrypoints"]["generateData.py"] = "data generation"
    
    # optional: detect framework from requirements.txt
    req_file = ROOT / "backend" / "requirements.txt"
    if req_file.exists():
        with open(req_file, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]
        if any("fastapi" in line.lower() for line in lines):
            backend["Framework"] = "FastAPI"
        if any("sqlalchemy" in line.lower() for line in lines):
            backend["ORM / DB tools"] = "SQLAlchemy / SQLite"
    return backend

def render_stack(stack_dict, prefix=""):
    """Render stack info in tree-style format"""
    lines = []
    for key, val in stack_dict.items():
        connector = "├─" if isinstance(val, dict) and val else "├─"
        if isinstance(val, dict) and val:
            lines.append(f"{prefix}{connector} {key}:")
            sub_connector = "│  "
            for i, (k2, v2) in enumerate(val.items()):
                last = "└─" if i == len(val)-1 else "├─"
                lines.append(f"{prefix}{sub_connector}{last} {k2}: {v2}")
        else:
            lines.append(f"{prefix}{connector} {key}: {val}")
    return lines

# ---------------- MAIN ----------------

def main():
    AI_SUMMARY_DIR.mkdir(exist_ok=True)

    # Step 1: Collect files
    files = collect_files()

    # Step 2: Load and update purposes
    existing_purposes = load_purposes()
    updated_purposes = update_purposes(files, existing_purposes)

    # Step 3: Save updated purpose.json alphabetically
    with open(PURPOSE_FILE, "w", encoding="utf-8") as f:
        json.dump(dict(sorted(updated_purposes.items())), f, indent=4)

    # Step 4: Build tree and write ai-summary.txt
    tree_text = build_tree(files, updated_purposes)

    # Step 5: Load tech stack
    frontend_stack = load_frontend_stack()
    backend_stack = load_backend_stack()

    # Step 6: Render stack
    stack_lines = ["\n--- TECH STACK (frontend & backend) ---"]
    stack_lines.append("Frontend/")
    stack_lines.extend(["├─ " + line for line in render_stack(frontend_stack, prefix="")])
    stack_lines.append("\nBackend/")
    stack_lines.extend(["├─ " + line for line in render_stack(backend_stack, prefix="")])

    with open(AI_SUMMARY_FILE, "w", encoding="utf-8") as f:
        f.write(INTRO_TEXT)
        f.write(tree_text)
        f.write("\n")
        f.write("\n".join(stack_lines))

    print(f"AI summary saved to {AI_SUMMARY_FILE} and purpose.json updated with {len(updated_purposes)} entries.")

if __name__ == "__main__":
    main()
