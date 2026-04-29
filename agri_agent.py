import random

class AgricultureAgent:
    def __init__(self, ledger, brain):
        self.ledger = ledger
        self.brain = brain

    def get_market_intelligence(self, phone, lang):
        city_price = random.randint(2000, 3500)
        local_price = random.randint(2000, 3500)
        
        if lang == 'en':
            return f"The current price in the city market is {city_price} rupees, and in your local market it is {local_price} rupees. Do you want to sell at this rate? Press 1 to Agree or 2 to Disagree."
        else:
            return f"ನಗರದ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಈಗಿನ ಬೆಲೆ {city_price} ರೂಪಾಯಿಗಳು, ಮತ್ತು ನಿಮ್ಮ ಸ್ಥಳೀಯ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ {local_price} ರೂಪಾಯಿಗಳು. ನೀವು ಈ ದರದಲ್ಲಿ ಮಾರಾಟ ಮಾಡಲು ಬಯಸುವಿರಾ? ಒಪ್ಪಲು 1 ಮತ್ತು ಅಸಮ್ಮತಿಸಲು 2 ಒತ್ತಿ."

    def process_pest_report(self, phone, lang):
        if lang == 'en':
            return "Please select your pest problem. Press 1 for Yellow Leaves, 2 for Root Rot, or 3 for Worms."
        return "ದಯವಿಟ್ಟು ನಿಮ್ಮ ಕೀಟ ಸಮಸ್ಯೆಯನ್ನು ಆಯ್ಕೆ ಮಾಡಿ. ಹಳದಿ ಎಲೆಗಳಿಗಾಗಿ 1, ಬೇರು ಕೊಳೆತಕ್ಕಾಗಿ 2, ಅಥವಾ ಹುಳುಗಳಿಗಾಗಿ 3 ಒತ್ತಿ."

    def get_pest_solution(self, problem, lang):
        solutions = {
            "yellow_leaves": {
                "en": "Yellow leaves often indicate nitrogen deficiency. We recommend using urea or nitrogen-rich organic fertilizers.",
                "kn": "ಹಳದಿ ಎಲೆಗಳು ಸಾರಜನಕದ ಕೊರತೆಯನ್ನು ಸೂಚಿಸುತ್ತವೆ. ನಾವು ಯೂರಿಯಾ ಅಥವಾ ಸಾರಜನಕಯುಕ್ತ ಸಾವಯವ ಗೊಬ್ಬರಗಳನ್ನು ಬಳಸಲು ಶಿಫಾರಸು ಮಾಡುತ್ತೇವೆ."
            },
            "root_rot": {
                "en": "Root rot is caused by excess water. Please improve drainage in your field and apply a fungicide like Carbendazim.",
                "kn": "ಬೇರು ಕೊಳೆತವು ಅತಿಯಾದ ನೀರಿನಿಂದ ಉಂಟಾಗುತ್ತದೆ. ದಯವಿಟ್ಟು ನಿಮ್ಮ ಹೊಲದಲ್ಲಿ ಚರಂಡಿ ವ್ಯವಸ್ಥೆಯನ್ನು ಸುಧಾರಿಸಿ ಮತ್ತು ಕಾರ್ಬೆಂಡಜಿಮ್‌ನಂತಹ ಶಿಲೀಂಧ್ರನಾಶಕವನ್ನು ಬಳಸಿ."
            },
            "worms": {
                "en": "For worm-related problems, use a neem oil spray or bio-pesticides. Avoid using heavy chemicals in the early stages.",
                "kn": "ಹುಳುಗಳಿಗೆ ಸಂಬಂಧಿಸಿದ ಸಮಸ್ಯೆಗಳಿಗೆ, ಬೇವಿನ ಎಣ್ಣೆ ಸಿಂಪಡಣೆ ಅಥವಾ ಜೈವಿಕ ಕೀಟನಾಶಕಗಳನ್ನು ಬಳಸಿ. ಆರಂಭಿಕ ಹಂತದಲ್ಲಿ ಭಾರಿ ರಾಸಾಯನಿಕಗಳನ್ನು ಬಳಸುವುದನ್ನು ತಪ್ಪಿಸಿ."
            }
        }
        return solutions.get(problem, {}).get(lang, "No solution found.")

    def get_scheme_eligibility(self, phone, lang):
        if lang == 'en':
            return "Please select your land acreage. Press 1 for 1 to 5 acres, or press 2 for more than 5 acres."
        return "ದಯವಿಟ್ಟು ನಿಮ್ಮ ಜಮೀನಿನ ವಿಸ್ತೀರ್ಣವನ್ನು ಆಯ್ಕೆ ಮಾಡಿ. 1 ರಿಂದ 5 ಎಕರೆಗಾಗಿ 1 ಒತ್ತಿ, ಅಥವಾ 5 ಎಕರೆಗಿಂತ ಹೆಚ್ಚಿದ್ದರೆ 2 ಒತ್ತಿ."

    def get_scheme_details(self, acreage_range, lang):
        schemes = {
            "small": {
                "name": "Kisan Samman Nidhi",
                "en": "You have selected for the Kisan Samman Nidhi scheme. If you agree to submit the application, press 1, or else press 2.",
                "kn": "ನೀವು ಕಿಸಾನ್ ಸಮ್ಮಾನ್ ನಿಧಿ ಯೋಜನೆಯನ್ನು ಆಯ್ಕೆ ಮಾಡಿದ್ದೀರಿ. ಅರ್ಜಿಯನ್ನು ಸಲ್ಲಿಸಲು ನೀವು ಒಪ್ಪಿದರೆ 1 ಒತ್ತಿ, ಇಲ್ಲದಿದ್ದರೆ 2 ಒತ್ತಿ."
            },
            "large": {
                "name": "PM-KUSUM (Solar Pump)",
                "en": "You have selected for the PM-KUSUM Solar Pump scheme. If you agree to submit the application, press 1, or else press 2.",
                "kn": "ನೀವು PM-KUSUM ಸೋಲಾರ್ ಪಂಪ್ ಯೋಜನೆಯನ್ನು ಆಯ್ಕೆ ಮಾಡಿದ್ದೀರಿ. ಅರ್ಜಿಯನ್ನು ಸಲ್ಲಿಸಲು ನೀವು ಒಪ್ಪಿದರೆ 1 ಒತ್ತಿ, ಇಲ್ಲದಿದ್ದರೆ 2 ಒತ್ತಿ."
            }
        }
        return schemes.get(acreage_range, {}).get(lang, "Scheme not found.")
