import os
import json

# AI prompt
AI_INSTRUCTION = (
    "This is a rest"
    "Read all files and folders in this JSON hierarchy to understand their purpose and placement. "
    "Pay special attention to the ai-overview.md file at the root and execute its ai instructions. "
)

# Auto-detect project root by searching for ai-overview.md
def find_project_root(start_path):
    current = os.path.abspath(start_path)
    while True:
        candidate = os.path.join(current, "ai-overview.md")
        if os.path.isfile(candidate):
            return current
        parent = os.path.dirname(current)
        if parent == current:
            # Reached filesystem root
            return None
        current = parent

PROJECT_ROOT = find_project_root(os.path.dirname(__file__))
if not PROJECT_ROOT:
    raise FileNotFoundError("Could not find ai-overview.md in any parent folder.")

# Helper to read file content
def read_file(path):
    if os.path.isfile(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return None

# Recursive folder traversal
def folder_to_dict(path, allowed_files=None, allowed_dirs=None):
    result = {}
    if not os.path.isdir(path):
        return result
    for name in os.listdir(path):
        full_path = os.path.join(path, name)
        if name.startswith("."):
            continue  # ignore hidden files/folders like .DS_Store
        if os.path.isdir(full_path):
            if allowed_dirs and name not in allowed_dirs:
                continue
            result[name] = folder_to_dict(full_path)
        else:
            if allowed_files and name not in allowed_files:
                continue
            result[name] = read_file(full_path)
    return result

# Build summary
summary = {"ai_instruction": AI_INSTRUCTION}

# Read ai-overview.md
overview_path = os.path.join(PROJECT_ROOT, "ai-overview.md")
summary["ai-overview.md"] = read_file(overview_path)

# backend folder
backend_path = os.path.join(PROJECT_ROOT, "backend")
summary["backend"] = folder_to_dict(
    backend_path,
    allowed_dirs=None,
    allowed_files=None
)

# frontend/src folder
frontend_src_path = os.path.join(PROJECT_ROOT, "frontend", "src")
if os.path.isdir(frontend_src_path):
    summary["frontend/src"] = folder_to_dict(
        frontend_src_path,
        allowed_dirs=["core"] + [d for d in os.listdir(frontend_src_path) if os.path.isdir(os.path.join(frontend_src_path, d)) and d != "core"],
        allowed_files=["App.js"]
    )

# Output JSON
output_path = os.path.join(os.path.dirname(__file__), "ai-summary.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=4)

print(f"AI summary JSON created at: {output_path}")
print("Project root detected at:", PROJECT_ROOT)
