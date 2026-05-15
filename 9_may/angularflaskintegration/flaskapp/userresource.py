from flask import Flask,request
from flask_restful import Api, Resource, reqparse, fields,marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///c:/users/admin/userresource.db"
CORS(app)
api=Api(app)
db=SQLAlchemy(app)

#dbmodel
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),nullable=False)
    email=db.Column(db.String(30),nullable=False,unique=True)

#resource fields for json serialization
user_fields={
    'id':fields.Integer,
    'name':fields.String,
    'email':fields.String
}

parser=reqparse.RequestParser()
parser.add_argument("name",type=str,required=True,help="Name is required")
parser.add_argument("email",type=str,required=True,help="Name is required")

class UserListResource(Resource):
    @marshal_with(user_fields)
    def get(self):
        return User.query.all()
    @marshal_with(user_fields)
    def post(self):
        args=parser.parse_args()
        new_user=User(name=args['name'],email=args['email'])
        db.session.add(new_user)
        db.session.commit()
        return new_user,201


class UserResource(Resource):
    @marshal_with(user_fields)
    def get(self,id):
        user=User.query.get_or_404(id)
        return user     
    
    @marshal_with(user_fields)
    def put(self,id):
        args=parser.parse_args()
        user=User.query.get(id)
        user.name=args["name"]
        user.email=args["email"]
        db.session.commit()
        return user     

    def delete(self,id):
        user=User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return '',204

api.add_resource(UserListResource,"/user")
api.add_resource(UserResource,"/user/<int:id>")
if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0',port=5000)   