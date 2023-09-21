FROM python:3.10.12

WORKDIR /app

COPY requirement.txt /app/

RUN pip install --no-cache-dir -r requirement.txt

COPY . /app/

CMD ["python3", "main.py"]
