import json
from datetime import datetime as dt, timedelta as td

with open("data/ranges.json") as fp:
    config = json.load(fp)

def convert_unix_to_hour_minute(timestamp):
    """ 
    Convertion function from unix time to human readable time in hours
    and minutes only.

    param: timestamp : time in unix format


    return: time in %H:%M format
    """
    try:
        resp = dt.utcfromtimestamp(timestamp).strftime('%H:%M')
    except:
        print("[Error] Error converting unit to hour_minute")
        resp = "00:00"
    return resp

def convert_unix_to_time(timestamp):
    """ 
    Convertion function from unix time to human readable complete timestamp

    param: timestamp : time in unix format


    return: time in %Y-%m-%d %H:%M:%S format
    """    
    try:
        resp = dt.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    except:
        print("[Error] Error converting unit to time")
        resp = "0000-00-00 00:00:00"
    return resp

def is_between(a, x, b):
    """ 
    Returns a bool which means if the x variable is inside de range
    [a,b] (borders included).

    param: a : left border fo range
    param: x : value to check if it's in between the range.
    param: b : right border fo range


    return: bool True if x between a and b, False if not.
    """  
    return min(a, b) <= x <= max(a, b)

def get_wind_speed_description(speed_m_s):
    """ 
    Returns a description for the wind speed

    param: speed_m_s : speed of wind value in meters/seconds

    return: String meaning description of wind speed
    """    
    for description,init_sp,end_sp in config["wind_speed"]:
        if is_between(float(init_sp),float(speed_m_s),float(end_sp)):
            return description
    else:
        return "Hard Hurricane"
        
def get_cardinal_name(cardinal):
    """ 
    Returns a de-parsed description for a cardinal name
    using a dictionary with the cardinal as key and 
    the de-parsed description as value.

    param: cardinal : string in normal cardinal format, ex: N for North.

    return: String of de-parsed cardinal name.
    """      
    return config["cardinal_names"][cardinal]

def get_cardinal_description(degrees):
    """ 
    Returns a description for the wind speed degree

    param: degrees : degrees of the wind speed

    return: String meaning description of wind speed degree
    """      
    cardinal=None
    for description,init_dg,end_dg in config["cardinal_direction"]:
        if is_between(init_dg,degrees,end_dg):
            cardinal=description
    if cardinal is not None:
        if len(cardinal)==1:
            return get_cardinal_name(cardinal)
        elif len(cardinal)==2:
            return f"{get_cardinal_name(cardinal[0])}{get_cardinal_name(cardinal[1])}"
        else:
            return f"{get_cardinal_name(cardinal[0])}-{get_cardinal_name(cardinal[1])}{get_cardinal_name(cardinal[2])}"
    else:
        return "wrong degrees adquired."

def get_cloudiness_name(percentage):
    """ 
    Returns a description for the cloudiness

    param: percentage : percentage of cloud cover

    return: String meaning description of cloudiness percentage.
    """      
    for description, init_range,end_range in config["cloudiness_names"]:
        if is_between(init_range,percentage,end_range):
            return description
    else:
        return "no range covered"
    