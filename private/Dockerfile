FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir flask
COPY private/app.py .
COPY index.html .
ENV PORT=8202
EXPOSE 8202
CMD ["python", "app.py"]
