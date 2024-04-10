import os
import re
import shutil
import math

import numpy as np
import pandas as pd

from difflib import SequenceMatcher
from tqdm import tqdm

def test_task01(code : str) -> int:
    '''One point for the plot, one point for the titles and labels iff temperatures shape and min max are ok.'''
    
    points = 0
    
    global temperature
    temperature = None
    
    try:
        numpystring = re.search(r'(np.random.\w+\()([\s\d\w\=,]+)(\))',code)[0]
        exec(f'temperature = {numpystring}',globals())
    
    except Exception as e:
        print(e)
    
    if re.search(r'(plt.title\([\'\"]{1}weeklytemperature[\'\"]{1}\))',code.lower().replace(" ","")) != None:
        if re.search(r'(plt.xlabel\([\'\"]{1}daysoftheweek[\'\"]{1}\))',code.lower().replace(" ","")) != None:
            if re.search(r'(plt.ylabel\([\'\"]{1}temperature\([\w\W]{1}c\)[\'\"]{1}\))',code.lower().replace(" ","")) != None:
                points += 1
    
    plotargs = re.search(r'(plt.plot\()([\w\s\d\'\",\=]+)(\))',code)[2]
    if plotargs != None:
        plotargs = plotargs.lower().replace(' ','').split(',')
        #we don't check purple since it is really hard to check exact color since it can be defined in too many ways
        if any(['color=' in arg for arg in plotargs]) and 'days' in plotargs and 'temperature' in plotargs:
            points += 1
    
    try:
        if not temperature.shape == (7,) or not np.max(temperature) <= 30 or not np.min(temperature) >= 20:
            points -= 1 if points > 1 else 0
    
    except Exception as e:
        print(e)
    
    return points

def test_task02(code : str) -> int:
    '''GRADING'''
    
    points = 0
    
    #add exec
    
    #add casetests
    
    return points

def test_task03(code : str) -> int:
    '''Gradin scheme is as follows:
    One point for each correct grades arrays (2/8).
    One points for correct subplot creation (3/8).
    One point for using "hist" (4/8).
    One point each for set_title, xlabel, ylabel per axis (6/8).
    One point each for legend and tight_layout (8/8). '''
    
    points = 0
    
    grades = re.findall(r'(np.random.normal\()([\s\w\d\=\'\",]+)(\))',code)
    grades = ["".join(grade) for grade in grades]
    
    subplots = re.search(r'(plt.subplots\()([\s\w\d\=\'\",\)\(]+)(\))',code)
    
    axes_1 = re.findall(r'(axes\[0\]\.)([\w\_]+)(\()',code)
    axes_2 = re.findall(r'(axes\[1\]\.)([\w\_]+)(\()',code)
    
    fig_parts = re.findall(r'(fig\.)([\w\_]+)(\()',code)
    
    try:
        nums = re.findall(r'\d+',grades[0])
        if int(nums[0]) == 70 and int(nums[1]) == 10 and int(nums[2]) == 100:
            points += 1
        
    except Exception as e:
        print(e)
        
    try:
        nums = re.findall(r'\d+',grades[0])
        if int(nums[0]) == 80 and int(nums[1]) == 8 and int(nums[2]) == 100:
            points += 1
        
    except Exception as e:
        print(e)
        
    try:
        if 'figsize' in subplots[1]:
            points += 1
        
    except Exception as e:
        print(e)
        
    try:
        if [elem[1] for elem in axes_1] == ['hist','set_title','set_xlabel','set_ylabel']:
            points += 2
        elif [elem[1] for elem in axes_1][1:] == ['hist','set_title','set_xlabel','set_ylabel'][1:]:
            points += 1
        
    except Exception as e:
        print(e)
        
    try:
        if [elem[1] for elem in axes_2] == ['hist','set_title','set_xlabel','set_ylabel']:
            points += 1
        
    except Exception as e:
        print(e)
        
    try:
        if fig_parts[0][1] == 'legend':
            points += 1
        
    except Exception as e:
        print(e)
        
    try:
        if fig_parts[1][1] == 'tight_layout':
            points += 1
        
    except Exception as e:
        print(e)
    
    return points

def test_task04(code : str) -> int:
    '''GRADING'''
    
    points = 0
    
    #add exec
    
    #add casetests
    
    return points
    
def validate_auto(path : str) -> bool:
    file = open(path,"r",encoding='utf-8')
    content = file.read()
    infostring = ""
    
    try:
        infostring = re.search(r'(name here)([\w\W]+)(Important)',content)[2]
        
    except Exception as e:
        print(e)
        file.close()
        return False
    
    name = re.search(r'([\w]+ [\w]+)',infostring)[0]
    rz = [elem for elem in re.findall(r'([\w \@\-.]+)',infostring) if '@' in elem][0]
    
    if name == "Example Name" or name == "" or rz == "example.name@uos.de" or rz == "" or 'example' in name.lower():
        file.close()
        return False
    
    file.close()
    return True

