import json
import hashlib
import hmac
from flask import Flask, request, jsonify

# Webhook signing secret (replace with actual secret)
SIGNING_SECRET = "your_webhook_secret"

app = Flask(__name__)

def verify_signature(request_body, signature_header):
    """Verify Copilot webhook signature to ensure authenticity."""
    computed_signature = hmac.new(
        SIGNING_SECRET.encode(), request_body, hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(computed_signature, signature_header)

def analyze_response(ai_response):
    """Analyze AI response for excessive agreement or lack of depth."""
    if "you're right" in ai_response.lower() or "absolutely" in ai_response.lower():
        return "I see your point, but have you considered another perspective?"
    return ai_response  # If balanced, keep original response

@app.route('/copilot_webhook', methods=['POST'])
def webhook_handler():
    """Handle incoming Copilot AI responses via webhook."""
    raw_body = request.data
    signature = request.headers.get('X-COPILOT-SIGNATURE')

    # Validate webhook signature
    if not verify_signature(raw_body, signature):
        return jsonify({"error": "Invalid signature"}), 403

    data = json.loads(raw_body)
    ai_response = data.get("data", {}).get("ai_response", "")

    # Process and refine AI response
    refined_response = analyze_response(ai_response)

    return jsonify({"refined_response": refined_response}), 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)