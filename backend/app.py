from flask import Flask, render_template, request, redirect, url_for
import json
import requests

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")

# Установите свой секретный ключ reCAPTCHA здесь
RECAPTCHA_SECRET_KEY = '6LdMZc0pAAAAAIEOcpg0ss7gUWVreX-dp28pnqSu'


# Функция для сохранения данных в JSON файл
def save_feedback(username, email, message):
    feedback_data = {'username': username, 'email': email, 'message': message}
    with open('feedback.json', 'a', encoding='utf-8') as f:
        json.dump(feedback_data, f, ensure_ascii=False)
        f.write('\n')


@app.route('/')
def index():
    return render_template('index.html', title='TravelVista')


@app.route('/countries')
def countries():
    return render_template('countries.html')


@app.route('/china')
def china():
    return render_template('china.html')


@app.route('/feedback')
def feedback():
    return render_template('feedback.html', title='Обратная связь')


@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        message = request.form['message']

        # Проверяем reCAPTCHA
        recaptcha_response = request.form['g-recaptcha-response']
        is_human = verify_recaptcha(recaptcha_response)

        if is_human:
            # Сохранение данных в JSON файл
            save_feedback(username, email, message)
            return redirect(url_for('index'))  # Перенаправляем пользователя на главную страницу
        else:
            return 'reCAPTCHA не пройдена'
    else:
        return 'Method not allowed'


def verify_recaptcha(recaptcha_response):
    data = {
        'secret': RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
    }
    response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
    result = response.json()
    return result['success']


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
