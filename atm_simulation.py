def atm_simulation():
    balance = 100.0
    
    print("\nWelcome to the ATM!")

    while True:
        print(f"\nCurrent Balance: ${balance:.2f}")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        try:
            option = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        
        if option == 1:
            print(f"\nYour current balance is: ${balance:.2f}")
        elif option == 2:
            try:
                deposit_amount = float(input("Enter amount to deposit: "))
                if deposit_amount <= 0:
                    print("Deposit amount must be greater than zero.")
                else:
                    balance += deposit_amount
                    print(f"Deposit successful! Your new balance is: ${balance:.2f}")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif option == 3:
            try:
                withdraw_amount = float(input("Enter amount to withdraw: "))
                if withdraw_amount <= 0:
                    print("Withdrawal amount must be greater than zero.")
                elif withdraw_amount > balance:
                    print("Insufficient funds! Please try a smaller amount.")
                else:
                    balance -= withdraw_amount
                    print(f"Withdrawal successful! Your new balance is: ${balance:.2f}")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif option == 4:
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 4.")

atm_simulation()
