from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1/hello'
app.config['QLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    password = db.Column(db.String(40))
    info = db.Column(db.String(128))

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'info': self.info,
        }

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users')
def hello_users():
    users = User.query.all()
    users = [user.to_json() for user in users]
    return jsonify(users)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port='10086', debug=True)