from flask import Flask, request, jsonify

app = Flask(__name__)

def process_command(command):
    # Replace this with your custom LLM processing logic.
    # For now, it simply echoes the command back.
    return f"You said: {command}"

@app.route('/llm', methods=['POST'])
def llm_webhook():
    data = request.get_json(force=True)
    
    if not data or 'command' not in data:
        return jsonify({"error": "No command provided"}), 400

    command = data['command']
    response_text = process_command(command)
    
    # Return the response as JSON
    return jsonify({"response": response_text})

if __name__ == '__main__':
    # Run the Flask app on all available IPs, port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
