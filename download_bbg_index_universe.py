#!/Users/Edward/anaconda3/bin/python

import tempfile, sys, os
import pandas as pd
import numpy as np
from datetime import date

root_dir = '/Users/Edward/Gauss/'
index_bid = sys.argv[1]


all_names = []
query_str = []
sd_year = 1995
ed_year = 2018

for y in range( sd_year, ed_year):
    date_str= str(y)+str(1231)
    all_names.append(date_str)
    query_str.append("=BDS(\"%s index\", \"indx_mweight_hist\", \"END_DATE_OVERRIDE =%s\")" % ( index_bid, date_str))
    all_names.append("")
    query_str.append("")
all_names = np.array( all_names)
query_str = np.array( query_str)

qdf = pd.DataFrame(pd.Series(query_str, index=all_names)).T

qdf.to_csv('%s/query/bbg_%s_universe_%s_%s.csv' % (root_dir, index_bid, str(sd_year), str(ed_year)), index=False)