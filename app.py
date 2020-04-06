import sys 
sys.path.append('./')
from flask import *
from AUTH import register,login

app = Flask(__name__)

app.add_url_rule('/register', view_func=register.register, methods=['POST'])
app.add_url_rule('/login',view_func=login.login, methods=['POST'])

if __name__== "__main__":
    app.run(debug = True,host='0.0.0.0')