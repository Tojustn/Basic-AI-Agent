from flask import Blueprint, request, jsonify, json
from ..ollama_chat import chat_response

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat", methods = ["POST"])
def chat():
    data = request.json

    #Get the user message if nothing is in the message payload defaults to ""
    message = data.get("message", "")

    response = chat_response(message)
    return jsonify({"response":response})