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
    '''Two points for a fully correct function.'''
    
    points = 0
    
    grades = [
        ("Leo", 87, 98, 89, 90),
        ("Fiona", 85, 90, 87, 96),
        ("Mark", 89, 87, 98, 90),
        ("Marie", 85, 91, 89, 91)
    ]
    
    averages = [np.mean([87, 98, 89, 90]),np.mean([85, 90, 87, 96]),np.mean([89, 87, 98, 90]),np.mean([85, 91, 89, 91])]
    
    global calculate_average
    
    def calculate_average(smth):
        return None
    
    try:
        exec(code,globals())
    
    except Exception as e:
        print(e)
        
    try:
        wrong = False
        for i, grade in enumerate(grades):
            avg_grade = calculate_average(grade)
        
            #break if None
            if avg_grade == None:
                wrong = True
        
            #break if not correct
            if not np.isclose(avg_grade,averages[i]):
                wrong = True
            
            #if no break, add one point
            
        points = 2 if not wrong else 0
            
    except Exception as e:
        print(e)
    
    return points

def test_task03(code : str) -> int:
    '''Half a point for each function correctly implemented, rounded down.'''
    
    points = 0
    
    global union
    global intersection
    global difference
    global symmetric_difference
    
    def union(a, b):
        return None
    
    def intersection(a, b):
        return None
    
    def difference(a, b):
        return None
    
    def symmetric_difference(a, b):
        return None

    def intersection(set1, set2):
        return set1.intersection(set2)

    def difference(set1, set2):
        return set1.difference(set2)

    def symmetric_difference(set1, set2):
        return set1.symmetric_difference(set2)
    
    try:
        exec(code,globals())
    
    except Exception as e:
        print(e)
        
    #try functions
    try:
        if union({1,2,3},{4,5,6}) == {1,2,3}.union({4,5,6}) and union({'a',7,4.93,-9},{'b',8,-1,-2,'c'}) == {'a',7,4.93,-9}.union({'b',8,-1,-2,'c'}):
            points += 0.5
    
    except Exception as e:
        print(e)
        
    try:
        if intersection({1,2,3},{3,4,5}) == {1,2,3}.intersection({3,4,5}) and intersection({'a',7,4.93,-9},{'b',8,-1,-2,'c'}) == {'a',7,4.93,-9}.intersection({'b',8,-1,-2,'c'}):
            points += 0.5
    
    except Exception as e:
        print(e)
        
    try:
        if difference({1,2,3},{2,3,4}) == {1,2,3}.difference({2,3,4}) and difference({'a',7,4.93,-9},{'b',8,-1,-2,'c'}) == {'a',7,4.93,-9}.difference({'b',8,-1,-2,'c'}):
            points += 0.5
    
    except Exception as e:
        print(e)
        
    try:
        if symmetric_difference({1,2,3},{2,3,4}) == {1,2,3}.symmetric_difference({2,3,4}) and symmetric_difference({'a',7,4.93,-9},{'b',8,-1,-2,'c'}) == {'a',7,4.93,-9}.symmetric_difference({'b',8,-1,-2,'c'}):
            points += 0.5
    
    except Exception as e:
        print(e)
    
    return int(points)

def test_task04(code : str) -> int:
    '''GRADING'''
    
    points = 0
    
    #add exec
    
    #add casetests
    
    return points

def test_task05(code : str) -> int:
    '''GRADING'''
    
    points = 0
    
    #add exec
    
    #add casetests
    
    return points

def test_task06(code : str) -> int:
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
        active_code_task = re.search(r'(Task 2 -  Student Grades  \(2 points\))([\W\w]+)(Task 3 - Set Operations Calculators   \(2 points\))',content)[2]
        active_code_task = "".join([line+'\n' for line in active_code_task.split('\n') if not 'input' in line])
        points += [test_task02(active_code_task)]
    
    except Exception as e:
        print(e)
        points += [0]
        
    print('Grading task03:')
    try:
        active_code_task = re.search(r'(Task 3 - Set Operations Calculators   \(2 points\))([\W\w]+)(Task 4 - Unique Elements Counter   \(3 points\))',content)[2]
        active_code_task = "".join([line+'\n' for line in active_code_task.split('\n') if not 'input' in line])
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
        
    print('Grading task05:')
    try:
        active_code_task = "" #parse regex
        points += [test_task05(active_code_task)]
    
    except Exception as e:
        print(e)
        points += [0]
        
    print('Grading task06:')
    try:
        active_code_task = "" #parse regex
        points += [test_task06(active_code_task)]
    
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
    origin_task = 'task06'
    
    #move manual grading task back to auto for new attempt
    for path in [f"./submissions/{origin_task}/manual/"+path for path in os.listdir(f"./submissions/{origin_task}/manual/") if path[-3:] == '.py']:
        shutil.move(path, "./submissions/task01/auto/"+path[path.find('submission_'):])
    
    columns = ["Path","Student","Student_rz","Task01","Task02","Task03","Task04","Task05","Task06","Total","Percentage"]
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
                appendix = pd.DataFrame([[path, name, rz, points[0], points[1], points[2], points[3], points[4], points[5], sum(points), sum(points)/20]], columns=columns)
                df = pd.concat([df, appendix], axis=0)
        
        else:
            print(f'Failed autograding validation for task {path}.')
            shutil.move(path, f"./submissions/{origin_task}/manual/"+path[path.find('submission_'):])
    
    df.to_csv(f'./autograding/{origin_task}.csv',index=False)

if __name__ == "__main__":
    main()