import os
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, send_from_directory
<<<<<<< HEAD
from jinja2 import Template
=======
import json
>>>>>>> 7feaa5ca56eba80397affba401b9a3b2329c27af

app = Flask(__name__)

@app.route('/')
def index():
<<<<<<< HEAD
    return render_template('pages/index.html')
=======
    f = open('copied_html/index.html', 'r')
    html = f.read()
    # result = requests.get('https://laulima.hawaii.edu/portal')
    soup = BeautifulSoup(html, 'lxml')
    return render_template('pages/index.html',
        nav=[[cell.text for cell in soup.find_all('li', 'nav-menu')] for row in soup]
    )
>>>>>>> 7feaa5ca56eba80397affba401b9a3b2329c27af

@app.route('/<path:path>')
def static_proxy(path):
  return app.send_static_file(path)

@app.route('/login')
def login():
    return render_template('pages/login.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
