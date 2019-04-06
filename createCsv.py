#!/usr/bin/env python3
import csv
import sqlite3

class createCsv:

    # Initializer / Instance Attributes
    def __init__(self, dbName,flename):
        self.dbName = dbName
        self.outputfilename = flename

    #get datafromDatabase
    def GenerateReport(self):

        #open sql connection
        conn = sqlite3.connect(self.dbName)
        cur = conn.cursor()

        #call init csv
        self.InitCSV()

        #get all diffrent days
        cur.execute("SELECT * FROM `SENSEHAT_Data`;")

        #loop throught days
        result= cur.fetchall()
        for row in result:
            date = row[0]
            time = row[1]
            temprature = row[2]
            humidity = row[3]
            
            #append data to csv
            self.writeToCSV(date,time,temprature,humidity)

    #append the data to csv
    def writeToCSV(self,date,time,temprature,humidity):

        with open(self.outputfilename , 'a', newline='') as file:

            #append data
            writer = csv.writer(file,escapechar='', quoting=csv.QUOTE_NONE)
            writer.writerow([date,time,temprature,humidity])

    #init csv header
    def InitCSV(self):
        
        with open(self.outputfilename , 'w',newline='') as file:

            #append initial row
            writer = csv.writer(file)
            writer.writerow(['Date','Time','Temprature','Humidity'])



report = createCsv('sensehat.db','temp.csv')
report.GenerateReport()