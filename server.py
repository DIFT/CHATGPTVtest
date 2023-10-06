from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/animation/start-talk', methods=['POST'])
def start_talk():
    print("Received request to start talking.")
    return "Start talk request received.", 200

@app.route('/animation/stop-talk', methods=['POST'])
def stop_talk():
    print("Received request to stop talking.")
    return "Stop talk request received.", 200

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form.get('message') # This line is changed

    if "talk" in message.lower():
        return jsonify({"action": "start_talk", "response": "Okay, I'll start talking!"})
    else:
        return jsonify({"action": "none", "response": "No animation trigger."})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
