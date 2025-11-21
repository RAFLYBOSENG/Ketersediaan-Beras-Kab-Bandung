# app.py
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Pastikan file JSON sudah ada
    if not os.path.exists('static/data_simulasi_beras.json'):
        return "<h1>ERROR</h1><p>Jalankan simulasi terlebih dahulu untuk membuat file data.</p>", 500
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)