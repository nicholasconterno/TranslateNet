from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import logging
import uuid
app = Flask(__name__)
# logging.getLogger().setLevel(logging.CRITICAL)
sessions = {}

@app.route('/')
def index():
    session_id = str(uuid.uuid4())
    return render_template('index.html', session_id=session_id)

@app.route('/<session_id>/takecommand')
def takecommand(session_id):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said {query}\n")
        return query
    except Exception as e:
        print("say that again please.....")
        return "None"

@app.route('/<session_id>/getcommand', methods=['POST'])
def getcommand(session_id):
    query = takecommand(session_id)
    while (query == "None"):
        query = takecommand(session_id)
    return jsonify({'message': query})

@app.route('/<session_id>/send', methods=['POST'])
def send(session_id):
    message = request.form['message']
    if session_id not in sessions:
        sessions[session_id] = []
    sessions[session_id].append(message)
    return jsonify({'message': message})

@app.route('/<session_id>/get_messages')
def get_messages(session_id):
    if session_id not in sessions:
        sessions[session_id] = []
    return\
        jsonify({'messages': sessions[session_id]})

@app.route('/<session_id>/chat', methods=['POST'])
def chat(session_id):
    print(session_id)
    message = request.form['message']
    send(session_id)
    print('Received message:', message)
    with open(f'chat_log_{session_id}.txt', 'a') as f:
        f.write(message + '\n')

    return jsonify({'status': 'OK'})

if __name__ == '__main__':
    app.run(host='10.197.86.249', port=5001, debug=True)
