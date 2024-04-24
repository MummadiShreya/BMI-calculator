while True:
    ret=False
 
    print("\n\n================= BMI Calculator  =================\n\n")


    height = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))

    BMI = weight / (height/100)**2

    print(f"You BMI is {BMI}")

    if BMI <= 18.4:
        print("You are underweight.")
    elif BMI <= 24.9:
        print("You are healthy.")
    elif BMI <= 29.9:
        print("You are over weight.")
    elif BMI <= 34.9:
        print("You are severely over weight.")
    elif BMI <= 39.9:
        print("You are obese.")
    else:
        print("You are severely obese.")

    user_input=input("\n\nTry again? (Yes/No): ")
    print("\n\n")
    if user_input.lower()=='no':
        print("Exit program.")
        break
 
    elif user_input.lower()=='yes':
        ret=True
 
    else:
        print("Wrong input.")
        ret=True
 
 
    if ret:
        continue
