"""
TP1
Author: Guillaume TCHIKLADZE
"""

def isBissextile(year):
    """ return true if the year is bissextile."""
    return (year%4==0 and year%100!=0) or year%400==0 
        

def numberOfDay(month, year):
    """ take two variables (month, year) and return the number of day."""
    if not (0<month<=12):
        raise Exception("Mois non valide")
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    else:
        if isBissextile(year):
            return 29
        else:
            return 28

def isValidDate(date):
    """ take a "DD/MM/YYYY" return true if it's a valid date."""
    try:
        [day,month,year] = date.split('/')
        day=int(day)
        month=int(month)
        year=int(year)
        return 0<day<=numberOfDay(month, year)
    except Exception as error:
        print(error)
        return False
    


date = input('entrer une date (JJ/MM/AAAA) : ')
if isValidDate(date):
    print('date valide')
else:
    print('date non valide')
