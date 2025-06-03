class AikidoAI:
    def __init__(self):
        self.values = {
            "respect": "Maintain balance and understanding in all interactions.",
            "integrity": "Ensure fairness, honesty, and personal responsibility.",
            "control": "Prioritize non-reactive responses and good judgment.",
            "harmony": "Seek resolution rather than escalation in conflicts.",
            "clarity": "Aim for transparency and thoughtful reasoning.",
            "peace": "Guide interactions toward peaceful outcomes.",
            "cooperation": "Encourage collaboration and mutual problem-solving.",
            "self-discipline": "Commit to ethical behavior and mindful decision-making."
        }

    def classify_situation(self, user_input):
        """Classifies user input into ethical guidance, conflict resolution, or personal development."""
        user_input = user_input.lower()
        if any(word in user_input for word in ["conflict", "argument", "disagreement"]):
            return "conflict_resolution"
        elif any(word in user_input for word in ["ethical", "ai", "morals", "justice"]):
            return "ethical_guidance"
        elif any(word in user_input for word in ["self-improvement", "growth", "focus"]):
            return "personal_development"
        else:
            return "general_guidance"

    def generate_response(self, situation):
        """Determines AI's response based on Aikido principles."""
        if situation == "conflict_resolution":
            return f"{self.values['harmony']} {self.values['respect']} Instead of reacting, consider redirecting the conversation toward mutual understanding."
        elif situation == "ethical_guidance":
            return f"{self.values['integrity']} {self.values['clarity']} Ethical AI must reason through fairness rather than follow rigid rules."
        elif situation == "personal_development":
            return f"{self.values['self-discipline']} {self.values['control']} Growth comes from mastering one's own reactions before guiding others."
        else:
            return "Let’s explore this together. Balance and adaptability are key in every challenge."

# Example usage:
ai_bot = AikidoAI()
user_input = input("You: ")
situation = ai_bot.classify_situation(user_input)
response = ai_bot.generate_response(situation)
print("Aikido AI Buddy:", response)