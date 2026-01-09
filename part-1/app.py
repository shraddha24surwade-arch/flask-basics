"""
Part 1: Hello Flask - Your First Web Server
============================================
How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask  # Import Flask class from the flask package

app = Flask(__name__)  # Create Flask app instance, __name__ tells Flask where to look for templates/static files


@app.route('/')  # Decorator that maps URL '/' (home page) to this function
def home():
    return "<h1>Hello Flask!</h1><p>This is HTML</p>"  # This text displays in the browser

@app.route('/user')
def user():
    return "<h1>Hello Shraddha!</h1>"

@app.route('/about')
def about():
    return "<h1>This is the about page</h1>"

if __name__ == '__main__':
    app.run(debug=True)  # debug=True enables auto-reload and detailed error messages
