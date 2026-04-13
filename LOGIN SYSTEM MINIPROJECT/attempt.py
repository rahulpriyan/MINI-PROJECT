try:
    correct_pin = 1234
    attempts = 3

    while attempts > 0:
        # Taking input and converting to integer
        pin = int(input("Enter PIN: "))

        if pin == correct_pin:
            print("Access Granted")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong PIN. Attempts left: {attempts}")

    if attempts == 0:
        # Raising a specific exception when attempts run out
        raise Exception("Card Blocked: Too many incorrect attempts.")

except ValueError:
    # Handles cases where the user enters something that isn't a number
    print("Invalid input! Please enter a numeric PIN.")

except Exception as e:
    # Handles the "Card Blocked" exception we raised
    print(f"Security Alert: {e}")