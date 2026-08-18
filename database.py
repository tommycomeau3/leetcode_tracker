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
    
def add_problem(problem_name, difficulty, category):
    connection  = sqlite3.connect('leetcode.db')
    cursor = connection.cursor()
    
    command = """ 
    INSERT INTO problems (problem_name, difficulty, category)
    VALUES (?, ?, ?)
    """
    
    cursor.execute(command, (problem_name, difficulty, category))
    
    connection.commit()
    connection.close()

def delete_problem(problem_name):
    connection = sqlite3.connect("leetcode.db")
    cursor = connection.cursor()
    
    command = """
    DELETE FROM problems
    WHERE id = (
        SELECT id
        FROM problems
        WHERE problem_name = ?
        ORDER BY date_solved DESC
        LIMIT 1
    )
    """
    
    cursor.execute(command, (problem_name,))
    deleted = cursor.rowcount > 0
    
    connection.commit()
    connection.close()
    
    return deleted

def get_problems():
    connection  = sqlite3.connect('leetcode.db')
    cursor = connection.cursor()
    
    command  = """
    SELECT * FROM problems
    """
    
    cursor.execute(command)
    
    problems = cursor.fetchall()
    
    connection.close()
    
    
    return problems