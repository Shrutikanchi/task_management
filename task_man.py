from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from dataclasses import dataclass 
from os import environ 

db=SQLAlchemy()

@dataclass
class task(db.model):
    _tablename_='USER'

    id=str
    username=str
    email=str

    id=db.Column(db.Integer, primary_key= True)
    username=db.Column(db.String(50),unique=True, null=False)
    email=db.Column(db.String(90),unique=True, null=False)

    def to_json():
        return{
            'id': self.id,
            'username': self.username,,
            'email': self.email
        }

def create_app():
    try:
        app=Flask(_name_)
        app.config['Databse_URL']= environ.get('DB_URL')
        db.init_app(app)

        with app.app_context():
            db.create_all()

        return app
    except Exception as e:
        print("error in creating in app")
        print(e)
        return False 

db.create_all()


@app.route("/")
def default_user():
    return("Welcome to the app")

def val_user(data):
    required_keys=["username","email"]
    for kkey in required_keys:
        if key not in data:
            return False
        return True

@app.route("/create/user", methods=['POST'])
def create():
    try:

        if not request.is_json:
            return jsonify({"error":"the request can't be validated"}),400

        body=request.json()
        if not val_user(body):
            return jsonify({"error":"request invalid"}),400


        new_user=task(username=body["username"], email=body["email"]
        db.session.add(new_user)
        db.session.commit()
        return jsonify("U_name": username, "mail": email, "sucess":"true")

    except Exception as e:
        print("error in creating user")
        print(e)
        return {"error": str(e)}


@app.route("/retrieve_users", methods=['POST'])
def retrieve_users():
    try:
        users=User.query.all()
        return jsonify([user.json() for user in users])

    except Exception as e:
        return{"error":str(e)}

@app.route("/retrieve_userID/<int:id>", methods=['POST'])
def retrieve_user(id):
    try:
        user= User.query.filter_by(id=id).first()
        if user:
            return jsonify({"user": user.to_json()})
        return jsonify({"message": "User not found"})
    except Exception as e:
        return jsonify({"message":'error getting user'})

@app.route("/update_task", methods=['POST'])
def update_task():
    try:
        user=User.query.filter_by(id=id).first()
        if user:
            body= request.json()
            user.username= body["username"]
            user.email=body["email"]
            db.session.commit()
            return jsonify({"message": "User updated successfully"})
        return jsonify({'message': "user not found"})

    except Exception as e:
        return jsonify({"message": "error updating user"})
        
@app.route("/delete_task", methods=['POST'])
def delete_task():
    try:
        user=User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({"message": "User deleted successfully"})
        return jsonify({"message":"user not found"})

    except Exception as e:
        return jsonify({"message": "error deleting user"})


    