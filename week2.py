grand_total = 0
no_of_sessions = 0
while True:
    while True:
        test_input = (input("What is your Test score: "))
        
        if not test_input.isdigit():
            print("Your Test score is invalid")
            continue
        test_score = int(test_input)
        if test_score > 30:
            print("Test score cannot be greater than 30")
        elif test_score < 0:
            print("Test score cannot be less than 0")
        
        else:
            break
        
    while True:
        ass_input = (input("What is your Assignment score: "))
        
        if not ass_input.isdigit():
            print("Your Assignment score is invalid")
            continue
        ass_score = int(ass_input)
        if ass_score > 10:
            print("Assignment score cannot be greater than 10")
        elif ass_score < 0:
            print("Assignment score cannot be less than 0")
        else:
            break
        
    while True:
        exam_input = (input("What is your Exam score: "))
        
        if not exam_input.isdigit():
            print("Your Exam score is invalid")
            continue
        exam_score = int(exam_input)
        if exam_score > 60:
            print("Exam score cannot be greater than 60")
        elif exam_score < 0:
            print("Exam score cannot be less than 0")
        else:
            break
            
    total_score = test_score + ass_score + exam_score
    grand_total += total_score
    no_of_sessions += 1
    print("no_of_sessions")
    print(f"Your total score is: {total_score}")
    
    if total_score >= 70:
        print("Your grade is A, You have an excellent result")
    elif total_score >= 60:
        print("Your grade is B, You have a very good result")
    elif total_score >= 50:
        print("Your grade is C, You have a good result")
    elif total_score >= 45:
        print("Your grade is D, Your result is fair")
    elif total_score >= 40:
        print("Your grade is E, You passed but your result is a bit low")
    else:
        print("Your grade is F, You have failed the assessment")
        
    if total_score >= 80:
        print("You are qualified for an award")
    else:
        print("--------------------------")
        
    next = input("Do you want to enter other scores? Yes/No: ").lower()
    if next == "yes" or next == "y":
        print(f"-------------------------")
    
    elif next == "no" or next == "n":
        print(f"The calculation is done, Overall total for all the sessions is {grand_total}")
        break
    else:
        print("Enter a valid input")
    
average = grand_total / no_of_sessions
percentage = (grand_total / 300) * 100
print(f"Your average score is {average} and your percentage score is {percentage}%")
    