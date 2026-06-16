# Expense Tracker
## Setup

1. `pip install -r requirements.txt`
2. In MySQL, create a database and user:
   ```sql
   CREATE DATABASE expense_tracker;
   CREATE USER 'expense_app'@'localhost' IDENTIFIED BY 'changeme';
   GRANT ALL PRIVILEGES ON expense_tracker.* TO 'expense_app'@'localhost';
   ```
3. Copy `.env.example` to `.env` and fill in your DB credentials and the
   local path to your cloned private GitHub repo (`BACKUP_REPO_PATH`).
4. Make sure `git push` already works from that repo path without prompting
   (SSH key set up) and that the `mysqldump` CLI tool is on your PATH.
5. Run it: `python main.py`

## What's here

- `main.py` — the TUI: a form to add an expense, a table to see them.
- `db.py` — talks to MySQL directly (one table, no ORM yet).
- `backup.py` — on app close, dumps the DB and pushes it to your repo.

## Known rough edges (left for later, on purpose)

- No input validation (bad amount text will crash on `float()`).
- No categories table — category is just a free-text string for now.
- Backup runs synchronously on close, so quitting will pause briefly.
- No tests yet — once this is structured the way you want, the next step
  is splitting parsing/validation into pure functions that don't touch
  MySQL, so those can be unit tested without a live connection.
