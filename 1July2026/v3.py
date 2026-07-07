while True:
    age = input("Enter your age: ")
    print(f"You entered {age}")

    if age.isdigit():
        print("You entered right data")
        card_expiry_in_years = int(age) + 10
        print(f"Your card will expire when you're {card_expiry_in_years} years old")
        break
    else:
        print("You entered wrong data")

print("completed")

