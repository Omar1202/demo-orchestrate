from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
import os

# from dotenv import load_dotenv

# load_dotenv()

app = Flask(__name__)
CORS(app)

# Obtener variables de entorno
username = os.environ.get("MONGODB_USERNAME")
password = os.environ.get("MONGODB_PASS")

if not username or not password:
    raise EnvironmentError("Faltan MONGODB_USERNAME o MONGODB_PASS")

# Construir URI
MONGODB_URI = f"mongodb+srv://{username}:{password}@watsonxtest.6u16lup.mongodb.net/?retryWrites=true&w=majority&appName=WatsonxTest"

DB_NAME = "watsonxDemoDB"
COLLECTION_NAME = "Obras"

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]


@app.route("/obras", methods=["GET"])
def obtener_obras():
    try:
        result = [{**doc, "_id": str(doc["_id"])} for doc in collection.find()]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/obra/<id>", methods=["GET"])
def obtener_obra_por_nombre(id):
    try:
        doc = collection.find_one({"_id": ObjectId(id)})
        if not doc:
            return jsonify({"error": "Documento no encontrado"}), 404
        doc["_id"] = str(doc["_id"])
        return jsonify(doc)
    except Exception as e:
        return jsonify({"error": "ID inválido o error interno", "details": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)