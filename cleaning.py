import os
import glob
import pandas

#This is the second script you should use. This script will eliminate any data that has an erroneous temperature
#of humidity for channel A and erroneous pressure. It will eliminate any rows where there is no PM2.5 data.
#You will need to run this file for both the A and the B data. When running for each make sure to change the
#directory where each resides and comment/uncomment parts of the code intended for each (indicated in the code below)
#This script will output cleaned data files to a new directory "cleaned"


indir = '/Users/sara/Documents/PurpleAir_Project/SoCalData/PrimaryData/B/reformatted' #make sure this points to your ./data/A/reformatted and ./data/B/reformatted directories
os.chdir(indir)
fileList = glob.glob("*.xlsx")
for filename in fileList:
    print(filename)
    df = pandas.read_excel(filename)
    outname = filename
    outdir = './cleaned'
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    fullname = os.path.join(outdir, outname)
    df = df.drop(columns='Unnamed: 0', errors='ignore')
    #Temp = df['Temperature_F']                          #For A
    #for t in range(len(Temp)):                          #For A
    #    if Temp[t] >= 200.0:                            #For A
    #        print(Temp[t])                              #For A
    #        print(t)                                    #For A
    #        df.drop(axis=0, index=t, inplace=True)      #For A
    #df.dropna(subset=['Temperature_F'], inplace=True)   #For A
    #df.dropna(subset=['Humidity_%'], inplace=True)      #For A
    df.dropna(subset=['PM2.5_ATM_ug/m3'], inplace=True)
    df.dropna(subset=['Pressure_hpa'], inplace=True)
    #df.dropna(subset=['Temperature_F'], inplace=True)   #For A
    df.to_excel(fullname)
