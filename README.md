# Minimal Flask App for Heroku Deployment

This app and repository aim to consolidate all necessary files and best practices for deploying a Flask application on Heroku. Below is a checklist to ensure a smooth and robust deployment.

## Deployment Checklist
When deploying this application, ensure the following are considered:

- **GitHub Actions**: Set up for tests and Continuous Integration.
- **GitHub Actions**: Automated deployment to test and main branches.
- **Flask Login**: Implement secure user authentication.
- **Bootstrap 5**: Use for frontend styling and responsive design.
- **Docker**: Enable local testing with containers for MQTT, database, and Redis.
- **Code Coverage**: Aim for a minimal coverage threshold to maintain code quality.
- **Prometheus**: Integrate for performance monitoring and analytics.
- **Jenkins (Optional)**: Consider Jenkins as an additional CI/CD pipeline if required.
- **Rollbacks (Optional)**: Automatic rollbacks on heroku
- **Documentations**: Find documentations tools Pdocs ? API ? 

## 1. GitHub Setup
- Create (at least) two branches: `dev` and `main`.
- Protect the `main` branch to prevent direct pushes.
- Ensure all changes to `main` are merged via pull requests and include tests and code reviews.