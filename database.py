import sqlite3

def create_db():
    connection  = sqlite3.connect('leetcode.db')

    cursor = connection.cursor()

    command1 = """ CREATE TABLE IF NOT EXISTS problems (
        id INTEGER PRIMARY KEY,
        problem_name TEXT NOT NULL,
        category TEXT NOT NULL,
        difficulty TEXT NOT NULL, 
        date_solved DATETIME DEFAULT CURRENT_TIME
    )"""

    cursor.execute(command1)

    connection.commit()
    connection.close()
    
def add_problem(problem_name, category, difficulty):
    connection  = sqlite3.connect('leetcode.db')
    cursor = connection.cursor()
    
    command = """ 
    INSERT INTO problems (problem_name, difficulty, category)
    VALUES (?, ?, ?)
    """
    
    cursor.execute(command, (problem_name, difficulty, category))
    
    connection.commit()
    connection.close()
    