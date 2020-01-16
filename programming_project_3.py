gas=float(input("Enter the number of gallons of gas. "))
liter=gas * 3.78541
barrel=gas / 19.5
co2=gas * 20
ethanol=gas * 115000 / 75700
price=gas * 3
print(f"The amount entered in liters is {liter :.2f} and would fill {barrel :.2f} barrels.")
print(f"This amount of gas when burned would produce {co2 :.2f} pounds of CO2 and would contain as much energy as {ethanol :.2f} gallons of ethanol.")
print(f"The total cost of the gas would be ${price:.2f}")