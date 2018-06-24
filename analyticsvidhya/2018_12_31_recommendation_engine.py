import os
import pandas as pd
from directory_utils import get_data_directory

os.chdir(get_data_directory() + "/2018_12_31_recommendation_engine/")

# Problem Data
problem_data_initial = pd.read_csv('problem_data.csv')
problem_data_temp = pd.concat([pd.Series(str(row['problem_id']) + '|' + str(row['level_type']) + '|' + str(row['points']), str(row['tags']).split(',')) for _, row in problem_data_initial.iterrows()]).reset_index()
problem_data_final= pd.DataFrame(list(problem_data_temp[0].str.split('|')), columns = ['problem_id', 'level_type', 'points'])
problem_data_final['tag']=problem_data_temp['index']
output_file = './output/2018_12_31_recommendation_engine--processed_problem_data_divided_by_tags.csv'
try:
    os.makedirs(output_file.rsplit('/',1)[0])
except OSError:
    pass

problem_data_final.to_csv(output_file)


train_submissions = pd.read_csv('train_submissions.csv')


user_data = pd.read_csv('user_data.csv')









# Train Submission Data
# def bucketing(num):
#     if num ==1:
#         return 1
#     elif 2<=num<=3:
#         return 2
#     elif 4<=num<=5:
#         return 3
#     elif 6<=num<=7:
#         return 4
#     elif 8<=num<=9:
#         return 5
#     elif num>=10:
#         return 6
# train_submissions['attempts_range'] = train_submissions['attempts_range'].apply(bucketing)
# output_file = './output/2018_12_31_recommendation_engine--processed_train_submissions_data.csv'
# try:
#     os.makedirs(output_file.rsplit('/',1)[0])
# except OSError:
#     pass
# train_submissions.to_csv(output_file)















