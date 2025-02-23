from flask import Flask, render_template
import requests

app = Flask(__name__)

# Отримуємо список епізодів через Jikan API v4
ANIME_ID = 54595  # Тут можеш змінити ID на будь-яке аніме
API_URL = f"https://api.jikan.moe/v4/anime/{ANIME_ID}/episodes"

response = requests.get(API_URL)
j = response.json()  # Отримуємо JSON-відповідь

@app.route('/')
def home():
    a = str()
    if "data" in j:
        for episode in j["data"]: 
            a += f"<p>Епізод {episode['mal_id']} з назвою: {episode['title']} має оцінку {episode.get('score', 'Немає оцінки')}<p>"
    else:
        a = "<p>Помилка: не вдалося отримати список епізодів.</p>"
    return a

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
