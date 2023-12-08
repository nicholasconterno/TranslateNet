from flask import Flask, render_template, request, jsonify, redirect, url_for

import speech_recognition as sr
app = Flask(__name__)
# logging.getLogger().setLevel(logging.CRITICAL)
sessions = {}


@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Join a Room</title>
    <style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f5f5f5;
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
        margin: 0;
    }

    #join-form {
        background-color: white;
        padding: 30px;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    h1 {
        color: #2c3e50;
        margin-top: 0;
        margin-bottom: 20px;
    }

    label {
        display: block;
        margin-bottom: 5px;
    }

    input[type="text"] {
        padding: 6px;
        border-radius: 3px;
        border: 1px solid #ccc;
        display: block;
        width: 100%;
        margin-bottom: 10px;
    }

    button {
        padding: 6px 10px;
        background-color: #2c3e50;
        color: white;
        border: none;
        border-radius: 3px;
        cursor: pointer;
    }

    button:hover {
        background-color: #1a2533;
    }
</style>

</head>
<body>
    <div id="join-form">
        <h1>Join a Room</h1>
        <form action="/join" method="post">
            <label for="room_name">Enter room name:</label>
            <input type="text" id="room_name" name="room_name" required>
            <button type="submit">Join</button>
        </form>
    </div>
</body>
</html>

    '''


@app.route('/join', methods=['POST'])
def join():
    room_name = request.form['room_name']
    return redirect(url_for('index', room_name=room_name))


@app.route('/<room_name>')
def index(room_name):
    return render_template('index.html', room_name=room_name)


@app.route('/<session_id>/takecommand')
def takecommand(session_id):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said {query}\n")
        return query
    except Exception as e:
        print("say that again please....."+str(e))
        return "None"


@app.route('/<session_id>/getcommand', methods=['POST'])
def getcommand(session_id):
    query = takecommand(session_id)
    while (query == "None"):
        query = takecommand(session_id)
    return jsonify({'message': query})


@app.route('/<session_id>/send', methods=['POST'])
def send(session_id, message, username, input_language):
    message_with_username = f"{username}: {message}"
    message_data = {"message": message_with_username,
                    "input_language": input_language}
    if session_id not in sessions:
        sessions[session_id] = []
    sessions[session_id].append(message_data)
    return jsonify({'message': message_with_username})


@app.route('/<session_id>/get_messages')
def get_messages(session_id):
    if session_id not in sessions:
        sessions[session_id] = []
    return jsonify({'messages': sessions[session_id]})


@app.route('/<session_id>/chat', methods=['POST'])
def chat(session_id):
    print(session_id)
    message = request.form['message']
    username = request.form['username']
    input_language = request.form['input_language']
    send(session_id, message, username, input_language)
    print('Received message:', message)
    with open(f'chat_log_{session_id}.txt', 'a') as f:
        f.write(username + ': ' + message + '\n')
    return jsonify({'status': 'OK'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
