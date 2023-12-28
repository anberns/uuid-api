from flask import Flask
import uuid

app = Flask(__name__)

@app.route('/')
def home():
    return "Healthy"

@app.route('/uuid')
def new_uuid():
    return str(uuid.uuid4())

if __name__ == '__main__':
    app.run(debug=True)
