from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Этот эндпоинт нужен, чтобы Render не засыпал и видел, что сервер работает
@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    # Запуск для локального теста
    app.run(host='0.0.0.0', port=10000)