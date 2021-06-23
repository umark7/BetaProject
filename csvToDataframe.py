import pandas as pd

#rename the headers
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

#need to find a way to import file not from my computer
data = pd.read_csv (r'C:\users\camih\documents\NASA_Centennial_Challenges_Survey.csv', skiprows = [0,1], header = None, names = headers) 

#this is just an array of the questions. Still need to take out blank spaces
questions = pd.read_csv(r'C:\users\camih\documents\NASA_Centennial_Challenges_Survey.csv', nrows=0)
pd.set_option("display.max_rows", None, "display.max_columns", None)

#display data
data

#q_cols[1] is the amount of columns dedicated to question 1
q_cols = [0,1,2,1,2,1,1,1,1,1,1,1,1,16,1,16,16,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,6,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,10]
