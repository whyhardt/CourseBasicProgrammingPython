import os
import re
import shutil
import math

import numpy as np
import pandas as pd

from difflib import SequenceMatcher
from tqdm import tqdm

def test_task01(code : str) -> int:
    '''GRADING'''
    
    points = 0
    
    #add exec
    
    #add casetests
    
    return points

def test_task02(code : str) -> int:
    '''Six points, three per task divided into the following subtasks:
    Zero points if not the right for or while loop, else three points for the correct result.
    Checking cases with 0 points is required here due to some writing of multiple loops causing errors'''
    
    points = 0
    
    
    #splits into the two tasks and removes comments
    filtered_code = "".join([line+'\n' for line in code.split('\n') if (not line.startswith('#')) or ("Snake trivia" in line)])
    filtered_code = filtered_code.split('Snake trivia')
    
    #splits into preexisting and added loop
    filtered_code[0] = re.split(r'print\(result\)',filtered_code[0])
    filtered_code[1] = re.split(r'print\(result\)',filtered_code[1])
    
    #filters out only added loop
    filtered_code[0] = filtered_code[0][1]
    filtered_code[1] = filtered_code[1][1]
    
    # print(filtered_code[0])
    # print(filtered_code[1])
    
    global result
    result = []
    
    if 'while' in filtered_code[0] and not 'results=\[2,4,6,8,10,12,14,16,18,20\]' in filtered_code[1].replace(' ',''):
        try:
            exec(filtered_code[0],globals())
            if result == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]:
                points += 3
                
        except Exception as e:
            print(e)
    
    if 'for' in filtered_code[1] and not 'results=\[ThePythonidaecommonlyknownas' in filtered_code[1].replace(',','').replace("'","").replace(' ',''):
        try:
            exec(filtered_code[1],globals())
            if "".join(result).replace(',','').replace('.','').replace('-','') == 'PythonidaenonvenomousAustraliacurrentlyrecognizednaturallynonvenomousconstrictsuffocateconsumptiontypicallyconstricteffectivelysuffocatingswallowingrattlesnakereleasesenvenomationconsumedCollectivelywelldocumentedconstrictorsnonvenomousincludingkingsnakes':
                points += 3
                
        except Exception as e:
            print(e)
    
    return points

def test_task03(code : str) -> int:
    '''One point per correct solution per subtask (five tasks).'''
    
    points = 0
    
    #split into subtasks
    filtered_code = re.split(r'[pP]art \d[\s]*',code)[1:]
    
    #add comment marker which got shifted to beginning again
    for i, subtask in enumerate(filtered_code):
        filtered_code[i] = '#'+subtask
    
    #remove unecessary stuff from subtasks
    for i, subtask in enumerate(filtered_code):
        filtered_code[i] = "".join([line+'\n' for line in subtask.split('\n') if not line.startswith('#')])
    
    global names
    global alphabet
    global idx
    global n
    global removed
    
    names = []
    idx = None
    removed = None
    n = 0
    alphabet = []
    
    try:
        if not 'names=\[DaisyDuck,' in filtered_code[0].replace(' ','').replace('\'','').replace('\"',''):
            exec(filtered_code[0],globals())
            if names == ['Daisy Duck', 'Donald Duck', 'Goofy', 'Mickey Mouse', 'Minnie Mouse', 'Pete', 'Pluto', 'Scrooge McDuck', 'Tick', 'Track', 'Trick']:
                points += 1
                
    except Exception as e:
        print(e)
    
    try:
        if '.index' in filtered_code[1] and not filtered_code[1].replace(' ','').count('idx=2') > 1:
            exec(filtered_code[1],globals())
            if idx == 2:
                points += 1
    
    except Exception as e:
        print(e)
    
    try:
        if 'alphabet.pop(' in filtered_code[2]:
            exec(filtered_code[2],globals())
            #we allow the other end due to miscommunication in an error on the sheet
            if removed == 'A' or removed == 'H':
                points += 1
    
    except Exception as e:
        print(e)
    
    try:
        if not 'alphabet=\[A,B,C,D,E,F,G,H\]' in filtered_code[4].replace(' ','').replace('\'','').replace('\"',''):
            exec(filtered_code[3],globals())
            if alphabet == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
                points += 1
    
    except Exception as e:
        print(e)
    
    try:
        if not 'n=15' in filtered_code[4].replace(' ','').replace('\'','').replace('\"',''):
            exec(filtered_code[4],globals())
            if n == 15:
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
        active_code_task = "" #parse regex
        points += [test_task01(active_code_task)]
    
    except Exception as e:
        print(e)
        points += [0]
        
    print('Grading task02:')
    try:
        active_code_task = re.search(r'(Task 2 For and While conversion \(6 points\))([\w\W]+)(Task 3 List methods \(5 points\))',content)[2]
        points += [test_task02(active_code_task)]
    
    except Exception as e:
        print(e)
        points += [0]
        
    print('Grading task03:')
    try:
        active_code_task = re.search(r'(Task 3 List methods \(5 points\))([\w\W]+)(Task 4)',content)[2]
        points += [test_task03(active_code_task)]
    
    except Exception as e:
        print(e)
        points += [0]
        
    print('Grading task04:')
    try:
        active_code_task = "" #parse regex
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
    origin_task = 'task03'
    
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