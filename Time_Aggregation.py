import pandas
import os
import glob
import numpy as np

#This is the third script you will run. This aggregates the data by hour, day, week, and month.
#Time aggregated averages and their corresponding variances will be calculated for every column that has
#a numerical column
#You will need to run this twice 1)for A data and 2) for B data
#This script will create 4 new directories corresponding to each of the time aggregates with the corresponding
#data files in each


indir = '/Users/sara/Documents/PurpleAir_Project/SoCalData/PrimaryData/A/reformatted/cleaned' #change this to point to your ./data/A/reformatted/cleaned and ./data/B/reformatted/cleaned directory
os.chdir(indir)
fileList = glob.glob("*.xlsx")
for filename in fileList:
    print(filename)
    df = pandas.read_excel(filename)
    reg_index = df['created_at']
    datetime_index = pandas.to_datetime(reg_index)
    df.index = datetime_index
    Aggregates = ['H', 'D', 'W', 'M']
    outdirs = ['./hourly', './daily', './weekly', './monthly']
    for a in range(len(Aggregates)):
        print(a)
        outdir = outdirs[a]
        print(outdir)
        if not os.path.exists(outdir):
            os.mkdir(outdir)
        Arg = Aggregates[a]
        print(Arg)
        resampled = df.resample(Arg).agg([np.mean,np.var])
        resampled.columns = np.concatenate([resampled.iloc[0,:2], resampled.columns[2:]])
        resampled = resampled.iloc[1:].reset_index(drop=False)
        resampled.dropna(subset = resampled.columns[[-2]],inplace=True)
        fullname = os.path.join(outdir, filename)
        print(fullname)
        resampled.to_excel(fullname)
