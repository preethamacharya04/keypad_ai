class AgricultureAgent:
    def __init__(self, ledger, brain):
        self.ledger = ledger
        self.brain = brain

    def get_market_intelligence(self, phone, lang):
        if lang == 'en':
            return "Here is the market intelligence report."
        return "ಇಲ್ಲಿ ಮಾರುಕಟ್ಟೆ ಬುದ್ಧಿಮತ್ತೆಯ ವರದಿ ಇದೆ."

    def process_pest_report(self, phone, lang):
        if lang == 'en':
            return "Press 1 for Yellow Leaves, 2 for Root Rot, 3 for Worms."
        return "ಹಳದಿ ಎಲೆಗಳಿಗಾಗಿ 1, ಬೇರು ಕೊಳೆತಕ್ಕಾಗಿ 2, ಹುಳುಗಳಿಗಾಗಿ 3 ಒತ್ತಿ."
        
    def record_and_check_pest(self, phone, village, issue, lang):
        self.ledger.report_issue(phone, village, issue)
        is_outbreak = self.ledger.check_outbreak(village, issue, limit=5)
        
        if is_outbreak:
            if lang == 'en':
                return f"Alert: 5 of your neighbors reported {issue} today. This is a spreading pest outbreak. Act within 24 hours. Press 1 to join the group to save costs on labor."
            else:
                # English word 'issue' is included here for simplicity in mock, ideally we'd translate the pest name too
                return f"ಎಚ್ಚರಿಕೆ: ನಿಮ್ಮ 5 ನೆರೆಹೊರೆಯವರು ಇಂದು {issue} ಬಗ್ಗೆ ವರದಿ ಮಾಡಿದ್ದಾರೆ. ಇದು ಹರಡುತ್ತಿರುವ ಕೀಟ ಪ್ರಕೋಪವಾಗಿದೆ. 24 ಗಂಟೆಗಳ ಒಳಗೆ ಕಾರ್ಯನಿರ್ವಹಿಸಿ. ಕಾರ್ಮಿಕರ ವೆಚ್ಚವನ್ನು ಉಳಿಸಲು ಗುಂಪಿಗೆ ಸೇರಲು 1 ಅನ್ನು ಒತ್ತಿ."
        else:
            prompt = f"The farmer in {village} is reporting a pest problem: {issue}. Give a direct, practical solution for {issue} in exactly 1 or 2 short sentences. Do not use more than 1.5 lines of text."
            language_str = "kannada" if lang == 'kn' else "english"
            
            response = self.brain.generate_response(user_input=prompt, language=language_str, context=f"Farmer in {village} with {issue}")
            return response

    def get_scheme_eligibility(self, phone, lang):
        if lang == 'en':
            return "You are eligible for the following schemes."
        return "ನೀವು ಈ ಕೆಳಗಿನ ಯೋಜನೆಗಳಿಗೆ ಅರ್ಹರಾಗಿದ್ದೀರಿ."
