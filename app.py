from flask import Flask, render_template, request
import os
from datetime import datetime

app = Flask(__name__)

# Глобальная переменная для хранения счетчика посещений
visit_count = 0

def initialize_counter():
    # Проверяем наличие файла и инициализируем счетчик из файла, если он существует
    global visit_count
    if os.path.exists('schet.txt'):
        with open('schet.txt', 'r') as file:
            contents = file.read()
            if contents.isdigit():
                visit_count = int(contents)
            else:
                visit_count = 0
    else:
        visit_count = 0

initialize_counter()

@app.route('/')
def index():
    global visit_count
    visit_count += 1
    with open('schet.txt', 'w') as file:
        file.write(str(visit_count))
    cur_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', visit_count=visit_count, ip_pos = request.remote_addr, time_now=cur_time, user_data = request.headers.get('User-Agent'))

@app.route('/reset')
def reset():
    global visit_count
    visit_count = 0
    with open('schet.txt', 'w') as file:
        file.write(str(visit_count))
    return render_template('reset.html')

if __name__ == '__main__':
    app.run(debug=True)
