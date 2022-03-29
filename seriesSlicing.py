#import pandas as pd
#s = pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])
#print(s[0])
#print(s[:3])
#print(s[-3:])

import pandas as pd
s = pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])
print(s.iloc[1:4])
print(s.loc['b':'e'])