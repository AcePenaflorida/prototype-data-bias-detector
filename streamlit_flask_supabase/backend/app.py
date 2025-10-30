from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_ANON_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
@app.route("/")
def home():
    return "Flask API is running. Try /users or /add_user."

@app.route("/users", methods=["GET"])
def get_users():
    response = supabase.table("users").select("*").execute()
    return jsonify(response.data)

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.json
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Name and email required"}), 400

    response = supabase.table("users").insert({"name": name, "email": email}).execute()
    return jsonify(response.data)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
