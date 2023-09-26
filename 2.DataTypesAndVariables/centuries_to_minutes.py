# centuries = int(input())
# years = centuries * 100
# days = years * 365.242
# hours = days * 24
# minutes = hours * 60
#
# print(f"{centuries} centuries = {years:.0f} years = {days:.0f} days = {hours:.0f} hours = {minutes:.0f} minutes")

# Input the number of centuries from the user
centuries = int(input("Enter the number of centuries: "))
# Calculate the equivalent number of years
years = centuries * 100
# Calculate the equivalent number of days, hours, and minutes
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60

# Display the results
print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
