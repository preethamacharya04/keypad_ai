class HealthAgent:
    def __init__(self, ledger, brain):
        self.ledger = ledger
        self.brain = brain

    def get_main_menu(self, lang):
        if lang == 'en':
            return "Welcome to AI Health Assistant. For Diabetes care, press 1. For Blood Pressure care, press 2. For Symptom Checker, press 3. Press 4 for medicine reminder."
        return "ಎಐ ಆರೋಗ್ಯ ಸಹಾಯಕರಿಗೆ ಸ್ವಾಗತ. ಮಧುಮೇಹ ಸೇವೆಗೆ 1 ಒತ್ತಿರಿ. ರಕ್ತದ ಒತ್ತಡ ಸೇವೆಗೆ 2 ಒತ್ತಿರಿ. ಲಕ್ಷಣ ಪರಿಶೀಲನೆಗೆ 3 ಒತ್ತಿರಿ."

    def get_bp_menu(self, lang):
        if lang == 'en':
            return "Please select your condition. If you feel low blood pressure symptoms like dizziness, press 1. If your blood pressure is normal, press 2. If your blood pressure is high, press 3."
        return "ದಯವಿಟ್ಟು ನಿಮ್ಮ ಸ್ಥಿತಿಯನ್ನು ಆಯ್ಕೆ ಮಾಡಿ. ತಲೆ ಸುತ್ತುವಿಕೆ ಇರುವ ಕಡಿಮೆ ರಕ್ತದ ಒತ್ತಡ ಇದ್ದರೆ 1 ಒತ್ತಿರಿ. ಸಾಮಾನ್ಯವಾಗಿದ್ದರೆ 2 ಒತ್ತಿರಿ. ಹೆಚ್ಚು ಇದ್ದರೆ 3 ಒತ್ತಿರಿ."

    def get_bp_advice(self, level, lang):
        advice = {
            "low": {
                "en": "You may have low blood pressure. Drink more water and include a little salt in your diet. Take buttermilk with salt, lemon water, and banana. Walk slowly for 10 to 15 minutes daily. Avoid standing suddenly.",
                "kn": "ನಿಮ್ಮ ರಕ್ತದ ಒತ್ತಡ ಕಡಿಮೆ ಇರಬಹುದು. ಹೆಚ್ಚು ನೀರು ಕುಡಿಯಿರಿ ಮತ್ತು ಸ್ವಲ್ಪ ಉಪ್ಪು ಸೇರಿಸಿ. ಉಪ್ಪಿನ ಮಜ್ಜಿಗೆ, ಲಿಂಬೆ ನೀರು, ಬಾಳೆಹಣ್ಣು ಸೇವಿಸಿ. ನಿಧಾನವಾಗಿ 10 ರಿಂದ 15 ನಿಮಿಷ ನಡೆಯಿರಿ. ತಕ್ಷಣ ಎದ್ದು ನಿಲ್ಲಬೇಡಿ."
            },
            "normal": {
                "en": "Your blood pressure is normal. Continue healthy food like vegetables, fruits, and grains. Avoid excess salt and oil. Walk at least 30 minutes daily. Do regular checkups if possible.",
                "kn": "ನಿಮ್ಮ ರಕ್ತದ ಒತ್ತಡ ಸಾಮಾನ್ಯವಾಗಿದೆ. ತರಕಾರಿ, ಹಣ್ಣು, ಧಾನ್ಯಗಳನ್ನು ಸೇವಿಸಿ. ಹೆಚ್ಚು ಉಪ್ಪು ಮತ್ತು ಎಣ್ಣೆ ತಪ್ಪಿಸಿ. ದಿನಕ್ಕೆ 30 ನಿಮಿಷ ನಡೆಯಿರಿ. ಸಾಧ್ಯವಾದರೆ ನಿಯಮಿತವಾಗಿ ಪರೀಕ್ಷೆ ಮಾಡಿಸಿ."
            },
            "high": {
                "en": "Your blood pressure may be high. Reduce salt and avoid fried foods. Eat spinach, cucumber, tomato, and fruits. Walk 30 minutes daily. If it remains high, consult a doctor.",
                "kn": "ನಿಮ್ಮ ರಕ್ತದ ಒತ್ತಡ ಹೆಚ್ಚು ಇರಬಹುದು. ಉಪ್ಪನ್ನು ಕಡಿಮೆ ಮಾಡಿ ಮತ್ತು ಹುರಿದ ಆಹಾರ ತಪ್ಪಿಸಿ. ಪಾಲಕ್, ಸೌತೆಕಾಯಿ, ಟೊಮೇಟೊ ಮತ್ತು ಹಣ್ಣು ಸೇವಿಸಿ. ದಿನಕ್ಕೆ 30 ನಿಮಿಷ ನಡೆಯಿರಿ. ಮುಂದುವರಿದರೆ ವೈದ್ಯರನ್ನು ಸಂಪರ್ಕಿಸಿ."
            }
        }
        return advice.get(level, {}).get(lang, "")

    def get_symptom_intro(self, lang):
        if lang == 'en':
            return "This is a basic health guide. It does not replace a doctor."
        return "ಇದು ಮೂಲ ಆರೋಗ್ಯ ಮಾರ್ಗದರ್ಶನ ಮಾತ್ರ. ಇದು ವೈದ್ಯರ ಸಲಹೆಯನ್ನು ಬದಲಾಯಿಸುವುದಿಲ್ಲ."

    def get_symptom_menu(self, lang):
        if lang == 'en':
            return "Select your symptom. For fever, press 1. For headache, press 2. For body pain, press 3. For cold and cough, press 4."
        return "ನಿಮ್ಮ ಲಕ್ಷಣವನ್ನು ಆಯ್ಕೆ ಮಾಡಿ. ಜ್ವರಕ್ಕೆ 1 ಒತ್ತಿರಿ. ತಲೆನೋವಿಗೆ 2 ಒತ್ತಿರಿ. ದೇಹ ನೋವಿಗೆ 3 ಒತ್ತಿರಿ. ಜಲದೋಷ ಅಥವಾ ಕೆಮ್ಮಿಗೆ 4 ಒತ್ತಿರಿ."

    def get_symptom_advice(self, symptom, lang):
        advice = {
            "fever": {
                "en": "You selected fever. Drink plenty of water and take rest. Eat light food like porridge or soup. You may take paracetamol such as Dolo 650 after food if needed. If it continues for more than two days, consult a doctor.",
                "kn": "ನೀವು ಜ್ವರ ಆಯ್ಕೆ ಮಾಡಿದ್ದೀರಿ. ಹೆಚ್ಚು ನೀರು ಕುಡಿಯಿರಿ ಮತ್ತು ವಿಶ್ರಾಂತಿ ತೆಗೆದುಕೊಳ್ಳಿ. ಗಂಜಿ ಅಥವಾ ಸೂಪ್ ಸೇವಿಸಿ. ಅಗತ್ಯವಿದ್ದರೆ Dolo 650 ತೆಗೆದುಕೊಳ್ಳಬಹುದು. ಎರಡು ದಿನಗಳಿಗಿಂತ ಹೆಚ್ಚು ಇದ್ದರೆ ವೈದ್ಯರನ್ನು ಸಂಪರ್ಕಿಸಿ."
            },
            "headache": {
                "en": "You selected headache. Drink enough water and rest. Avoid long mobile usage. You may take paracetamol if needed. If it continues frequently, consult a doctor.",
                "kn": "ನೀವು ತಲೆನೋವು ಆಯ್ಕೆ ಮಾಡಿದ್ದೀರಿ. ನೀರು ಕುಡಿಯಿರಿ ಮತ್ತು ವಿಶ್ರಾಂತಿ ತೆಗೆದುಕೊಳ್ಳಿ. ಮೊಬೈಲ್ ಬಳಕೆ ಕಡಿಮೆ ಮಾಡಿ. ಅಗತ್ಯವಿದ್ದರೆ ಔಷಧಿ ತೆಗೆದುಕೊಳ್ಳಿ. ಮುಂದುವರಿದರೆ ವೈದ್ಯರನ್ನು ಸಂಪರ್ಕಿಸಿ."
            },
            "body_pain": {
                "en": "You selected body pain. Take rest and drink warm water. Do light walking or stretching. You may take paracetamol if needed. If pain continues, consult a doctor.",
                "kn": "ನೀವು ದೇಹ ನೋವು ಆಯ್ಕೆ ಮಾಡಿದ್ದೀರಿ. ವಿಶ್ರಾಂತಿ ತೆಗೆದುಕೊಳ್ಳಿ ಮತ್ತು ಬೆಚ್ಚಗಿನ ನೀರು ಕುಡಿಯಿರಿ. ಸ್ವಲ್ಪ ನಡೆ ಅಥವಾ ಸ್ಟ್ರೆಚಿಂಗ್ ಮಾಡಿ. ಅಗತ್ಯವಿದ್ದರೆ ಔಷಧಿ ತೆಗೆದುಕೊಳ್ಳಿ. ಮುಂದುವರಿದರೆ ವೈದ್ಯರನ್ನು ಸಂಪರ್ಕಿಸಿ."
            },
            "cold_cough": {
                "en": "You selected cold and cough. Drink warm water and avoid cold drinks. Take ginger tea or turmeric milk. You may take cetirizine if needed. If it continues for more than three days, consult a doctor.",
                "kn": "ನೀವು ಜಲದೋಷ ಅಥವಾ ಕೆಮ್ಮು ಆಯ್ಕೆ ಮಾಡಿದ್ದೀರಿ. ಬೆಚ್ಚಗಿನ ನೀರು ಕುಡಿಯಿರಿ ಮತ್ತು ತಣ್ಣನೆಯ ಪದಾರ್ಥ ತಪ್ಪಿಸಿ. ಶುಂಠಿ ಚಹಾ ಅಥವಾ ಅರಿಶಿನ ಹಾಲು ಸೇವಿಸಿ. ಅಗತ್ಯವಿದ್ದರೆ ಸೆಟಿರಿಜಿನ್ ತೆಗೆದುಕೊಳ್ಳಬಹುದು. ಮೂರು ದಿನಗಳಿಗಿಂತ ಹೆಚ್ಚು ಇದ್ದರೆ ವೈದ್ಯರನ್ನು ಸಂಪರ್ಕಿಸಿ."
            }
        }
        return advice.get(symptom, {}).get(lang, "")

    def get_safety_message(self, lang):
        if lang == 'en':
            return " If symptoms become severe, visit the nearest hospital immediately."
        return " ಲಕ್ಷಣಗಳು ಗಂಭೀರವಾದರೆ ತಕ್ಷಣ ಆಸ್ಪತ್ರೆಗೆ ಹೋಗಿ."

    def get_sugar_menu(self, lang):
        if lang == 'en':
            return "Please enter your fasting blood sugar range. If your sugar is below 70, press 1. If it is between 70 and 130, press 2. If it is above 130, press 3."
        return "ದಯವಿಟ್ಟು ನಿಮ್ಮ ರಕ್ತದ ಸಕ್ಕರೆ ಶ್ರೇಣಿಯನ್ನು ಆಯ್ಕೆ ಮಾಡಿ. 70 ಕ್ಕಿಂತ ಕಡಿಮೆ ಇದ್ದರೆ 1 ಒತ್ತಿರಿ. 70 ರಿಂದ 130 ನಡುವೆ ಇದ್ದರೆ 2 ಒತ್ತಿರಿ. 130 ಕ್ಕಿಂತ ಹೆಚ್ಚು ಇದ್ದರೆ 3 ಒತ್ತಿರಿ."

    def get_sugar_advice(self, level, lang):
        advice = {
            "low": {
                "en": "Your blood sugar is low. Eat a piece of candy or drink half a cup of fruit juice immediately. Wait 15 minutes and check again. Do not skip meals.",
                "kn": "ನಿಮ್ಮ ರಕ್ತದ ಸಕ್ಕರೆ ಕಡಿಮೆ ಇದೆ. ತಕ್ಷಣ ಒಂದು ಮಿಠಾಯಿ ತಿನ್ನಿರಿ ಅಥವಾ ಅರ್ಧ ಕಪ್ ಹಣ್ಣಿನ ರಸ ಕುಡಿಯಿರಿ. 15 ನಿಮಿಷ ಕಾಯಿರಿ ಮತ್ತು ಮತ್ತೆ ಪರೀಕ್ಷಿಸಿ. ಊಟ ಬಿಡಬೇಡಿ."
            },
            "normal": {
                "en": "Your blood sugar is in a safe range. Maintain your current diet of vegetables and whole grains. Walk for at least 30 minutes daily to keep it stable.",
                "kn": "ನಿಮ್ಮ ರಕ್ತದ ಸಕ್ಕರೆ ಸುರಕ್ಷಿತ ಶ್ರೇಣಿಯಲ್ಲಿದೆ. ತರಕಾರಿ ಮತ್ತು ಧಾನ್ಯಗಳ ಆಹಾರವನ್ನು ಮುಂದುವರಿಸಿ. ಇದನ್ನು ಸ್ಥಿರವಾಗಿಡಲು ದಿನಕ್ಕೆ ಕನಿಷ್ಠ 30 ನಿಮಿಷ ನಡೆಯಿರಿ."
            },
            "high": {
                "en": "Your blood sugar is high. Avoid sweets, sugary drinks, and white rice. Eat more fiber-rich foods like bitter gourd and fenugreek. Exercise daily. If it remains high, consult a doctor.",
                "kn": "ನಿಮ್ಮ ರಕ್ತದ ಸಕ್ಕರೆ ಹೆಚ್ಚು ಇದೆ. ಸಿಹಿತಿಂಡಿ, ಸಕ್ಕರೆ ಪಾನೀಯ ಮತ್ತು ಬಿಳಿ ಅನ್ನವನ್ನು ತಪ್ಪಿಸಿ. ಹಾಗಲಕಾಯಿ ಮತ್ತು ಮೆಂತ್ಯದಂತಹ ನಾರಿನಂಶವಿರುವ ಆಹಾರ ಸೇವಿಸಿ. ಪ್ರತಿದಿನ ವ್ಯಾಯಾಮ ಮಾಡಿ. ಮುಂದುವರಿದರೆ ವೈದ್ಯರನ್ನು ಸಂಪರ್ಕಿಸಿ."
            }
        }
        return advice.get(level, {}).get(lang, "")

    def get_medicine_reminder(self, lang):
        if lang == 'en':
            return "This is the Medicine Reminder module. Did you take your pills today?"
        return "ಇದು ಔಷಧಿ ಜ್ಞಾಪನೆ ಮಾಡ್ಯೂಲ್. ನೀವು ಇಂದು ನಿಮ್ಮ ಮಾತ್ರೆಗಳನ್ನು ತೆಗೆದುಕೊಂಡಿದ್ದೀರಾ?"

    # Legacy support if needed
    def get_triage_instructions(self, level, lang):
        if lang == 'en':
            return f"Follow these {level} level instructions."
        return f"ಈ {level} ಮಟ್ಟದ ಸೂಚನೆಗಳನ್ನು ಅನುಸರಿಸಿ."

    def trigger_hospital_alert(self, phone):
        print(f"Hospital alert triggered for {phone}")
