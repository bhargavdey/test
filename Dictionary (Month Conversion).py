monthConversions = {
    #key : value
    "Jan": "January",#a key can also be a unique number
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May"
}#use {} for dictionary

print(monthConversions["Mar"])
print(monthConversions.get("Feb", "Not a valid key."))
print(monthConversions.get("jan", "Not a valid key."))
print(monthConversions.get("Mar"))
#two ways to call a value from a dictionary.
#use .get to return a default statement.