import pandas as pd
stud_marks=pd.Series({'Shreya':20,'Rakshit':22,'Srijan':18,'ABY':45,'Shini':56})
stud_age=pd.Series({'Shreya':20,'Rakshit':22,'Srijan':18,'ABY':45,'Shini':56})
stud_df=pd.DataFrame({'Marks':stud_marks,'Ahe':stud_age})
print(stud_df)
print(stud_df.sort_values(by=['Marks']))
print(stud_df.sort_values(by=['Marks'],ascending=False))