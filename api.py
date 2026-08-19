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

update_args = reqparse.RequestParser()
update_args.add_argument("difficulty", type=str)
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
        return problem
    
    def patch(self, problem_name):
        data = update_args.parse_args()
        
        updated = database.update_problem(
            problem_name,
            data["difficulty"],
            data["category"]
        )
        
        if not updated:
            return {"message": "Problem not updated"}, 404
        return updated
        

api.add_resource(Problems, '/api/problems/')
api.add_resource(Problem, '/api/problems/<string:problem_name>')

@app.get("/")
def home():
    return {"message": "API is running"}

if __name__ == "__main__":
    app.run(debug=True)