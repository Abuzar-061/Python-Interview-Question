from flask import Flask, jsonify
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r'/*': {"origins": '*'}})

@app.route('/show', methods=['GET'])
def show():
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="Interview",
            user="postgres",
            password="Passwords0"
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM send")
        rows = cur.fetchall()
        # Convert the rows into a list of dictionaries for better readability
        result = [{"id": row[0], "name": row[1]} for row in rows ]
        return jsonify(result)
        
    except psycopg2.Error as e:
        return jsonify({"error": str(e)})
    
if __name__ == "__main__":
    app.run(port=5000, debug=True)
