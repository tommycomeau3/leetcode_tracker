import database

def main():
    database.create_db()
    
    print("1. Add Problem")
    print("2. Delete Problem")
    print("3. Exit")
    
    using = True
    while using:
        choice = input("Choose an option: ")
        if choice == "1":
            problem_name = input("Problem Name: ")
            difficulty = input("Difficulty: ")
            category = input("Category: ")
            
            database.add_problem(
                problem_name,
                difficulty,
                category
            )
        elif choice == "3":
            using = False
        elif choice == "2":
            problem_name = input("Problem Name: ")
            database.delete_problem(problem_name)
        else:
            print("Invalid Input")
        

if __name__ == "__main__":
    main()