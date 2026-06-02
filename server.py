from flask import Flask, request, jsonify

app = Flask(__name__)

# Главная страница
@app.route('/')
def home():
    return "Сервер работает!"

# Пример API-эндпоинта
@app.route('/api/data', methods=['GET'])
def get_data():
    sample_data = {"message": "Привет, мир!", "status": "ok"}
    return jsonify(sample_data)

# Пример POST-запроса
@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify({"you_sent": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
