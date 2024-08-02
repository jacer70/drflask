from flask import Flask, request, redirect, render_template
import random
import string

app = Flask(__name__)

# Base de datos simulada (diccionario)
url_mapping = {}

def generate_short_id(length=6):
    """Genera un ID corto aleatorio."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form['url']
        short_id = generate_short_id()
        url_mapping[short_id] = original_url
        return f'Short URL: <a href="/{short_id}">/{short_id}</a>'
    return render_template('index.html')

@app.route('/<short_id>')
def redirect_to_url(short_id):
    original_url = url_mapping.get(short_id)
    if original_url:
        return redirect(original_url)
    return 'URL not found', 404

if __name__ == '__main__':
    app.run(debug=True)
