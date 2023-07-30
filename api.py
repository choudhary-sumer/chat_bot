''' chat system API '''
from flask import Flask, request, jsonify
from chat_system import generate_response


app = Flask(__name__)


@app.route('/chats', methods=['POST'])
def chat():
    ''' Initialize chat object '''
    user_ask = request.json['user_ask']
    response = generate_response(user_ask)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
    