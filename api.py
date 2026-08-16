from flask import Flask, request
import database
from flask_restful import Resource, Api, fields, reqparse, marshal_with, abort

app = Flask(__name__) 
api = Api(app)

user_args = reqparse.RequestParser()
user_args.add_argument('problem_name', type=str, required = True, help = "Problem name cannot be blank")
user_args.add_argument('difficulty', type=str, required = True, help = "Difficulty cannot be blank")
user_args.add_argument('category', type=str, required = True, help = "Category cannot be blank")

userFields = {
    'problem_name':fields.String,
    'difficulty':fields.String,
    'category':fields.String
}

class Problems(Resource):
    def get(self):
        problems = database.get_problems()
        return problems
    
    def post(self):
        data = request.get_json()

        database.add_problem(
            data["problem_name"],
            data["difficulty"],
            data["category"]
        )

        return {"message": "Problem added"}, 201

api.add_resource(Problems, '/api/problems/')
api.add_resource(Problems, "/api/problems/")

@app.get("/")
def home():
    return {"message": "API is running"}

if __name__ == "__main__":
    app.run(debug=True)