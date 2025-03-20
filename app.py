# Importation de Flask pour créer l'API
from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

# Création de l'application Flask
app = Flask(__name__)
@app.route("/")
def home():
    return jsonify({"message": "Welcome to calculates health metrics (BMI and BMR) using a REST API.  Now it is modified"})

# Endpoint pour calculer l'IMC (BMI)
@app.route('/bmi', methods=['POST'])
def bmi():
    # Récupère les données de la requête
    data = request.json
    height = data['height']  # Hauteur en mètres
    weight = data['weight']  # Poids en kilogrammes

    # Calcule l'IMC
    bmi_value = calculate_bmi(height, weight)

    # Retourne le résultat en JSON
    return jsonify({
        "height": height,
        "weight": weight,
        "bmi": round(bmi_value, 2)
    })

# Endpoint pour calculer le MB (BMR)
@app.route('/bmr', methods=['POST'])
def bmr():
    # Récupère les données de la requête
    data = request.json
    height = data['height']    # Hauteur en centimètres
    weight = data['weight']    # Poids en kilogrammes
    age = data['age']          # Âge en années
    gender = data['gender']    # Sexe ('male' ou 'female')

    # Calcule le BMR
    bmr_value = calculate_bmr(height, weight, age, gender)

    # Retourne le résultat en JSON
    return jsonify({
        "height": height,
        "weight": weight,
        "age": age,
        "gender": gender,
        "bmr": round(bmr_value, 2)
    })

# Lance l'application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)