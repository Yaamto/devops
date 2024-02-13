import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request

# Charger les variables d'environnement à partir du fichier .env lorsque nous ne sommes pas en mode production
if os.environ.get('ENV') != 'production':
    load_dotenv()

# Créer une app Flask
app = Flask(__name__)

# Echantillon de données pour travailler
tasks = [
    {
        'id': 1,
        'title': 'Faire des courses',
        'description': 'Lait, fromage, pizza, fruits',
        'done': False
    },
    {
        'id': 2,
        'title': 'Apprendre Python',
        'description': 'Apprendre les bases de la programmation Python',
        'done': False
    }
]


# Route "/health" (GET) Questionner le serveur
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': "Ok"})


# Route "/get" (GET) pour lister
@app.route('/get', methods=['GET'])
def get():
    # Recuperate les données de la BDD
    return jsonify({'status': "Ok", "iterator": tasks})


# Route "/add" (POST) pour ajouter
@app.route('/add', methods=['POST'])
def create_task():
    if not request.json:
        return jsonify({'error': 'JSON expected'}), 400
    interator = {
        'state': request.json['state'],
    }

    # BDD à faire pour créer
    return jsonify({'interator': interator}), 201


# Enfin, démarrer l'API
if __name__ == '__main__':
    if os.environ.get('ENV') == 'production':
        app.run()
else:
    app.run(host='0.0.0.0', port=8080, debug=True)
