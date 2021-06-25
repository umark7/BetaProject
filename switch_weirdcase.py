import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('ggplot')
import seaborn as sns
import textwrap

#this is just to specify which columns to use. Its kinda wordy but gets the job done
cols = []
for i in range(9,129):
    cols.append(i)

#For now just download to your computer and use that pathway or figure out how to download from google sheets.
dataf = pd.read_csv(r'C:\users\cehall3\documents\NASA_Centennial_Challenges_Survey.csv', skiprows = [0,1], header = None, usecols = cols) 
questions = pd.read_csv(r'C:\users\cehall3\documents\NASA_Centennial_Challenges_Survey.csv', nrows=2, header = None, usecols = cols)
pd.set_option("display.max_rows", None, "display.max_columns", None)
dataf

def qtype(index):
    if questions[index][1].find('Response')==-1 and questions[index][1].find('specify') == -1 and questions[index][1].find('Open') == -1:
        return 3
    else:
        return 1
    
def switch_case(index,df):
    if qtype(index) == 3:
        
        #create new data frame
        first_col = index
        last_col = index
        question_cols = [index]
        index = index+1
        while pd.isna(questions[index][0]):
            question_cols.append(index)
            last_col = index
            index+=1
        question_df = df[question_cols]
        question_IDdf = questions[question_cols]
        
        #create array of tick names
        tik_names = question_IDdf.iloc[1]
        
        #create array to specify amount of tiks
        tiks=[]
        for i in range(0,len(question_cols)):
            tiks.append(i)
        
        #make graph from dataframe
        plt.figure(figsize=(8,12))
        g = sns.violinplot(data = question_df, size = 6, inner = "quartile", orient='h')
        plt.title("\n".join(textwrap.wrap(question_IDdf.iloc[0,0], 80)))
        plt.yticks(ticks = tiks, labels = tik_names)
        print(g)
        
switch_case(23, dataf)
