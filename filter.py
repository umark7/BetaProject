#filter given the index of the question, and a list of the target answers
def filter(index, target, df):
    #initialize dataframe to be edited
    df_subset = df 
    
    #if target isn't in row, drop the row
    for i in range(0,df.shape[0]):
        if df.iloc[i][index] not in target:
            df_subset = df_subset.drop(index = i)
    
    #reassign indexes so there are no skips in case of another itteration
    df_subset = df_subset.reset_index()
    
    #print(df_subset)
    return df_subset

filter1 = filter(10, ['Vascular Tissue', 'Space Robotics'], dataf)
#print(filter1)
filter2 = filter(9, ['Yes'], filter1)
print(filter2)
