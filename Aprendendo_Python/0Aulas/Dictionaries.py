############# Dictionaries #############

MonthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
    
Week_day = {
    0: "Domingo",
    1: "Segunda",
    2: "Terca",
    3: "Quarta",
    4: "Quinta",
    5: "sexta",
    7: "Sabado"
}


print(MonthConversion["Feb"])
print(MonthConversion.get("Jul"))
print(MonthConversion.get("Luv", "Not a valid Key"))

print(Week_day[3])
print(Week_day.get(2))
print(Week_day.get(9, "Not a valid Key"))