def process_script(path : str) -> tuple:
    '''
    ADD
    '''
    
    file = open(path,"r",encoding='utf-8')
    content = file.read()
    
    infostring = re.search(r'(name here)([\w\W]+)(Important)',content)[2]
    
    name = re.search(r'([\w]+ [\w]+)',infostring)[0]
    rz = [elem for elem in re.findall(r'([\w \@\-.]+)',infostring) if '@' in elem][0]
    
    points = []
    
    print(f'\nCorrecting script {path} for {name}:')
    
    print('Grading task01:')
    try:
        active_code_task = re.search(r'(Task 1 - Temperature Plot \(2 points\))([\w\W]+)(Task 2 - Steps Taken Analysis \(4 points\))',content)[2]
        points += [test_task01(active_code_task)]
    
    except Exception as e:
        print(e)
        points += [0]
        
    print('Grading task02:')
    try:
        active_code_task = re.search(r'(Task 2 - Steps Taken Analysis \(4 points\))([\w\W]+)(Task 3 - Math Exam Score Distribution \(8 points\))',content)[2]
        points += [test_task02(active_code_task)]
    
    except Exception as e:
        print(e)
        points += [0]
        
    print('Grading task03:')
    try:
        active_code_task = re.search(r'(Task 3 - Math Exam Score Distribution \(8 points\))([\w\W]+)(Task 4 - Stacked Bar Plot \(6 points\))',content)[2]
        points += [test_task03(active_code_task)]
    
    except Exception as e:
        print(e)
        points += [0]
        
    print('Grading task04:')
    try:
        active_code_task = re.search(r'(Task 4 - Stacked Bar Plot \(6 points\))([\w\W]+)',content)[2]
        points += [test_task04(active_code_task)]
    
    except Exception as e:
        print(e)
        points += [0]
    
    file.close()
    
    return name, rz, points

def duplicate_detector(paths, origin):
    '''Creates a list of similarity measures between scripts.'''
    df = pd.DataFrame(columns=['PathA','PathB', 'Similarity', 'Notebook similarity'])
    
    for i, path in tqdm(enumerate(paths),desc="Creating duplicate matrix:"):
        for j, check in enumerate(paths):
            if i != j and i < j:
                file_a, file_b = open(path,"r",encoding='utf-8'), open(check,"r",encoding='utf-8')
                
                text_a, text_b = file_a.read(), file_b.read()
                
                file_a.close()
                file_b.close()
                
                ratio = int(round(SequenceMatcher(None, text_a, text_b).ratio(),2)*10**2)
                
                file_c, file_d = open(re.sub('/auto/','/original/',re.sub(r'.py','.ipynb',path)),"r",encoding='utf-8'), open(re.sub('/auto/','/original/',re.sub(r'.py','.ipynb',check)),"r",encoding='utf-8')
                
                text_c, text_d = file_c.read(), file_d.read()
                
                file_c.close()
                file_d.close()
                
                celldata_sim = int(round(SequenceMatcher(None, text_c, text_d).ratio(),2)*10**2)
                                                                                               
                df = pd.concat([df, pd.DataFrame([[path, check, ratio, celldata_sim]],columns=df.columns)],axis=0)
    
    df.to_csv(f'./autograding/{origin}_similarity.csv',index=False)
    
def main():
    origin_task = 'task08'
    
    #move manual grading task back to auto for new attempt
    for path in [f"./submissions/{origin_task}/manual/"+path for path in os.listdir(f"./submissions/{origin_task}/manual/") if path[-3:] == '.py']:
        shutil.move(path, "./submissions/task01/auto/"+path[path.find('submission_'):])
    
    columns = ["Path","Student","Student_rz","Task01","Task02","Task03","Task04","Total","Percentage"]
    df = pd.DataFrame(columns=columns)
    
    script_paths = [
        f"./submissions/{origin_task}/auto/"+path for path in os.listdir(f"./submissions/{origin_task}/auto/") if path[-3:] == '.py'
    ]
    
    if not os.path.exists(f'./autograding/{origin_task}_similarity.csv'):
        duplicate_detector(script_paths, origin_task)
    
    for path in script_paths:
        if validate_auto(path):
            name, rz, points = process_script(path)
                    
            if name != None:
                appendix = pd.DataFrame([[path, name, rz, points[0], points[1], points[2], points[3], sum(points), sum(points)/20]], columns=columns)
                df = pd.concat([df, appendix], axis=0)
        
        else:
            print(f'Failed autograding validation for task {path}.')
            shutil.move(path, f"./submissions/{origin_task}/manual/"+path[path.find('submission_'):])
    
    df.to_csv(f'./autograding/{origin_task}.csv',index=False)

if __name__ == "__main__":
    main()