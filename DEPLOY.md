Deployment notes:
- Set SECRET_KEY and DEBUG in environment for production.
- Use git lfs for large model files or use MODEL_URL env var and download at startup.
- Render start command: gunicorn agri_project.wsgi:application --bind 0.0.0.0:$PORT
