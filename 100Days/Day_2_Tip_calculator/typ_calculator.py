

print("Welcome to the tip calculator.")
total = input("What was the total bill? $")
how_many_ppl = input("How many people to split the bill? ")
percentage_tip = input("What percentage tip would you like to give? 10,12, or 15? ")

print(f"Each person should pay: ${round(((float(total)+(float(total)*int(percentage_tip)*0.01))/int(how_many_ppl)),1)}")