import pandas as pd


host = "localhost"
username = "root"
password = "***"

students_df = pd.read_json('students.json')
students_df.birthday = pd.to_datetime(students_df.birthday)
students_reindexed = students_df.reindex(columns=['id', 'name', 'birthday', 'sex', 'room'])



