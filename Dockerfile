# Utilise une image Python de base
FROM python:3.9-slim

# Définit le répertoire de travail
WORKDIR /app

# Copie les dépendances
COPY requirements.txt .

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copie l'application
COPY . .

# Expose le port de l'application
EXPOSE 5000

# Commande pour lancer l'application
CMD ["python", "app.py"]