from flask import Flask
import database
from flask_restful import Resource, Api, reqparse
from datetime import datetime


app = Flask(__name__) 
api = Api(app)

def validate_difficulty(value):
    allowed = ["Easy", "Medium", "Hard"]

    if value not in allowed:
        raise ValueError("Difficulty must be Easy, Medium, or Hard")

    return value

problems_args = reqparse.RequestParser()
problems_args.add_argument('problem_name', type=str, required = True, help = "Problem name cannot be blank")
problems_args.add_argument('difficulty', type=validate_difficulty, required = True, help = "Difficulty must be Easy, Medium, or Hard")
problems_args.add_argument('category', type=str, required = True, help = "Category cannot be blank")

class Problems(Resource):
    def get(self):
        problems = database.get_problems()
        
        for problem in problems:
            problem["date_solved"] = datetime.strptime(
                problem["date_solved"],
                "%Y-%m-%d %H:%M:%S"
            ).strftime("%b %d, %Y at %I:%M %p")
        
        return problems
    
    def post(self):
        data = problems_args.parse_args()

        database.add_problem(
            data["problem_name"],
            data["difficulty"],
            data["category"]
        )
        
        return {"message": "Problem added"}, 201 

update_args = reqparse.RequestParser()
update_args.add_argument("difficulty", type=validate_difficulty)
update_args.add_argument("category", type=str)

class Problem(Resource):
    def delete(self, problem_name):

        deleted = database.delete_problem(problem_name)
        
        if not deleted:
            return {"message": "Problem not found"}, 404

        return {"message": "Problem deleted"}, 200

    def get(self, problem_name):
        problem = database.get_problem(problem_name)
        if problem is None:
            return {"message": "Problem not found"}, 404
        problem["date_solved"] = datetime.strptime(
            problem["date_solved"],
            "%Y-%m-%d %H:%M:%S"
        ).strftime("%b %d, %Y at %I:%M %p")
        return problem
    
    def patch(self, problem_name):
        data = update_args.parse_args()
        
        if data["difficulty"] is None and data["category"] is None:
            return {"message": "No update fields provided"}, 400
        
        updated = database.update_problem(
            problem_name,
            data["difficulty"],
            data["category"]
        )
        
        if not updated:
            return {"message": "Problem not found"}, 404
        return {"message": "Problem updated"}, 200
        

api.add_resource(Problems, '/api/problems/')
api.add_resource(Problem, '/api/problems/<string:problem_name>')

@app.get("/")
def home():
    return {"message": "API is running"}

if __name__ == "__main__":
    app.run(debug=True)