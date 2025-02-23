from flask import Flask, render_template
import requests

app = Flask(__name__)

# Головна сторінка
@app.route('/')
def home():
    return "Ласкаво просимо! Перейдіть на <a href='/httpbin'>сторінку httpbin</a>"

# Сторінка з вашим кодом з попереднього завдання
@app.route('/httpbin')
def show_httpbin():
    try:
        response = requests.get('https://httpbin.org/')
        # Перетворюємо бінарні дані у текст із правильною кодуванням
        content = response.content.decode('utf-8')  
        return render_template('index.html', data=content)
    except Exception as e:
        return f"Помилка: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)