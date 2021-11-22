from math import *
def haversine_distance(lat1, lon1, lat2, lon2):
    """Return the distance in km between two points around the Earth.

    Latitude and longitude for each point are given in degrees.
    """
    d = 2 * 6371 * sin(((sin((lat1 - lat2)/2))**2 + cos(lat1) * cos(lat2) * (sin((lon1 - lon2)/2))**2) **1/2)
    return d

def check_id(id_str):
    if len(id_str)==5 and id_str.isdigit():
        return True
    else:
        print('The unique ID should be comprised of exactly 5 digits, but this id is ', id_str)
        return False
def check_lat_value(value_str):
    try:
        num = float(value_str)
        if num<=90 and num >=-90:
            return True
        else:
            print('The latitude should be between -90 and 90, but this latitude is ',value_str)
            return False
    except:
        print('The latitude should be numeric, but this latitude is ',value_str)
        return False
def check_lon_value(value_str):
    try:
        num = float(value_str)
        if num<=180 and num >=-180:
            return True
        else:
            print('The longitude should be between -180 and 180, but this longitude is ',value_str)
            return False
    except:
        print('The longitude should be numeric, but this longitude is ',value_str)
        return False
def check_year(year_str):
    try:
        year = int(year_str)
        if year <=2021 and year >0:
            return True
        else:
            print('The year should not in the future or negative, but this year is ', year_str)
            return False
    except:
        print('The year should be numeric, and this year is ', year_str)
        return False
def check_unit(unit_str):
    if len(unit_str)==2 and (unit_str=='99' or (unit_str.isupper()and unit_str.isalpha())):
        return True
    else:
        print('The political unit is a string of length 2, composed only of capital letters or the special value 99, and this unit is ', unit_str)
        return False
def check_annual_value(value_str):
    try:
        num = float(value_str)
        if isinstance(num, float):
            return True
        else:
            print('The value for the mass-balance should be numeric, but this value is ', value_str)
            return False
    except:
        print('The value for the mass-balance should be numeric, but this value is ', value_str)
        return False
