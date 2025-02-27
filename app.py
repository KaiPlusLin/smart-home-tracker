from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Smart Home Tracker!"

if __name__ == '__main__':
    app.run(debug=True)
