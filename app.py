from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Respuestas predefinidas del chatbot
responses = {
    "default": "Lo siento, no entiendo tu pregunta. ¿Podrías reformularla?",
    "saludos": "Hola, soy un chatbot diseñado para ayudarte con denuncias de violencia política de género. ¿En qué puedo ayudarte?",
    "denuncia": "Para realizar una denuncia formal, necesitaré algunos detalles. ¿Podrías describir la situación que deseas denunciar?",
    "ayuda": "Puedo ayudarte a: \n1. Realizar una denuncia\n2. Informarte sobre tus derechos\n3. Conectarte con autoridades competentes",
    "derechos": "Tienes derecho a participar en la política libre de violencia. Esto incluye estar libre de discriminación, acoso y cualquier forma de violencia basada en género."
}

def get_response(message):
    message = message.lower()
    
    if any(word in message for word in ['hola', 'buenos días', 'buenas']):
        return responses["saludos"]
    elif any(word in message for word in ['denuncia', 'denunciar', 'reportar']):
        return responses["denuncia"]
    elif any(word in message for word in ['ayuda', 'ayudar', 'apoyo']):
        return responses["ayuda"]
    elif any(word in message for word in ['derechos', 'derecho']):
        return responses["derechos"]
    else:
        return responses["default"]

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    response = get_response(message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)