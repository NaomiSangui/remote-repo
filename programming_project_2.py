days=int(input("Enter number of days after 09/25/2009. "))
dist=days * 917784 + 16637000000
print(f"The Voyager 1 at a distance of {dist} miles, or {dist * 1.609344} kilometers, or {dist / 92955887} astronomical units from the sun {days} days after 09/25/2009.")
print(f"Round trip radio communication would take {(((dist * 1.609344) / 299792.458) / 3600) * 2} hours.")