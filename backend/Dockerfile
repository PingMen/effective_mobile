ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}

WORKDIR /app

RUN useradd -m appuser

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown==appuser app.py .

USER appuser

EXPOSE 8080

CMD ["python3", "app.py"]