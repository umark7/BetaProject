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
    if pd.isna(questions[index][0])
        return 5
    elif questions[index][1].find('Open')!=-1:
        return 4
    elif questions[index][1].find('Response')!=-1 and questions[index+1][1].find('Other')==-1:
        return 1
    elif questions[index][1].find('Response')!=-1 and questions[index+1][1].find('Other')!=-1:
        return 2
    elif questions[index][1].find('Response')==-1 and questions[index][1].find('specify') == -1 and questions[index][1].find('Open') == -1:
        return 3
     
#print(questions[10][0])  
#print(qtype(16))

#input the index of the question you want a graph of and the dataframe with all the answers
#this function will generate a graph for that question
def switch_case(index,df):
    if qtype(index) == 5:
        print("ERROR: Inputted index is part of a multi-column question. Enter the first index of the question.")
        pass
    
    elif qtype(index) == 4:
        print(df[index])
        #return df[index]
        
    elif qtype(index) == 1:
        pass #this is where Rishi's code will go
        
    elif qtype(index) == 2:
        question_df = df[index]
        plt.figure(figsize=(8,5))
        g = sns.countplot(y = df[index])
        #q_title = questions[index][0]
        plt.title(q_title)
        print(g)
        print(df[index+1])
        #return question_df
        
    elif index == 41:
        cols = [41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57]
        question_df = df[cols]
        question_IDdf = questions[cols]
        
        #make a new dataframe where each row is the part and if it was yes or no
        q_array = []
        for i in range(41,56):
            for j in range(0,60):
                q_part = questions.iloc[1][i]
                yn = df.iloc[j][i]
                q_array.append([q_part,yn])
        #make graph        
        q_df = pd.DataFrame(q_array, columns=['Factor', 'Answer'])
        sns.countplot(y = 'Factor', hue = 'Answer', data = q_df, orient ='h')
    
    elif qtype(index) == 3:
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
        
        #return question_df
        
switch_case(, dataf)
