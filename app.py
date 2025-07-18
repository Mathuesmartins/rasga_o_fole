from flask import Flask, render_template, request, redirect, url_for

import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Porta fornecida pelo Render
    app.run(debug=False, host='0.0.0.0', port=port)