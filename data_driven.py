# import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


#data Pre processing
driven_data=pd.read_csv("C:\\Users\\gdnir\\Desktop\\OSU_Dec\\Transfer_dec_'16-20161215T045007Z\Transfer_dec_'16\\Drive_Data\\Train.csv")

driven_data_clean=driven_data.drop(['date_recorded','funder','installer','wpt_name','subvillage','region','region_code','district_code','lga','ward','scheme_name','quantity','source','waterpoint_type_group'] ,axis=1)
driven_data_clean.head(5)

data=driven_data_clean.fillna(method='pad')

data.isnull().values.any()

data.dtypes

