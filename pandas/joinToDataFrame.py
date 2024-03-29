import pandas as pd

student_data1 = pd.DataFrame({
        'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
         'name': ['Dam', 'Rinne', 'Bruse', 'Edword', 'Morni'], 
        'marks': [200, 210, 190, 222, 199]})

student_data2 = pd.DataFrame({
        'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
        'name': ['Scarl', 'Carla', 'Dante', 'Kaiser', 'Madeeha'], 
        'marks': [201, 200, 198, 219, 201]})

result_data = pd.concat([student_data1, student_data2])
print(result_data)