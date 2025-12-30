# SGC CLI – Stargate Command Personnel Management

A Python command-line app for managing Stargate Command personnel and mission reports.

This project is my practice ground for building a data management system in Python
that I can later expand with SQL and a web-based UI (TypeScript).

## Current Features

- Text-based main menu:
  - `1` – List personnel
  - `2` – Add personnel
  - `3` – List missions
  - `4` – Add mission report
  - `0` – Exit
- Hard-coded initial data:
  - Example: Colonel Jack O'Neill on SG-1 with an Abydos mission report.
- Personnel management:
  - List all personnel with id, name, rank, assignment, and status.
  - Add new personnel via CLI prompts.
- Mission reports:
  - List all missions with id, title, date, team, and commanding officer id.
  - Add new mission reports:
    - Enter title, team, date, and summary.
    - Automatically link all personnel assigned to that team as participants.
    - Use the first team member as the commanding officer (for now).

## How to Run

1. Make sure you have Python 3 installed.
2. Clone this repository.
3. From the project root, run:

   ```bash
   python sgc.py
   ```
4. Follow the on-screen menu options.

## Project Structure

- sgc.py – Main CLI entrypoint and menu logic.
- data.py – In-memory “database” with initial personnel and missions.
- models.py – Data models and enums:
    - Personnel
    - Missions
    - Status enum for personnel status (Active, MIA, KIA, Retired)
    - Role enum (reserved for future use in a web UI)


## Roadmap / Future Plans
This project is intentionally simple now so it can evolve as I learn more:

- Replace data.py with a real SQL database (e.g. SQLite/Postgres).
- Add the ability to:
    - Edit personnel (rank, assignment, status).
    - View detailed mission reports, including participant names.
- Expose the core data via an API.
- Build a web-based UI in TypeScript that talks to the backend.
- Add automated tests (possibly with Selenium once a UI exists).
