# Elf app

Simple streamlit app assigning an elf from a DB table based on an inputted name.
Lots of improvement potential.

- Azure table needs to be pre-populated for all users, see upload_data.py
- Logic for streamlit app in app.py
- Pipeline for deploying to azure web app in .github/workflows

Improvements
- Define resources used as IaC, clickopsed today
- Improve logic of app, not proud of the nested if/elses
- Improve logic in general (Made quick and dirty as christmas always seem to be just around the corner when I start)
- Add tests
- Migrate to a frontend framework