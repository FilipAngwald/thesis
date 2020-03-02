import pandas as pd
import numpy as np
import datetime
from datetime import date

### Price model
#Function for providing cost for different grid operators and power deals

#### Spot price from Nordpool

yearly_spotprice = pd.read_excel('spotpris.xlsx', sheet_name=0) # SEK/MWh


def cost_spotprice(power_profile, start_date,end_date):
    
    
    initial = ((start_date-date(start_date.year,1,1)).days)*24
    duration = ((end_date-start_date).days)*24   
    spot_price = (yearly_spotprice['mean_price'][initial:initial+duration])/1000 # convert to SEK/kWh
    spotprice_cost=(power_profile.T*spot_price)/1000 #convert to kWh
    
    return spotprice_cost



