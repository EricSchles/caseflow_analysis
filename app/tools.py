from app.models import *
from datetime import datetime
import json
import scipy as sp
from scipy import stats
import math

"""
This set of tools represents the analysis portion of the application.  The goal of this tool is to create a way to determine what pieces of CaseFlow need to be attacked next.  
"""

def time_lapse_dates(dates):
    #returns list with deltas of the form: current_date - date_created
    current_date = datetime.now()
    time_elapsed = []
    for date in dates:
        time_elapsed.append((current_date - date).days)
    return time_elapsed

def generate_graph():
    pass

def process_dates():
    #replace this later
    dates = [elem.date_created for elem in Data.query.all()]
    time_elapsed = time_lapse_dates(dates)
    s = sp.array(time_elapsed)
    n,min_max,mean,var,skew,kurt = stats.describe(s)
    sorted_time_elapsed = time_elapsed[:]
    sorted_time_elapsed.sort()
    sorted_time_elapsed = ["Sorted Time Elapsed - Note: sorted order does not correspond to the table below"] + sorted_time_elapsed 
    data = zip(Data.query.all(),time_elapsed)
    time_elapsed = ["time elapsed"] + time_elapsed
    return data,sorted_time_elapsed, time_elapsed, kurt, skew, var, mean
