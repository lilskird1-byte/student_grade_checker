print("===============STUDENT GRADE CHECKER============")
print()

print("Enter your scores here to check your progress.")
print()
#Subjects and scores data input

def student_grade_checker():
    name= str(input("What is your name? :"))
    print(f"Hello Dear {name}")
    print()
    math= int(input("Mathematics score:"))
    print()
    english= int(input("English score:"))
    print()
    science= int(input("Science score:"))
    print()
    total= math+ english+ science
    print(f"Total score= {total}")
    print()
    average= total/3
    print(f"Average score= {average}")
    print()
    if 80<= average <=89:
        print("Congrats! You had grade A")
        print("You are good to go!!!")
    elif 90<= average <=100:
        print("Excellent Student!!")
    elif 70<= average <=79:
        print("Well Done! You had grade B")
    elif 60<= average <=69:
        print("Good! You had grade C")
    elif 50<= average <=59:
        print("Sit Up!, You had grade D")
    else:
        print("You failed the results, learn harder!!!")
student_grade_checker()



















