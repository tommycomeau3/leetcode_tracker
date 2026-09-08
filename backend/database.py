from typing import Any


from ast import Dict
import sqlite3

def create_db():
    connection  = sqlite3.connect('leetcode.db')

    cursor = connection.cursor()

    command1 = """ CREATE TABLE IF NOT EXISTS problems (
        id INTEGER PRIMARY KEY,
        problem_name TEXT NOT NULL,
        category TEXT NOT NULL,
        difficulty TEXT NOT NULL, 
        date_solved DATETIME DEFAULT CURRENT_TIMESTAMP
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
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    
    command  = """
    SELECT * FROM problems
    """
    
    cursor.execute(command)
    
    problems = cursor.fetchall()
    
    connection.close()
    
    
    return [dict(problem) for problem in problems]

def get_problem(problem_name):
    connection = sqlite3.connect('leetcode.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    
    command = """
        SELECT * FROM problems
        WHERE problem_name = ?
        ORDER BY date_solved DESC
        LIMIT 1
    """
    
    cursor.execute(command, (problem_name,))
    
    problem = cursor.fetchone()
    
    connection.close()
    
    return dict(problem)

def update_problem(problem_name, difficulty=None, category=None):
    connection = sqlite3.connect('leetcode.db')
    cursor = connection.cursor()
    
    if difficulty is not None:
        cursor.execute(
            """
            UPDATE problems
            SET difficulty = ?
            WHERE problem_name = ?
            """,
            (difficulty, problem_name)
        )
    
    if category is not None:
        cursor.execute(
            """
            UPDATE problems
            SET category = ?
            WHERE problem_name = ?
            """,
            (category, problem_name)
        )
    
    updated = cursor.rowcount > 0
    connection.commit()
    connection.close()
    
    return updated