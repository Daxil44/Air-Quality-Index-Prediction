# webscraping

from Plot_AQI import avg_data_2013,avg_data_2014,avg_data_2015,avg_data_2016
import pandas as pd
import sys
import os
import csv
import requests
from bs4 import BeautifulSoup
# for webscraping

def met_data(month,year):
    file_html=open('Data/Html_Data/{}/{}.html'.format(year,month),'rb')
    plain_text =file_html.read()

    tempD=[]
    finalD=[]

    soup= BeautifulSoup(plain_text,"lxml")
    for table in soup.findAll('table',{'class':'medias mensuales numspan'}):# we get class name from inspect the website tutiempo
            for tbody in table:
                for tr in tbody:
                    a=tr.get_text()
                    tempD.append(a)

    rows = len(tempD)/15
    #print(tempD[0])
       # we have 15 features in table so we divide them
    for times in range(round(rows)):
        newtempD = []
        for i in range(15):
            newtempD.append(tempD[0])
            tempD.pop(0)
        finalD.append(newtempD)
    #print(finalD)
    # my data are divid in months  in finalID list each list of list contain 1 month's values[[]]
    length = len(finalD)

    finalD.pop(length - 1)
    finalD.pop(0)
    #print(finalD)

    for a in range(len(finalD)):
        finalD[a].pop(6)
        finalD[a].pop(13)
        finalD[a].pop(12)
        finalD[a].pop(11)
        finalD[a].pop(10)
        finalD[a].pop(9)
        finalD[a].pop(0)

    #print(finalD)
    return finalD


def data_combine(year, cs):
    for a in pd.read_csv('Data/Real-Data/real_' + str(year) + '.csv', chunksize=cs):
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()
    return mylist


if __name__ == "__main__":
    if not os.path.exists("Data/Real-Data"):
        os.makedirs("Data/Real-Data")
    for year in range(2013, 2017):
        final_data = []
        with open('Data/Real-Data/real_' + str(year) + '.csv', 'w') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            wr.writerow(
                ['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        for month in range(1, 13):
            temp = met_data(month, year)
            final_data = final_data + temp
        #print(final_data)
        pm = getattr(sys.modules[__name__], 'avg_data_{}'.format(year))()
        # here we did not want use fun. like (avg_data_2013,avg_data_2014,avg_data_2015,avg_data_2016) so we did this
        # to get PM 2.5 from Plot_AQI.py
        #print(pm)

        if len(pm) == 364:
            pm.insert(364, '-')

        for i in range(len(final_data) - 1):
            # final[i].insert(0, i + 1)
            final_data[i].insert(8, pm[i])
        # print(final_data)

        with open('Data/Real-Data/real_' + str(year) + '.csv', 'a') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            for row in final_data:
                flag = 0
                for elem in row:
                    if elem == "" or elem == "-":# here i remove blank data ex.(like '-','')
                        flag = 1
                    if flag != 1:
                        wr.writerow(row)
            #print(final_data)
    data_2013 = data_combine(2013, 600)
    data_2014 = data_combine(2014, 600)
    data_2015 = data_combine(2015, 600)
    data_2016 = data_combine(2016, 600)

    total = data_2013 + data_2014 + data_2015 + data_2016

    with open('Data/Real-Data/Real_Combine1.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(
            ['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(total)

df = pd.read_csv('Data/Real-Data/Real_Combine.csv')