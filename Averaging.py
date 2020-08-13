import pandas
import os
import glob
import numpy as np

#This is the fourth script you will run. This script throws out data points that vary too much between the A and B channels and then averages
#the concentrations and variances in the A and B channels for each row of data in each time aggregate.
#You only need to run this script once and will populate your outdirectory with subdirectories containing
#monthly, weekly, daily, and hourly averaged data.


indir_A = '/Users/sara/Library/Mobile Documents/com~apple~CloudDocs/Documents/PurpleAir_Project/SoCalData/PrimaryData/A/reformatted/'
indir_B = '/Users/sara/Library/Mobile Documents/com~apple~CloudDocs/Documents/PurpleAir_Project/SoCalData/PrimaryData/B/reformatted/'
Aggregates = ['cleaned/hourly', 'cleaned/daily', 'cleaned/weekly', 'cleaned/monthly']
for a in Aggregates:
    indir_A_agg = os.path.join(indir_A,a)
    indir_B_agg = os.path.join(indir_B,a)
    os.chdir(indir_A_agg)
    fileList_A = glob.glob("*.xlsx")
    for filename in fileList_A:
        print(filename)
        df_A_agg = pandas.read_excel(filename)
        df_A_agg = df_A_agg.drop(columns='Unnamed: 0', errors='ignore')
        df_A_agg.columns = df_A_agg.columns.str.replace(r"'","")
        os.chdir(indir_B_agg)
        filename_B = filename.replace('(outside)','B (undefined)')
        df_B_agg = pandas.read_excel(filename_B)
        df_B_agg = df_B_agg.drop(columns='Unnamed: 0', errors='ignore')
        df_B_agg.columns = df_B_agg.columns.str.replace(r"'","")
        merged = pandas.merge(left = df_A_agg, left_on='created_at', right = df_B_agg, right_on='created_at')
        PM25_B = merged['(PM2.5_ATM_ug/m3, mean)_y']
        PM25_A = merged['(PM2.5_ATM_ug/m3, mean)_x']
        PM25_B_var = merged['(PM2.5_ATM_ug/m3, var)_y']
        PM25_A_var = merged['(PM2.5_ATM_ug/m3, var)_x']
        comb_pm25 = [PM25_A,PM25_B]
        tot_pm25 = pandas.concat(comb_pm25)
        stdev = tot_pm25.std()
        os.chdir(indir_A_agg)
        averages = []
        variances = []
        for i in range(len(PM25_A)):
            A = PM25_A[i]
            print(A)
            A_var = PM25_A_var[i]
            print(A_var)
            B = PM25_B[i]
            print(B)
            B_var = PM25_B_var[i]
            print(B_var)
            diff = abs(A-B)
            if diff > 5.0 and diff > 2*stdev:
                merged.drop(axis=0,index=i,inplace=True)
            else:
                combine = [A,B]
                combine_var = [A_var,B_var]
                avg = np.mean(combine)
                var = np.mean(combine_var)
                averages = np.append(averages, avg)
                variances = np.append(variances, var)
        merged['Average_A_B'] = averages
        merged['Variance_A_B'] = variances
        merged.index.name = 'index'
        outdir_1 = '/Users/sara/Library/Mobile Documents/com~apple~CloudDocs/Documents/PurpleAir_Project/Downloaded_Data' #change this to wherever you want your A&B averaged data to live
        os.chdir(outdir_1)
        full_path = os.path.join(outdir_1, a)
        if not os.path.exists(full_path):
            os.mkdir(full_path)
        fullname = os.path.join(full_path,filename)
        merged.to_excel(fullname)
        os.chdir(indir_A_agg)








