monthsConversion = {
    "jan":"January",
    "feb":"February",
    "mar": "March",
    "apr":"April",
    "jun": "June",
    "jul" :"July",
    "aug" : "August",
    "sep" : "September",
    "oct" : "October",
    "nov" :"November",
    "dec" :"december",

}
print(monthsConversion["dec"])
print(monthsConversion.get("nov"))    # another way
print(monthsConversion.get("luv","not a valid key"))

