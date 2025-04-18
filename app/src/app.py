# from flask import Flask, jsonify
# import mysql.connector
# import os

# app = Flask(__name__)

# @app.route('/health')
# def health():
#     return jsonify({"status": "healthy"}), 200

# @app.route('/data')
# def data():
#     try:
#         # Test de connexion simplifié
#         conn = mysql.connector.connect(
#             host='mysql',
#             port=3306,
#             user='myuser',
#             password='mypassword',
#             database='test_db'
#         )
#         print("hello")
#         # Si la connexion réussit, renvoyer un message de succès
#         return jsonify({"status": "Connection successful"}), 200
#     except Exception as e:
#         # Afficher les détails complets de l'erreur
#         import traceback
#         error_details = traceback.format_exc()
#         return jsonify({"error": str(e), "details": error_details}), 500
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=4743)
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
            host='mysql',
            port=3306,
            user='myuser',
            password='mypassword',
            database='test_db'
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