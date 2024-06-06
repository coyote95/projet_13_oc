FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

# Commande par défaut pour démarrer le serveur Django
CMD ["python", "manage.py", "runserver", "127.0.0.1:8080"]
