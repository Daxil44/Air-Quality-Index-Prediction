# AQI's data downloda from openweathermap.com
# this data are divided into hours but we want data in daily base so we pre process the data and clean the data (because we no-data and other stuff)

import pandas as pd
import matplotlib.pyplot as plt

def avg_data_2013():
    temp_i=0
    average=[]  #list
    # because our data in hours and we want in day
    for rows in pd.read_csv("Data/AQI/aqi2013.csv",chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                # data cleaning here
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i) # convert string data in to float
                    add_var=add_var+temp #total of PM2.4
        avg=add_var/24 #avg of PM2.4
        temp_i=temp_i+1

        average.append(avg)
    return average

def avg_data_2014():
    temp_i=0
    average=[]  #list
    # because our data in hours and we want in day
    for rows in pd.read_csv("Data/AQI/aqi2014.csv",chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                # data cleaning here
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i) # convert string data in to float
                    add_var=add_var+temp #total of PM2.4
        avg=add_var/24 #avg of PM2.4
        temp_i=temp_i+1

        average.append(avg)
    return average

def avg_data_2015():
    temp_i=0
    average=[]  #list
    # because our data in hours and we want in day
    for rows in pd.read_csv("Data/AQI/aqi2015.csv",chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                # data cleaning here
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i) # convert string data in to float
                    add_var=add_var+temp #total of PM2.4
        avg=add_var/24 #avg of PM2.4
        temp_i=temp_i+1

        average.append(avg)
    return average

def avg_data_2016():
    temp_i=0
    average=[]  #list
    # because our data in hours and we want in day
    for rows in pd.read_csv("Data/AQI/aqi2016.csv",chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                # data cleaning here
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i) # convert string data in to float
                    add_var=add_var+temp #total of PM2.4
        avg=add_var/24 #avg of PM2.4
        temp_i=temp_i+1

        average.append(avg)
    return average

def avg_data_2017():
    temp_i=0
    average=[]  #list
    # because our data in hours and we want in day
    for rows in pd.read_csv("Data/AQI/aqi2017.csv",chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                # data cleaning here
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i) # convert string data in to float
                    add_var=add_var+temp #total of PM2.4
        avg=add_var/24 #avg of PM2.4
        temp_i=temp_i+1

        average.append(avg)
    return average

def avg_data_2018():
    temp_i=0
    average=[]  #list
    # because our data in hours and we want in day
    for rows in pd.read_csv("Data/AQI/aqi2018.csv",chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                # data cleaning here
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i) # convert string data in to float
                    add_var=add_var+temp #total of PM2.4
        avg=add_var/24 #avg of PM2.4
        temp_i=temp_i+1

        average.append(avg)
    return average

if __name__=="__main__":
    lst2013 = avg_data_2013()
    lst2014 = avg_data_2014()
    lst2015 = avg_data_2015()
    lst2016 = avg_data_2016()
    lst2017 = avg_data_2017()
    lst2018 = avg_data_2018()
    plt.plot(range(0, 365), lst2013, label="2013 data")
    plt.plot(range(0, 364), lst2014, label="2014 data")
    plt.plot(range(0, 365), lst2015, label="2015 data")
    # plt.plot(range(0, 121), lst2016, label="2016 data")
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    plt.show()

