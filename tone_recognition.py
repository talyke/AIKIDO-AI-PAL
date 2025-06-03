import textblob

def analyze_tone(user_input):
    """Evaluate emotional tone of user message."""
    sentiment = textblob.TextBlob(user_input).sentiment.polarity
    if sentiment > 0.5:
        return "positive"
    elif sentiment < -0.5:
        return "negative"
    else:
        return "neutral"

def emotional_response(user_input):
    """Shape AI response based on detected tone."""
    tone = analyze_tone(user_input)
    if tone == "positive":
        return r"You're approaching this with great energy! Keep that mindset."
    elif tone == "negative":
        return r"I hear your frustration. Let's find a way to turn this around."
    else:
        return r"Let's explore this thoughtfully."