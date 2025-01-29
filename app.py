from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Привет! Этот сайт создан на языке программирования Python!"

if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/menu')
def menu():
    return "Это меню, оно бесполезно."

@app.route('/test')
def test():
    return "Тестовая страница."