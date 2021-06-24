#!/usr/bin/env python
# coding: utf-8

# In[67]:


#import libraries
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('ggplot')
import seaborn as sns

headers = ['respondentID', 'collectorID', 'start_date', 'end_date', 'IPaddress', 'email', 'first_name', 'last_name', 'custom_data1', 
            'q1', 'q2', 'q2_specify', 'q3', 'q4', 'q4_specify', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12',
            'q13_prize', 'q13_NASA', 'q13_interesting', 'q13_existing', 'q13_sponsor', 'q13_community', 'q13_glory', 
            'q13_testing', 'q13_feedbak','q13_mentoring', 'q13_exposure', 'q13_validation', 'q13_partners', 'q13_regulators', 
            'q13_networking', 'q13_collab', 'q14', 'q15_prize', 'q15_NASA', 'q15_interesting', 'q15_existing', 'q15_sponsor', 
            'q15_community', 'q15_glory', 'q15_testing', 'q15_feedbak','q15_mentoring', 'q15_exposure', 'q15_validation', 
            'q15_partners', 'q15_regulators', 'q15_networking', 'q15_collab', 'q16_prize', 'q16_NASA', 'q16_interesting', 
            'q16_existing', 'q16_sponsor', 'q16_community', 'q16_glory', 'q16_testing', 'q16_feedbak','q16_mentoring', 
            'q16_exposure', 'q16_validation', 'q16_partners', 'q16_regulators', 'q16_networking', 'q16_collab',
            'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q30_specify', 
            'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40', 'q41_salries', 'q41_travelcost', 'q41_fees', 
            'q41_equipcost', 'q41_overhead', 'q41_specify', 'q42', 'q43', 'q44', 'q45', 'q46', 'q47', 'q48', 'q49', 
            'q50', 'q51', 'q52', 'q53', 'q54', 'q55', 'q56', 'q57', 'q58_name', 'q58_company', 'q58_address', 
            'q58_address2', 'q58_city', 'q58_state', 'q58_zip', 'q58_country', 'q58_email', 'q58_phone' ] 

#import CSV
dataf = pd.read_csv (r'C:\users\camih\documents\NASA_Centennial_Challenges_Survey.csv', skiprows = [0,1], header = None, names = headers) 
questions = pd.read_csv(r'C:\users\camih\documents\NASA_Centennial_Challenges_Survey.csv', nrows=0)
pd.set_option("display.max_rows", None, "display.max_columns", None)

#I should make a new db with same column names and for each it has type of question and amount of columns, and the question itself
#q_cols[1] is the amount of columns dedicated to question 1
q_cols = [0,1,2,1,2,1,1,1,1,1,1,1,1,16,1,16,16,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,6,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,10]
dataf


# In[118]:


#question graph
def singlecol_bargraph(qnum, colname):
    #sns.barplot(data = dataf[colname])
    #print(dataf[colname])

    #x axis: response options
    #X = list(dict.fromkeys(dataf[colname]))
    #print(X)
    
    #y axis: percent of each response
    #table =dataf.groupby(colname).size()
    #print(table)
    #total = sum(table)
    #end = len(table)
    #percents = []
    #for i in range(0,end):
    #    percents.append(round((((table[i]*1.0)/(total*1.0))*100), 2))
    #print(percents)
    
    bargraph = sns.countplot(x = colname, data = dataf)
    
    for p in bargraph.patches:
        bargraph.annotate(format(p.get_height(), '.1f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (0, 9), 
                   textcoords = 'offset points')
    #plt.xlabel(questions[qnum], size=14) #make a function to translate q num to index
    #plt.ylabel("amount per response", size=14) 
singlecol_bargraph(3, 'q3')

#def multcol_bargraph(numcol, colname):
#    index = 23#dataf.columns.get_loc(colname)
#    print(index)
#    
#    for n in range(0,numcol):
#        index= index+n
#        colnamee = dataf.columns[index]
#        print(sns.countplot(x = colnamee, data = dataf))
#multcol_bargraph(q_cols[2], 'q2')


# In[196]:


#make separate data frames for complex questions:
q13_df = dataf[['q13_prize', 'q13_NASA', 'q13_interesting', 'q13_existing', 'q13_sponsor', 'q13_community', 'q13_glory', 
            'q13_testing', 'q13_feedbak','q13_mentoring', 'q13_exposure', 'q13_validation', 'q13_partners', 'q13_regulators', 
            'q13_networking', 'q13_collab']]

q15_df = dataf[['q15_prize', 'q15_NASA', 'q15_interesting', 'q15_existing', 'q15_sponsor', 'q15_community', 'q15_glory', 
            'q15_testing', 'q15_feedbak','q15_mentoring', 'q15_exposure', 'q15_validation', 'q15_partners', 'q15_regulators',
            'q15_networking', 'q15_collab']]

q16_df = dataf[['q16_prize', 'q16_NASA', 'q16_interesting', 'q16_existing', 'q16_sponsor', 'q16_community', 'q16_glory', 
            'q16_testing', 'q16_feedbak','q16_mentoring', 'q16_exposure', 'q16_validation', 'q16_partners', 'q16_regulators', 
            'q16_networking', 'q16_collab']]

q15_df


# In[271]:


plt.figure(figsize=(18,10))
q13 = sns.violinplot(data = q13_df, size = 2.1, inner = "quartile")
plt.xticks(rotation=45)
print(q13)

#plt.figure(figsize=(18,10))
#ans = dataf.groupby('q15_prize').size()
#sns.countplot(data = q15_df)
#for col in q15_df:
#    sns.countplot(x = col, data = q15_df)
ex = ['q15_prize', 'q15_NASA', 'q15_interesting', 'q15_existing', 'q15_sponsor', 'q15_community', 'q15_glory', 
            'q15_testing', 'q15_feedbak','q15_mentoring', 'q15_exposure', 'q15_validation', 'q15_partners', 'q15_regulators',
            'q15_networking', 'q15_collab']

#sns.countplot(x = 'q15_prize', data = q15_df, hue = "q15_NASA")
#plt.xticks(rotation=80)
#print(q15)

fig, ax =plt.subplots(1,16,figsize=(15,3))
plt.xticks(rotation=80)
sns.countplot(x = q15_df['q15_prize'], ax=ax[0])
sns.countplot(x = q15_df['q15_NASA'], ax=ax[1])
sns.countplot(x=q15_df['q15_interesting'], ax=ax[2])
sns.countplot(x=q15_df['q15_existing'], ax=ax[3])
sns.countplot(x=q15_df['q15_sponsor'], ax=ax[4])
sns.countplot(x=q15_df['q15_community'], ax=ax[5])
sns.countplot(x=q15_df['q15_glory'], ax=ax[6])
sns.countplot(x=q15_df['q15_testing'], ax=ax[7])
sns.countplot(x=q15_df['q15_feedbak'], ax=ax[8])
sns.countplot(x=q15_df['q15_mentoring'], ax=ax[9])
sns.countplot(x=q15_df['q15_exposure'], ax=ax[10])
sns.countplot(x=q15_df['q15_validation'], ax=ax[11])
sns.countplot(x=q15_df['q15_partners'], ax=ax[12])
sns.countplot(x=q15_df['q15_regulators'], ax=ax[13])
sns.countplot(x=q15_df['q15_networking'], ax=ax[14])
sns.countplot(x=q15_df['q15_collab'], ax=ax[15])
fig.show()

plt.figure(figsize=(20,10))
q16 = sns.violinplot(data = q16_df, size = 6, inner = "quartile")
plt.xticks(rotation=45)
print(q16)


# In[252]:




