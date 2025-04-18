from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/data')
def data():
    cursor = None
    conn = None
    try:
        # Essayer de se connecter à MySQL avec les credentials spécifiés
        conn = mysql.connector.connect(
            host='mysql',  # Assurez-vous que ce nom est correct (nom du service MySQL dans Docker)
            port=3306,     # Le port exposé pour MySQL
            user='myuser',  # L'utilisateur défini dans la commande Docker
            password='mypassword',  # Le mot de passe pour 'myuser'
            database='test_db'  # La base de données que tu as créée
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM TpTable;")
        rows = cursor.fetchall()
        return jsonify(rows), 200
    except mysql.connector.Error as err:
        return jsonify({"error": f"MySQL error: {err}"}), 500
    except Exception as e:
        return jsonify({"error": f"Other error: {e}"}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4743)
