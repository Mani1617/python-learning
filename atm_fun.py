# 1.Withdraw
# 2.credit
balance = 0
balance=int(balance)
# amount=input("Enter the amount : ")
# amount=int(amount)
def credit():
   global balance
   amount = float(input("Enter amount to credit: "))
   if amount <= 0:
     print("Please enter a positive amount.")
   else:
        balance += amount
        print(f"${amount} credited to your account.")
        return balance
def debit():
   global balance
   amount = float(input("Enter amount to debit: "))
   if amount <= 0:
     print("Please enter a positive amount.")
   elif amount>balance:
      print("Insufficient Funds.")
   else:
        balance -= amount
        print(f"${amount} Debited from your account.")
        return balance
   
def Show_balance():
    print(f"Your current balance is: ${balance}")
    return balance
def Exit():
    print("Thank you for using the ATM. Goodbye!")
    return 0

while True:
    print("\nATM Menu:")
    print("1. Credit")
    print("2. Debit")
    print("3. Balance")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
     credit()
     print(f"Account balance is : {balance}")
    elif choice=='2':
       debit()
       print(f"Account balance is : {balance}")
    elif choice=='3':
       Show_balance()
    elif choice=='4':
       Exit()
       break
    else:
       print("Invalid choice. Please try again.")
       



   
