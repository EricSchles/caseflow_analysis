from app.models import *
from datetime import datetime
import json
import scipy as sp
from scipy import stats
import math

"""
This set of tools represents the analysis portion of the application.  The goal of this tool is to create a way to determine what pieces of CaseFlow need to be attacked next.  

We want to tell two stories - the case level story and the system level story.  This means being able to tell information about the system at a high level as well as figuring out how each case moves through the system.

Also, note that this is only how long a case has sat in the queue per department, not how long it took to complete.  To get a realistic sense of actual productivity challeneges, the size per department and average productivity per worker will be needed.
"""


def time_lapse_dates(dates):
    #returns list with deltas of the form: current_date - date_created
    current_date = datetime.now()
    time_elapsed = []
    for date in dates:
        time_elapsed.append((current_date - date).days)
    return time_elapsed

def get_by_id(id):
    nodes = {}
    nodes["id"] = id
    nodes["a"] = A.query.filter_by(case_id=id)
    nodes["b"] = B.query.filter_by(case_id=id)
    nodes["c"] = C.query.filter_by(case_id=id)
    nodes["d"] = D.query.filter_by(case_id=id)
    return nodes


def is_complete(end):
    #if end date is later than current date that means case is ongoing
    diff = datetime.now() - end  
    if diff.days < 0:
        return False
    else:
        return True

def process_node(node):
    #To do carry out the same analysis as is done in process_case at the node level
    pass

def process_system():
    #To do carry out the same analysis as is done in the process_case at the system level
    pass

def process_case(id):
    keys = ["a","b","c","d"]
    
    #Task level information
    total_tasks = 0
    completed_tasks = 0
    completed_tasks_per_node = {}.fromkeys(keys,0)
    total_tasks_per_node = {}.fromkeys(keys,0)
    ave_tasks_per_node = {}.fromkeys(keys,0)
    std_dev_tasks_per_node = {}.fromkeys(keys,0)
    skew_tasks_per_node = {}.fromkeys(keys,0)
    kurt_tasks_per_node = {}.fromkeys(keys,0)
    
    #To Do
    """
    The issue is we need to calculate this based on a 40 hour work week.  However, that still may not be accurate because of over time.
    So really it should be a range from 40 hours - 84 hours (12 hour day 7 days per week).  Perhaps I'll make this a sliding scale allowing a manager
    to add in overtime hour estimates?  
    In any event, total hours needs to be calculated
    
    Add below metrics once calculation can be completed
    """
    
    #Hours spent per task
    total_hours_per_node = {}.fromkeys(keys,0)
    ave_task_hours_per_node = {}.fromkeys(keys,0)
    std_dev_task_hours_per_node = {}.fromkeys(keys,0)
    skew_task_hours_per_node = {}.fromkeys(keys,0)
    kurt_task_hours_per_node = {}.fromkeys(keys,0)

    #Days spent per task
    total_days_per_node = {}.fromkeys(keys,0)
    ave_task_days_per_node = {}.fromkeys(keys,0)
    std_dev_task_days_per_node = {}.fromkeys(keys,0)
    skew_task_days_per_node = {}.fromkeys(keys,0)
    kurt_task_days_per_node = {}.fromkeys(keys,0)
    
    nodes = get_by_id(id)
    for key in keys:
        for elem in nodes[key]:
            total_tasks += 1
            total_tasks_per_node[key] += 1
            if is_complete(elem.date_completed):
                completed_tasks += 1
                completed_tasks_per_node[key] += 1
            
def rank_cases():
    #To do based on the information calculated, rank cases by average hours spent, variance in time spent, by total time spent, by number of tasks completed,
    #by total number of nodes traversed, by number of nodes traversed over time - if case goes between  A <-> B quickly but A <-> C slowly, then this must be documented
    #and accounted for (for example)
    pass
    
def rank_nodes():
    #To do based on the information calculated, rank each node, to see which one performs the best on average.  This should be done by all the metrics described in rank_cases
    pass

def rank_connections():
    #To do based on the information calculated, rank each node, to see which pairs of nodes performs the best on average.  So this analysis will focus on how long it takes to transition work from node A to node B (For example)
    pass

def assess_system_over_time():
    #As new cases come in a base line should be established for how well the system is doing from time to time.  This is more or less measuring average productivity over time and looking at the first and second derivative over time. Use the complex plane trick to get this by fitting from a curve.  Use interpolation to get this.

def projected_system_performance():
    #When enough data has been added, we'll be able to assess how well the system performs on average and project how well it should perform if parts of the process are improved.  By understanding the productivity increases of new systems, we'll have a sense of what to work on next - assumes we can determine this ahead of time.
    


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
