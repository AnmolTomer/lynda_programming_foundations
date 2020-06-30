# Python returning values


def withdraw_money(current_bal, amount):
    if(current_bal >= amount):
        current_bal -= amount

        return current_bal


balance = withdraw_money(100, 20)

if (balance >= 50):
    print(f"The balance is {balance}.")
else:
    print("You need to make a deposit.")
