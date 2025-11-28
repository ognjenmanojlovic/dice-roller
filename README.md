# 🎲 Dice Roller -- Flask Learning Project

This project is a small **Flask application** built to learn and
practice:

-   Application Factory pattern
-   Blueprints (`/api`)
-   JSON API endpoints
-   Custom exception handling
-   Jinja2 templates
-   Frontend interaction with JavaScript (`fetch`)
-   Clean project structure
-   Git/GitHub workflow (main + development branches)

The goal of the project was to understand how a real Flask application
is structured and how APIs and templates work together.

------------------------------------------------------------------------

## 🚀 Features

### 🔹 Frontend

-   HTML templates using **Jinja2**
-   Dynamic content rendering
-   Simple UI to display existing dice
-   Form to add new dice via JavaScript

### 🔹 Backend

-   `/api/dices` endpoint (GET, POST)
-   Custom Python exceptions:
    -   `InvalidDiceError`
    -   `DiceAlreadyExistsError`
-   Proper Flask error handlers returning clean JSON messages
-   In-memory "database" (`dices` list)

### 🔹 Architecture

    src/
    │   app.py
    │   errors.py
    │   api.py
    │   __init__.py
    │
    ├── templates/
    │     hello.html
    │     home.html
    │     dice.html
    │     layout.html.j2
    │
    ├── static/
    │     layout.css

Backend logic is separated using:

-   `create_app()` in `__init__.py`
-   API routes in a **Blueprint** (`api_bp`)
-   Custom errors in a separate module

------------------------------------------------------------------------

## 🧪 API Endpoints

### GET `/api/dices`

Returns all available dice:

``` json
{
  "available_dices": [
    {"numberOfSides": 6},
    {"numberOfSides": 20}
  ]
}
```

### POST `/api/dices`

Create a new dice:

**Request example:**

``` json
{
  "numberOfSides": 12
}
```

**Success response:**

``` json
{
  "message": "dice created"
}
```

**Possible error responses:** - `400` → Invalid number of sides\
- `409` → Dice already exists
- `500` → Unexpected server error

------------------------------------------------------------------------

## 💻 Running the project locally

### 1. Activate venv (macOS / zsh)

``` bash
source dice-venv/bin/activate
```

### 2. Start Flask with debug

``` bash
python -m flask --app src.app run --debug
```

### 3. Open in browser

    http://127.0.0.1:5000

------------------------------------------------------------------------

## 🌿 Git Workflow (Learning Goal)

This project uses a professional workflow:

-   `main` → clean branch with README only
-   `development` → full project with all commits
-   All features are developed on `development`
-   Final version merged into `main` via Pull Request

This mirrors a real-world team setup.

------------------------------------------------------------------------

## 📚 Purpose of this Project

The purpose was to:

-   learn Flask fundamentals
-   understand API design
-   work with Blueprints
-   integrate JavaScript with the backend
-   structure a clean Python project
-   practice a real development workflow with Git

------------------------------------------------------------------------

## 🧑‍💻 Author

**0gisha (ognjenmanojlovic)**