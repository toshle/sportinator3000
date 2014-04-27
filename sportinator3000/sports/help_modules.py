import math

def distance_between_points(latitude1, longitude1, latitude2, longitude2):
    degrees_to_radians = math.pi/180.0
    phi1 = (90.0 - latitude1)*degrees_to_radians
    phi2 = (90.0 - latitude2)*degrees_to_radians
    theta1 = longitude1*degrees_to_radians
    theta2 = longitude2*degrees_to_radians
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) +
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos(cos)
    return arc*6373

def filter_by_sport(data, sport_name):
    return data.filter(activity__sport__id=sport_name)

def filter_by_duration(data, duration):
    return data.filter(activity__duration__lte=duration)

def filter_by_price(data, price):
    return data.filter(activity__price__lte=price)

def filter_all(data, sport_name, duration, price):
    result = data

    if sport_name != None:
        result = filter_by_sport(result, sport_name)

    if duration != None:
        result = filter_by_duration(result, duration)

    if price != None:
        result = filter_by_price(result, price)

    return result