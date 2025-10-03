# AI Overview

## AI Instructions
When reviewing this readme:
- Validate that all folders and files exist as described in the ## Structure hierarchy.
- Ensure file descriptions (e.g., comments or README notes about purpose) match their actual functionality.
- Missing, extra, or misnamed folders/files.
- Incorrect file paths or descriptions that don’t match the file’s purpose.
- Dependencies: list only what is actually required to run the backend/frontend.  

Return 'No readme changes needed' if there are no factual errors. Otherwise, provide minimal corrections that fix only the errors.


---

## Structure

project/
├── backend/
│   ├── core/
│   │   ├── backend_emulator.py   # Flask API for frontend
│   │   ├── database/
│   │   │   ├── data.json         # Player, team, match data
│   │   │   ├── generateData.py   # Generates data.json
│   │   ├── fetch-api/           # Placeholder for future API logic
├── frontend/
│   ├── src/
│   │   ├── App.js               # Main app container
│   │   ├── core/
│   │   │   ├── components/
│   │   │   │   ├── sidebar.js    # Sidebar navigation
│   │   │   │   ├── topbar.js     # Top bar/header
│   │   │   ├── pages/
│   │   │   │   ├── players.js    # Player list and editor

---

## Dependencies

### Backend
- Python 3
- Flask
- Flask-CORS
- Virtual environment (venv)

### Frontend
- Node.js
- npm
- React
- Material-UI (MUI)
- Other npm packages as listed in package.json