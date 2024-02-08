bill = float(input("How much: "))
tip = int(input("What percentage would you like to tip (10, 12 , 15): "))
if(tip not in [10,12,15]):
    print("Wrong tip!")
    exit(1)
people = int(input("How many people: "))

total = (bill + ((tip / 100) * bill) ) / people

print(f"Each person should pay: {total}")
