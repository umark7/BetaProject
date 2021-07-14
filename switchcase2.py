def qtype(index):
    if questions[index][1].find('Open')!=-1:
        return 1
    elif pd.isna(questions[index][0]):
        return 2
    elif questions[index][1].find('Response')!=-1 and questions[index+1][1].find('Other')==-1:
        return 3
    elif questions[index][1].find('Response')!=-1 and questions[index+1][1].find('Other')!=-1:
        return 4
    elif questions[index][1].find('Response')==-1 and questions[index][1].find('specify') == -1 and questions[index][1].find('Open') == -1:
        return 5
     
def switch_case(index,df):
    #Short Answer
    if qtype(index) == 1:
        print(questions[index][0])
        print(df[index])
    
    elif qtype(index) == 2:
        print("ERROR: Inputted index is part of a multi-column question. Enter the first index of the question.")
        pass
    
    #normal response single-column
    elif qtype(index) == 3:
        question_df=df[index]
        plt.figure(9)
        g = sns.countplot(y = df[index])
        q_title = questions[index][0]
        plt.title(q_title)
        plt.ylabel("Answer")
        plt.xlabel("Count")
        #fig=plt.figure(9)
        #question_df.plot.hist()
        #plt.xlabel("Ranking")
        #plt.title('Reason for particpation:Applying existing technology in a new way')
        plt.show
    
    #has "specify other" option
    elif qtype(index) == 4:
        question_df = df[index]
        plt.figure(figsize=(8,5))
        g = sns.countplot(y = df[index])
        q_title = questions[index][0]
        plt.title(q_title)
        plt.ylabel("Answer")
        plt.xlabel("Count")
        print(g)
        print(df[index+1])
        #return question_df
    
    #question 15
    elif index == 40:
        #make new dataframe for export
        cols = [40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56]
        question_df = df[cols]
        question_IDdf = questions[cols]
        
        #make a new dataframe where each row is the part and if it was yes or no
        q_array = []
        for i in range(40,56):
            for j in range(0,df.shape[0]):
                q_part = questions.iloc[1][i]
                yn = df.iloc[j][i]
                q_array.append([q_part,yn])
        #make graph    
        q_df = pd.DataFrame(q_array, columns=['Factor', 'Answer'])
        plt.figure(figsize=(8,10))
        sns.countplot(y = 'Factor', hue = 'Answer', data = q_df, orient ='h')
        p_title = questions[index][0]
        plt.title(p_title)
    
    #question 41
    elif index == 97:
        s = df[97].count()
        t = df[98].count()
        c = df[99].count()
        e = df[100].count()
        o = df[100].count()
        
        xaxis = [s,t,c,e,o]
        yaxis = ['Salaries', 'Travel costs', 'Contractor/consultant fees', 'Equipment costs', 'Overhead']
        plt.figure(figsize = (8,5))
        sns.barplot(x = xaxis, y = yaxis, orient = 'h')
        plt.title(questions[index][0])
        
    elif index == 119:
        print(questions[index][0])
        for i in range(119, 129):
            print(questions[i][1])
            print(df[i])
    
    #question 13 and 16
    elif qtype(index) == 5:
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
    
        
switch_case(9, dataf)
