import re

def isPassportValid(passportString):
    neededPassportFields = [
        "byr",  # Birth Year
        "iyr",  # Issue Year
        "eyr",  # Expiration Year
        "hgt",  # Height
        "hcl",  # Hair Color
        "ecl",  # Eye Color
        "pid",  # Passport ID
        # "cid",  # Country ID
    ]
    
    eyeColors = [
        "amb",
        "blu",
        "brn",
        "gry",
        "grn",
        "hzl",
        "oth",
    ]
    
    parsedFields = {}
    for passportField in passportString.split():
        key, value = passportField.split(':')
        parsedFields[key] = value
    
    for neededField in neededPassportFields:
        if neededField not in parsedFields.keys():
            return False
        
        field = parsedFields[neededField]
        
        if neededField == "byr":
            intField = int(field)
            if intField < 1920 or 2002 < intField:
                return False
        
        elif neededField == "iyr":
            intField = int(field)
            if intField < 2010 or 2020 < intField:
                return False
        
        elif neededField == "eyr":
            intField = int(field)
            if intField < 2020 or 2030 < intField:
                return False
        
        elif neededField == "hgt":
            if field[-2:] == "cm":
                height = int(field[:-2])
                if height < 150 or 193 < height:
                    return False
            elif field[-2:] == "in":
                height = int(field[:-2])
                if height < 59 or 76 < height:
                    return False
            else:
                return False
        
        elif neededField == "hcl":
            if not re.match('^#[a-f0-9]{6}$', field):
                return False
        
        elif neededField == "ecl":
            if field not in eyeColors:
                return False
        
        elif neededField == "pid":
            if not re.match('^\d{9}$', field):
                return False
        else:
            return False
    
    return True

f = open('input.txt', 'r')
input = f.read()

passports = input.split("\n\n")

validPassports = 0
for passport in passports:
    if isPassportValid(passport):
        validPassports += 1

print(validPassports)
