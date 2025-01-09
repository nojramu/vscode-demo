def threshold_counter():
    current_value = 0
    try:
        # Get the threshold from the user
        threshold = int(input("Set the threshold value: "))
        
        while True:
            print(f"\nCurrent Value: {current_value}")
            print("[1] Add (+1)")
            print("[2] Reset")
            print("[3] Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                # Logical error: Should use <= instead of <
                if current_value < threshold:
                    current_value += 1
                    print("Value incremented.")
                else:
                    print("Value has reached the threshold.")
            elif choice == "2":
                current_value = 0
                print("Value has been reset.")
            elif choice == "3":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the threshold.")

# Run the program
threshold_counter()
