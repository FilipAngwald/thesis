# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:34:47 2020

@author: Filip
"""
#### Vattenfall E4 power deal

def vattenfall_E4(power_profile, main_fuse, start_date, end_date):
    
    #Fixed cost per year depends on main fuse
    
    if main_fuse == 12:
        fixed_cost = 1472
    elif main_fuse == 16:
        fixed_cost = 3464 
    elif main_fuse == 20:
        fixed_cost = 4840 
    elif main_fuse == 35:
        fixed_cost = 8296
    elif main_fuse == 50:
        fixed_cost = 11920
    elif main_fuse == 63:
        fixed_cost = 16080 
        
    transmission_cost = 0.272 #SEK/kWh
    
    #Days in interval
    days = ((end_date-start_date).days)
    
    #Cost is per month with the yearly fixed cost for the amount of days in interval
    
    deal_cost = sum(transmission_cost*power_profile/1000) + (days*fixed_cost/365)
    
    return deal_cost



def vattenfall_T4(power_profile, main_fuse, start_date, end_date):
    
    #Fixed cost per year depends on main fuse
    
    if main_fuse == 12:
        fixed_cost = 1472
    elif main_fuse == 16:
        fixed_cost = 3464 
    elif main_fuse == 20:
        fixed_cost = 4840 
    elif main_fuse == 35:
        fixed_cost = 8296
    elif main_fuse == 50:
        fixed_cost = 11920
    elif main_fuse == 63:
        fixed_cost = 16080 
        
    transmission_cost_peak_hours = 56.0 #SEK/kWh
    transmission_cost_regular_hours = 14.8 #SEK/kWh
    
    #Days in interval
    days = ((end_date-start_date).days)
    
    #Cost is per month with the yearly fixed cost for the amount of days in interval
    if start_date.month == 1 or 2 or 3 or 11 or 12 :
        for i in power_profile:
            if i 
        deal_cost = sum(transmission_cost_peak_hours*power_profile/1000) + (days*fixed_cost/365)
    else :
        deal_cost = sum(transmission_cost_regular_hours*power_profile/1000) + (days*fixed_cost/365)
    
    return deal_cost