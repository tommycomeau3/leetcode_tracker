import sqlite3

def create_db(self):
    connection  = sqlite3.connect('leetcode.db')

    cursor = connection.cursor()

    command1 = """ CREATE TABLE problems (
        id INTEGER PRIMARY KEY,
        problem_name TEXT NOT NULL,
        category TEXT NOT NULL,
        difficult TEXT NOT NULL, 
        date_solved DATETIME DEFAULT CURRENT_TIME
    )"""

    cursor.execute(command1)

    connection.commit()
    connection.close()
    
# def add_problem(self, problem):
#     connection  = sqlite3.connect('leetcode.db')
#     cursor = connection.cursor()
    
#     add_problem = 
    
    