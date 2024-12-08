from flask import Flask, request, jsonify, make_response


app = Flask(__name__)

# Список пользователей (замените на что-то более безопасное в реальном приложении!)
users = {"user1": "pass1", "user2": "pass2"}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username in users and users[username] == password:
           response = make_response(jsonify({"token": "some_token"}))
           response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8082'
           response.headers['Access-Control-Allow-Methods'] = 'POST'
           response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
           return response
    else:
           response = make_response(jsonify({"error": "Invalid credentials"}))
           response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8082'
           response.headers['Access-Control-Allow-Methods'] = 'POST'
           response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
           return response, 401


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)