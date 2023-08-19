name = input("Enter your name: ")
print("Hello!", name)
print("Here you can find out if you are eligible to vote or not.")
proceed = input("Do you want to proceed? (yes/no): ")

if proceed.lower() == "yes":
    print("Ok!")

    age = int(input("Enter your age: "))
    
    if age >= 18:
        print("You are Eligible to Vote.")
    else:
        print("You are not eligible to Vote.")
else:
    print("Some error occurred!")
