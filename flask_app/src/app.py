from config import app_config
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'

if __name__ == '__main__':    
    app.run(host=app_config['HOST'],port=app_config['PORT'], debug=app_config['DEBUG'])
