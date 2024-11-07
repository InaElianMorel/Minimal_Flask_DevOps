# Minimal Flask App for Heroku Deployment

This app and repository aim to consolidate all necessary files and best practices for deploying a Flask application on Heroku. Below is a checklist to ensure a smooth and robust deployment.

## Deployment Checklist
WHAT HAS TO BE DONE 

- [X]**GitHub Actions**: Set up for tests and Continuous Integration.
- [X]**GitHub Actions**: Automated deployment to test and main branches.
- []**Flask Login**: Implement secure user authentication.
- []**Bootstrap 5**: Use for frontend styling and responsive design.
- []**Docker**: Enable local testing with containers for MQTT, database, and Redis.
- []**Code Coverage**: Aim for a minimal coverage threshold to maintain code quality.
- [X]**Monitoring** : Add new Relic to monitor performance on the heroku app 
- [X]**Monitoring** : Prometheus to monitor locally
- [X]**Monitoring** : Handle the fact that we don t monitor the same way locally and remotly
- []**Jenkins (Optional)**: Consider Jenkins as an additional CI/CD pipeline if required.
- []**Rollbacks (Optional)**: Automatic rollbacks on heroku
- []**Documentations**: Find documentations tools Pdocs ? API ? 

## 1. GitHub Setup
- Create (at least) two branches: `dev` and `main`.
- Protect the `main` branch to prevent direct pushes.
- Ensure all changes to `main` are merged via pull requests and include tests and code reviews.
- 
## 2. Monitoring Performance
With an app deployed to Heroku : add the New Relic add-on
Install new relic in the venv and add it to the requirements:  
```bash
pip install new relic
```
Then change the Procfile to : 
```bash 
web: flask db upgrade; newrelic-admin run-program  gunicorn -w 1 your_app:app
```

Add the config value : 
```bash
heroku config:set --app your_app NEW_RELIC_APP_NAME='your_app' 
```
Push and deploy your app
Test that the set up works : 
```bash
heroku run --app your_app newrelic-admin validate-config - stdout
```

Click on new relic add on to see metrics