from flask import Flask, request
import database
from flask_restful import Resource, Api, reqparse

app = Flask(__name__) 
api = Api(app)

problems_args = reqparse.RequestParser()
problems_args.add_argument('problem_name', type=str, required = True, help = "Problem name cannot be blank")
problems_args.add_argument('difficulty', type=str, required = True, help = "Difficulty cannot be blank")
problems_args.add_argument('category', type=str, required = True, help = "Category cannot be blank")

class Problems(Resource):
    def get(self):
        problems = database.get_problems()
        return problems
    
    def post(self):
        data = problems_args.parse_args()

        database.add_problem(
            data["problem_name"],
            data["difficulty"],
            data["category"]
        )

        return {"message": "Problem added"}, 201

class Problem(Resource):
    def delete(self, problem_name):
            
        database.delete_problem(problem_name)
            
        return {"message": "Problem deleted"}, 200


api.add_resource(Problems, '/api/problems/')
api.add_resource(Problem, '/api/problems/<string:problem_name>')

@app.get("/")
def home():
    return {"message": "API is running"}

if __name__ == "__main__":
    app.run(debug=True)