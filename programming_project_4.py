born=60/7*60*24*365
death=60/13*60*24*365
immi=60/35*60*24*365
pop=307357870
user=int(input("Enter a number of years to see estimated population in that number of years. "))
print(f"Current population is {pop} and in {user} years it will be {pop + born - death + immi * user :,.0f}.")
print( f"The abount of people born was {born * user :,.0f} and the amount that dies was {death * user :,.0f}. Lastly the amount of immigrants was {immi *user :,.0f}.")