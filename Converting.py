import pandas
import os
import glob
import re

#This script is intended to process PurpleAir data so that there are columns with Lat, Long, The Sensor Name, and the channel used
#This is the first script you should use and you will have to run it twice 1)for A 2)for B
#Before you run this script you should change the indir to the directory where your A data lives and then where you B data lives
#The output are uniformly reformatted excel files in a new directory titled "reformatted"

indir = '/Users/sara/Documents/PurpleAir_Project/SoCalData/PrimaryData/B'
os.chdir(indir)
fileList = glob.glob("*.csv")
for filename in fileList:
    df = pandas.read_csv(filename)
    lat_long = re.findall('\d*\.\d+',filename)
    time = df['created_at']
    time_new = time.replace(' UTC','')
    lat = [lat_long[0]] * len(time)
    long_pos = lat_long[1]
    long_flt = float(long_pos)
    long_neg = -long_flt
    long = [long_neg] * len(time)
    Station = [filename[0:40]] * len(time)
    Sensor = ['A'] * len(time)
    df.insert(0, 'Longitude',long)
    df.insert(1, 'Latitude', lat)
    df.insert(2, 'Station',Station)
    df.insert(3,'Sensor',Sensor)
    df['created_at'] = df['created_at'].str.replace(" UTC", "", case=False)
    df.rename(columns={"created_at" : "created_at (UTC)"})
    if 'entry_id' not in df:
        entry = -9999*len(time)
        df.insert(5,'entry_id',entry)
    df = df.drop(columns='Unnamed: 0',errors='ignore')
    df = df.drop(columns='Unnamed: 1', errors='ignore')
    df = df.drop(columns='Unnamed: 2', errors='ignore')
    df = df.drop(columns='Unnamed: 3', errors='ignore')
    df = df.drop(columns='Unnamed: 4', errors='ignore')
    df = df.drop(columns='Unnamed: 5', errors='ignore')
    df = df.drop(columns='Unnamed: 6', errors='ignore')
    df = df.drop(columns='Unnamed: 7', errors='ignore')
    df = df.drop(columns='Unnamed: 8', errors='ignore')
    df = df.drop(columns='Unnamed: 9', errors='ignore')
    df = df.drop(columns='Unnamed: 10', errors='ignore')
    df = df.drop(columns='Unnamed: 11', errors='ignore')
    df = df.drop(columns='Unnamed: 12', errors='ignore')
    df = df.drop(columns='Unnamed: 13', errors='ignore')
    df = df.drop(columns='Unnamed: 14', errors='ignore')
    df = df.drop(columns='Unnamed: 15', errors='ignore')
    outdir = './reformatted'
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    filename = filename.replace('csv','xlsx')
    fullname = os.path.join(outdir,filename)
    print(fullname)
    df.to_excel(fullname)









