# Fonction pour calculer l'IMC (BMI)
def calculate_bmi(height, weight):
    """
    Calcule l'IMC à partir de la hauteur (en mètres) et du poids (en kg).
    """
    bmi = weight / (height ** 2)
    return bmi

# Fonction pour calculer le BMR (BMR)
def calculate_bmr(height, weight, age, gender):
    """
    Calcule le BMR à partir de la hauteur (en cm), du poids (en kg),
    de l'âge (en années) et du sexe.
    """
    if gender.lower() == 'male':
        # Équation pour les hommes
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender.lower() == 'female':
        # Équation pour les femmes
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Le sexe doit être soit 'male' soit 'female'.")
    return bmr