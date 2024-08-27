print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
        bill = 5
    elif age <= 18:
        print("Please pay $7.")
        bill = 7
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride with us!")
    else:
        print("Please pay $12.")
        bill = 12

    wants_photo = input("Do you want a photo? Y or N. ")
    if wants_photo == "Y":
        # Add $3 to their bill
        bill += 3
    print(f"Your finalbill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
