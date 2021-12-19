# Flask and TailwindCSS SAAS App Starter Template

## How to use

1. Clone this repo and create a virtual environment (`python3 -m venv venv`) for use with this application.
2. Activate the virtual environment (`source venv/bin/activate`) and run `pip install -r requirements.txt` to install package dependencies.
3. Run `npm install` to install node packages (only Tailwind in this case as per the package.json file).
4. In one terminal - run `npm run dev`- this will start the Tailwind JIT Watcher and will compile your CSS on the fly.
5. In the second terminal - setup some ENV variables required to run the Flask application:
   5.1 Run `export FLASK_APP=run.py`
   5.2 Run `export FLASK_ENV=development`
   5.3 Run `flask run` to start the Flask development server.
6. You can now add/remove CSS in your jinja templates, it will be auto-compiled by the compiler running in step 4.
7. You will now see the Tailwind CSS styles when you refresh your browser (Flask server) window.

## Key Features

JINJA2 TEMPLATES
FLASH MESSAGES
FLASK WTFORMS
FLASK SQLALCHEMY
FLASK LOGIN
FLASK ASSETS (CACHE BUSTING)
FLASK CACHING
TAILWIND CLI
STRIPE PAYMENTS
POSTGRES
REDIS
CELERY BACKGROUND JOBS AND SCHEDULED JOBS
