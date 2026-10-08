# Blood Bank and Donor Management System

A Django application for managing blood donors, blood groups, requests, and contacts.

## Requirements

- Python 3.10 or newer
- Dependencies in `requirements.txt`

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The project uses SQLite by default and creates the database locally. Local database
files and uploaded media are intentionally excluded from Git.

## Configuration

Set `DJANGO_SECRET_KEY` to a unique value for deployments. The built-in fallback
secret is intended only for local development.

Google Maps is optional. Set `GOOGLE_MAPS_API_KEY` to a key restricted to the
application's domains to enable the map integration.

To use MySQL instead of SQLite, set `USE_SQLITE=false` and configure `DB_NAME`,
`DB_USER`, `DB_PASSWORD`, `DB_HOST`, and `DB_PORT`. Install a compatible MySQL
driver in that environment.
