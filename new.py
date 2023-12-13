from flask import Flask, jsonify, request
import mysql.connector
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)





def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='touhid',
        password='MyN3wP4ssw0rd',
        database='trivia_game'
    )
    return connection

# Fetch trivia questions from the database
@app.route('/get-questions', methods=['GET'])
def get_questions():
    level = request.args.get('level', default=1, type=int)
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    if level == 1:
        cursor.execute("SELECT * FROM questions")
    else:

        pass

    questions = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(questions)

# Roll dice endpoint
@app.route('/roll-dice', methods=['GET'])
def roll_dice():
    return jsonify({"dice_result": random.randint(1, 6)})

if __name__ == '__main__':
    app.run(debug=True)
