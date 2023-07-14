monthConversion = {
    "Jan": "January",
    "Feb": "February ",
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
       0:"error"
}

print(monthConversion["Nov"])

print(monthConversion["Mar"])

print(monthConversion.get(0))
print(monthConversion.get("Luv","Not a valid key"))

