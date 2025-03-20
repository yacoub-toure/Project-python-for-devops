# Charge les variables d'environnement
#include .env
#export
BMI_URL=http://localhost:5001/bmi  
BMR_URL=http://localhost:5001/bmr


# Commandes du Makefile  
.PHONY: init run test test-api test-api-async build clean
# Commande pour installer les dépendances
init:
	@echo "Installation des dépendances..."
	pip install -r requirements.txt

# Commande pour lancer l'application
run:
	@echo "Démarrage de l'application..."
	python app.py

# Commande pour exécuter les tests
test:
	@echo "Exécution des tests..."
	python -m unittest test.py


# Commande pour exécuter les tests API  
test-api:  
	@echo "Exécution des tests API..."  
	@echo "Test de l'endpoint BMI..."  
	@curl -X POST -H "Content-Type: application/json" -d '{"height": 1.75, "weight": 70}' $(BMI_URL) | jq .  
	@echo "\nTest de l'endpoint BMR..."  
	@curl -X POST -H "Content-Type: application/json" -d '{"height": 175, "weight": 70, "age": 30, "gender": "male"}' $(BMR_URL) | jq .
# Commande pour construire l'image Docker
build:
	@echo "Construction de l'image Docker..."
	docker build -t health-calculator .

# Commande pour nettoyer le projet
clean:
	@echo "Nettoyage du projet..."
	rm -rf __pycache__ *.log