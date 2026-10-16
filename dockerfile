FROM python:3.12-slim
WORKDIR /app
copy app/ /app/
RUN python -m compileall -q /app
EXPOSE 8000
CMD ["python", "-u", "main.py"]
