from flask import Flask

# Создаем экземпляр приложения Flask
app = Flask(__name__)

# Определяем маршрут для главной страницы
@app.route('/')
def index():
    return 'Hello from Effective Mobile!'

# Эта часть нужна, чтобы запустить сервер, когда мы запускаем файл напрямую
if __name__ == '__main__':
    # Важный момент: host='0.0.0.0' делает сервер видимым
    # за пределами контейнера.
    app.run(host='0.0.0.0', port=8080)