#this is just to specify which columns to use. Its kinda wordy but gets the job done
cols = []
for i in range(9,129):
    cols.append(i)

#For now just download to your computer and use that pathway or figure out how to download from google sheets.
dataf = pd.read_csv(r'C:\users\camih\documents\NASA_Centennial_Challenges_Survey.csv', skiprows = [0,1], header = None, usecols = cols) 
questions = pd.read_csv(r'C:\users\camih\documents\NASA_Centennial_Challenges_Survey.csv', nrows=2, header = None, usecols = cols)
pd.set_option("display.max_rows", None, "display.max_columns", None)
questions
dataf
