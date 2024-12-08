from flask import Flask, request, jsonify
import mysql.connector
import requests
app = Flask(__name__)

# MySQL connection details (replace with your credentials)
mydb = mysql.connector.connect(
  host="db",  # имя сервиса в docker-compose
  user="user",
  password="1234",
  database="notesdb"
)

    
@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        data = request.get_json()
        name = data['name']
        phone = data['phone']

        cursor = mydb.cursor()
        sql = "INSERT INTO registrations (name, phone) VALUES (%s, %s)"
        val = (name, phone)
        cursor.execute(sql, val)
        mydb.commit()

        return jsonify({'message': 'Data submitted successfully!'})

    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        if mydb.is_connected():
            mydb.close()
            
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)