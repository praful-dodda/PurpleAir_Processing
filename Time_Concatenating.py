import os
import glob
import pandas

#This file concatenates all of the data from all of the different sensors into one file for the different time aggregates.
#You will need to change the "indir" 4 times to reflect where your averaged aggregated lives: monthly, weekly, daily, hourly
#This script will output the concatenated file in the same folder as your indir

indir='/Users/sara/Library/Mobile Documents/com~apple~CloudDocs/Documents/PurpleAir_Project/Downloaded_Data/cleaned/monthly'
outfile="PurpAir_Station_monthly_Concatenated.xlsx"
os.chdir(indir)
fileList=glob.glob("*.xlsx")
dfList=[]
for filename in fileList:
    print(filename)
    df=pandas.read_excel(filename,index=None)
    dfList.append(df)
concatDf=pandas.concat(dfList,axis=0,ignore_index=True)
concatDf.to_excel(outfile)

