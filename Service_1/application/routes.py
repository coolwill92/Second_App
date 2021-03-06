from application import app
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import environ
import requests
import random

app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \
                                        environ.get('MYSQL_USER') + \
                                        ':' + \
                                        environ.get('MYSQL_PASSWORD') + \
                                        '@' + \
                                        environ.get('MYSQL_HOST') + \
                                        ':' + \
                                        environ.get('MYSQL_PORT') + \
                                        '/' + \
                                        environ.get('MYSQL_DB_NAME')

db = SQLAlchemy(app)





class willdatabase(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    f_name = db.Column(db.String(50), nullable=False)
   
    def __repr__(self):
        return ''.join(
        [
            'F_name: ' + self.f_name + '\n' 
            'ID: ' + str(self.id)
        ]
    )


@app.route('/', methods=['GET', 'POST'])
def home():
    response = requests.get('http://service_4:5003/randomword')
    print(response)
    sentence = response.text
    game_data = willdatabase.query.all()

    # print(randomword)
    # display = games.query.order_by(games.id.desc())
    name = willdatabase(
        f_name=sentence
    )
    db.session.add(name)
    db.session.commit()

    return render_template('index.html', sentence=sentence, willdatabase=game_data, title='Home')
