import numpy as np
import pandas as pd

import re

def retrieve_tasks(task_numbers=[1,2,3,4,5,6,7,8]):
    sheet_names = ['task0'+str(num) for num in task_numbers]
    
    dataframes = [pd.read_excel('./autograding/final_grades.xlsx',sheet_name=name,index_col=None) for name in sheet_names]
    
    return dataframes

def get_student_name_dict(address_list, dataframes):
    add2name = dict()
    
    for address in address_list:
        for i, df in enumerate(dataframes):
            for j, name in enumerate(df['Student']):
                if df['Student_rz'].iloc[j] == address:
                    if address in add2name.keys():
                        if not add2name[address] == name and not add2name[address].lower().replace(" ","") == name.lower().replace(" ",""):
                            raise ValueError(f'A mail address (key) has multiple names (values), found in sheet_0{i+1} at address:{address}.')
                        
                    else:
                        add2name[address] = name
                    
    return add2name

def get_address_list(dataframes):
    total_unique = list(set([sublst for lst in [df['Student_rz'] for df in dataframes] for sublst in lst]))
    
    if 'example' in "".join(total_unique):
        raise ValueError('Please remove remaining missing mail addresses e.g. example.name@uos.de from the lists.')
        
    if len(total_unique) != len(list(set([re.sub('(@uni-sonabrueck)|(@uni-sonabrück)','@uos',un) for un in total_unique]))):
        raise ValueError('Please ensure uniformity of mail suffixes uos/uni-osnabrueck for each student.')
    
    total_unique.sort()
    
    return total_unique
    
def get_taskarray(address, dataframes):
    arr = []
    empty_task = {
        0 : [0]*4,
        1 : [0]*4,
        2 : [0]*4,
        3 : [0]*5,
        4 : [0]*4,
        5 : [0]*6,
        6 : [0]*6,
        7 : [0]*4,
    }

    for i, df in enumerate(dataframes):
        filtered = df.where(df['Student_rz'] == address).dropna()
        filtered = filtered.drop(["Path","Student","Student_rz"],axis=1)

        if len(filtered) > 1:
            raise ValueError(f'Please remove duplicate for student: {address} on sheet_0{i+1}')

        if len(filtered) == 0:
            arr.append(empty_task[i])

        else:
            arr.append([int(pts) for pts in list(filtered.iloc[0])])

    return arr

def evaluate(arr):
    passed = (np.sum(np.array([np.sum(row) for row in arr]) >= 10) >= 3)
    points = int(sum([sum(row) for row in arr]))
    percentage = round(float(points/(8*20)*100),4)
    
    return passed, points, percentage

def generate_mail(student, taskarray, passed, points, percentage):
    '''ADD'''
    
    mailstring = (
        f'Dear {student},\n'
        f'\n'
        f'in this generated email you will find your results from the assignments in Basic Programming in Python.\n'
        f'Firstly, in this mail we will inform you if you are allowed to take the exam and give you a list of your points for each assignment.\n'
        f'Hopefully this list of points is also helpful for you to practice for the upcoming exam.'
        f'Here is the overview of all the points you got over the eight tasks:\n'
        f'\n'
    )
    
    for i, row in enumerate(taskarray):
        mailstring += (f'Task {i+1}:   {str([pt for pt in row]).replace(",",",  ")}  for a total of {int(np.sum(row))}/20 points over {len(row)} tasks => {"passed" if (int(np.sum(row)) >= 10) else "failed"}\n')
    
    mailstring += (
        f'\n'
        f'Your total points therefore are {points}/{int(20*8)} points, making {percentage}% percent.\n'
    )
    
    if passed:
        mailstring += (
            f'Since you passed three or more assignments, this means you are allowed to take the exam.\n'
            f'We wish you best of luck and good health and energy for your practice.\n'
        )
    
    else:
        mailstring += (
            f'Sadly, since you did not pass three or more assignments, this means you are not allowed to take the exam.\n'
            f'We already lowered the admission boundary to only three passed exercises and apologize you will not be able to write the exam nevertheless.\n'
            f'Hopefully, you still take away from this course as much as possible and will attempt to do it gain next year.\n'
        )
    
    mailstring += (
        f'\n'
        f'In case of further questions you cannot answer for yourself reply to this email.\n'
        f'\n'
        f'Best,\n'
        f'The Basic Programming in Python Team'
    )
    
    topic = f'Basic Programming in Python Exam Admission \[{"PASSED" if passed else "FAILED"}\]'
    
    return topic, mailstring

def main():
    dataframes = retrieve_tasks()
    
    columns=["Student","Address","Passed","Points","Percentage","Topic","Mailstring"]
    maildoc = pd.DataFrame(columns=columns)
    
    addresses = get_address_list(dataframes)
    add2name = get_student_name_dict(addresses, dataframes)
    
    print(", ".join(list(add2name.keys())))
    
    for address in addresses:
        print(f'Generating mail and data for student {add2name[address]}:')
        taskarray = get_taskarray(address, dataframes)
        
        passed, points, percentage = evaluate(taskarray)
        
        topic, mailstring = generate_mail(add2name[address], taskarray, passed, points, percentage)
        
        aux_address = re.sub(r'(@[\w\W]+)',"@uni-osnabrueck.de",address)
        
        print(aux_address)
        
        maildoc = pd.concat([maildoc,pd.DataFrame([[add2name[address],aux_address,"PASSED" if passed else "FAILED",points,percentage,topic,mailstring]],columns=columns)],axis=0)
        
    maildoc.to_excel('./autograding/maildoc.xlsx',index=None)

if __name__ == "__main__":
    main()