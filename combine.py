# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 10:37:21 2020

@author: Rohit
"""

import os
import glob
import pandas as pd
os.remove("C:/Users/Rohit/Desktop/combined_csv.csv")

os.chdir("C:/Users/Rohit/Desktop/project/")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv

combined_csv.to_csv( "C:/Users/Rohit/Desktop/combined_csv.csv", index=False, encoding='utf-8-sig')
