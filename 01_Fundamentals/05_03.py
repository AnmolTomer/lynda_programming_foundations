def wash_car(num):
    if(num <= 6):
        print("Wash with white foam\nRinse Once\nAir Dry\n-------")
    elif(num <= 12):
        print("Wash with tri-color foam\nRinse twice\nDry with large blow dryers!\n-------")
    else:
        print("Enter amount!")


wash_car(6)

wash_car(12)
