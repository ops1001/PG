#!/Users/Edward/anaconda3/bin/python

import tempfile, sys, os
import pandas as pd
import numpy as np
from datetime import date

root_dir = '/Users/Edward/Gauss/'
field = sys.argv[1]

# read all stock names in the R3K index
df = pd.read_csv('%s/data/Eq/Universe/Univ_RAY.csv' % root_dir)
#df = pd.read_csv('%s/data/Eq/Universe/Univ_ETF_Equity_List.csv' % root_dir)

names = np.array([str.split()[0] for str in df.Ticker.values])

# get the start and end date
start_date = date(1990, 1,1)
end_date = date.today()
sd_str = start_date.strftime('%m/%d/%Y')
ed_str = end_date.strftime('%m/%d/%Y')
sd_str1 = start_date.strftime('%Y%m%d')
ed_str1 = end_date.strftime('%Y%m%d')

# get the query for each stock
query_str = [];
all_names = []
for s in names:
    all_names.append("%s_1_FQ" % s)
    query_str.append("=BDH(\"%s equity\", \"%s\", \"%s\", \"%s\")" % (s, field, sd_str, ed_str))
    all_names.append("%s_2_Date"%s)
    query_str.append("")
    all_names.append("%s_3_Time"%s)
    query_str.append("")
    all_names.append("%s_EPS_1_Rpt"%s)
    query_str.append("")
    all_names.append("%s_EPS_2_Comp"%s)
    query_str.append("")
    all_names.append("%s_EPS_3_Est"%s)
    query_str.append("")

query_str = np.array(query_str)
all_names = np.array(all_names)

qdf = pd.DataFrame(pd.Series(query_str, index=all_names)).sort_index().T
qdf.to_csv('%s/query/bbg_ern_%s_%s_%s.csv' % (root_dir, field, sd_str1, ed_str1), index=False)

