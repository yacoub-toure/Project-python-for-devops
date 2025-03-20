import unittest
from health_utils import calculate_bmi, calculate_bmr

class TestHealthUtils(unittest.TestCase):
    def test_calculate_bmi(self):
        # Test d'un BMI normal
        height = 1.75  # 175 cm
        weight = 70      # 70 kg
        expected_bmi = 70 / (1.75 ** 2)
        self.assertAlmostEqual(calculate_bmi(height, weight), expected_bmi, places=2)

    def test_calculate_bmr_male(self):
        # Test du BMR pour un homme
        height = 175    # 175 cm
        weight = 70     # 70 kg
        age = 30       # 30 ans
        gender = 'male'
        expected_bmr = 88.362 + (13.397 * 70) + (4.799 * 175) - (5.677 * 30)
        self.assertAlmostEqual(calculate_bmr(height, weight, age, gender), expected_bmr, places=2)

    def test_calculate_bmr_female(self):
        # Test du BMR pour une femme
        height = 160    # 160 cm
        weight = 55     # 55 kg
        age = 25       # 25 ans
        gender = 'female'
        expected_bmr = 447.593 + (9.247 * 55) + (3.098 * 160) - (4.330 * 25)
        self.assertAlmostEqual(calculate_bmr(height, weight, age, gender), expected_bmr, places=2)

if __name__ == '__main__':
    unittest.main()