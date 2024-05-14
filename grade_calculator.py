def calculate_average_grade(): #This is a script that has a user input their name and grades in three subjects, finds their grade average, then outputs a name and averaged grade
    # Prompt the user for their name and store it in the student_name variable
    student_name = input("Student Name_")

    # Prompt the user for their scores in Math, Science, and English
    # Store the scores in the respective variables: math_score, science_score, english_score
    math_score = input("Math Score_")
    science_score = input("Science Score_")
    english_score = input("English Score_")

    # Calculate the average grade
    average_grade = (int(math_score)+int(science_score)+int(english_score))/3 #This line takes the user inputted scores, turns them to integers, sums them, then divides by 3
    
    # Return the student's name and their average grade
    return student_name, average_grade

if __name__ == '__main__':
    # Call the calculate_average_grade function
    student_name, average_grade = calculate_average_grade()

    # Print the student's name and their average grade
    print(f"{student_name},","Grade =",average_grade)