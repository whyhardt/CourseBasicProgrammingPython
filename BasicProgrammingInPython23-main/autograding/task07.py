import os
import re
import shutil
import math

import numpy as np
import pandas as pd

from difflib import SequenceMatcher
from tqdm import tqdm

import numpy as np

def test_task01(code : str) -> int:
    '''Give one base point due to mistake erasing initial line, then one point per correct mutation.'''
    
    points = 1
    
    global arr
    global arr_reshaped
    global arr_transposed
    global max_index
    
    arr = None
    arr_reshaped = None
    arr_transposed = None
    max_index = None

    try:
        exec(code, globals())
    
    except Exception as e:
        print(e)

    try:
        if all(np.isclose(arr_reshaped, arr.reshape(2, 5)).reshape(-1)) and arr_reshaped.shape == (2, 5):
            points += 1
    
    except Exception as e:
        print(e)
            
    try:
        if all(np.isclose(arr_transposed, arr_reshaped.T).reshape(-1)) and arr_reshaped.T.shape == arr_transposed.shape:
            points += 1
    
    except Exception as e:
        print(e)
            
    try:
        if all(np.isclose(max_index, np.argmax(arr_transposed)).reshape(-1)):
            points += 1
    
    except Exception as e:
        print(e)
            
    return points

def test_task02(code : str) -> int:
    '''One point for a random valued numerical array.
    One point for a split into a positive and negative array.
    One point for getting the std of the arrays correctly.
    One point for a correct sdr in the end.'''
    
    points = 0
    
    global arr1
    global positive_array
    global negative_array
    global positive_std_dev
    global negative_std_dev
    global sdr
    
    arr1 = None
    positive_array = None
    negative_array = None
    positive_std_dev = None
    negative_std_dev = None
    sdr = None
    
    try:
        exec(code, globals())
    
    except Exception as e:
        print(e)
    
    try:
        if arr1.shape[0] == 100 and arr1.dtype in ['int64','int32','float64','float32'] and 'np.random' in code:
            points += 1
            print("Cond A")

    except Exception as e:
        print(e)
        
    try:
        if type(positive_array) != type(None) and type(negative_array) != type(None):
            if all(np.isclose(positive_array,arr1[arr1 > 0]).reshape(-1)) and all(np.isclose(negative_array,arr1[arr1 < 0]).reshape(-1)):
                points += 1
                print("Cond B")
                
    except Exception as e:
        print(e)
            
    try:
        if positive_std_dev != None and negative_std_dev != None:
            if all(np.isclose(positive_std_dev,np.std(positive_array)).reshape(-1)) and all(np.isclose(negative_std_dev,np.std(negative_array)).reshape(-1)):
                points += 1
                print("Cond C")
                
    except Exception as e:
        print(e)
            
    try:
        if sdr != None:
            if all(np.isclose(sdr,positive_std_dev / negative_std_dev).reshape(-1)):
                points += 1
                print("Cond D")
                
    except Exception as e:
        print(e)
    
    return points

def test_task03(code : str) -> int:
    '''One point for each correct subtask and one point for a correct total task.'''
    
    points = 0
    
    subtasks = code.split('# Replace the non-diagonal elements with random integers\n')[0]
    final = code.split('# Replace the non-diagonal elements with random integers\n')[1]
    
    global identity_matrix
    global random_integers
    
    identity_matrix = None
    random_integers = None
    
    try:
        exec(subtasks, globals())
    
    except Exception as e:
        print(e)
        
    try:
        if all(np.isclose(identity_matrix,identity_matrix).reshape(-1)):
            points += 1
                
    except Exception as e:
        print(e)
        
    try:
        if all(np.isclose(random_integers,random_integers).reshape(-1)):
            points += 1
                
    except Exception as e:
        print(e)
        
    try:
        exec(final, globals())
    
    except Exception as e:
        print(e)
    
    try:
        test = np.zeros((5,5))
        test[~np.eye(5, dtype=bool)] = random_integers[~np.eye(5, dtype=bool)]
        
        if all(np.isclose(identity_matrix,test).reshape(-1)):
            points += 1
                
    except Exception as e:
        print(e)
    
    return points

def test_task04(code : str) -> int:
    '''Two points, one for difference and one for distance being correct arrays.'''
    
    points = 0
    
    global arr1
    global arr2
    global difference
    global distance
    
    arr1 = None
    arr2 = None
    difference = None
    distance = None
    
    try:
        exec(code,globals())
    
    except Exception as e:
        print(e)
    
    try:
        if all(np.isclose(difference,arr1 - arr2).reshape(-1)):
            points += 1
                
    except Exception as e:
        print(e)
        
    try:
        if all(np.isclose(distance,np.linalg.norm(arr1 - arr2)).reshape(-1)):
            points += 1
                
    except Exception as e:
        print(e)
    
    return points

def test_task05(code : str) -> int:
    '''Two points for cumsum. Two points for argmax.'''
    
    points = 0
    
    global arr
    global cumulative_sum
    global threshold
    global index
    
    arr = None
    cumulative_sum = None
    threshold = None
    index = None
    
    try:
        exec(code,globals())
    
    except Exception as e:
        print(e)
        
    try:
        # print(code,'\n')
        # print(cumulative_sum, arr)
        # print(np.isclose(cumulative_sum,np.cumsum(arr)).reshape(-1))
        if all(np.isclose(cumulative_sum,np.cumsum(arr)).reshape(-1)):
            points += 2
    
    except Exception as e:
        print(e)
        
    try:
        if all(np.isclose(index,np.argmax(cumulative_sum > threshold)).reshape(-1)) and threshold == 100:
            points += 2
    
    except Exception as e:
        print(e)
    
    return points

def test_task06(code : str) -> int:
    '''One point for a correct array generated with shape and values. One point each for correct determinant, inverse and identity matrix for a maximum of two additional points.'''
    
    points = 0
    
    global arr
    global determinant
    global inverse
    global identity
    
    arr = None
    determinant = None
    inverse = None
    identity = None
    
    try:
        exec(code,globals())
    
    except Exception as e:
        print(e)
    
    try:
        #we are lenient here and do not check if 9 is included in the interval
        if arr.shape == (2,2) and np.max(arr) < 10 and np.min(arr) >= 1:
            points += 1
    
    except Exception as e:
        print(e)
    
    try:
        if all(np.isclose(determinant,np.linalg.det(arr)).reshape(-1)):
            points += 1
    
    except Exception as e:
        print(e)
        
    try:
        if all(np.isclose(inverse,np.linalg.inv(arr)).reshape(-1)):
            points += 1
    
    except Exception as e:
        print(e)
        
    try:
        if all(np.isclose(identity,np.dot(arr, inverse)).reshape(-1)):
            points += 1
    
    except Exception as e:
        print(e)
    
    
    points = 3 if points >= 3 else points
    
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
        active_code_task = re.search(r'(Task 1 - Array Manipulation \([\w\d]{1} points\))([\W\w]+)(Task 2 - Standart Deviation Ratio \(SDR\) \([\w\d]{1} points\))',content)[2]
        points += [test_task01(active_code_task)]
    
    except Exception as e:
        print(e)
        points += [0]
        
    print('Grading task02:')
    try:
        active_code_task = re.search(r'(Task 2 - Standart Deviation Ratio \(SDR\) \([\w\d]{1} points\))([\W\w]+)(Task 3 - Identity Matrix \([\w\d]{1} points\))',content)[2]
        points += [test_task02(active_code_task)]
    
    except Exception as e:
        print(e)
        points += [0]
        
    print('Grading task03:')
    try:
        active_code_task = re.search(r'(Task 3 - Identity Matrix \([\w\d]{1} points\))([\W\w]+)(Task 4 - Calculate the Euclidean distance between two arrays \([\w\d]{1} points\))',content)[2]
        points += [test_task03(active_code_task)]
    
    except Exception as e:
        print(e)
        points += [0]
        
    print('Grading task04:')
    try:
        active_code_task = re.search(r'(Task 4 - Calculate the Euclidean distance between two arrays \([\w\d]{1} points\))([\W\w]+)(Task 5 - Find the Point of Exceeding a Cumulative Sum Threshold \([\w\d]{1} points\))',content)[2]
        points += [test_task04(active_code_task)]
    
    except Exception as e:
        print(e)
        points += [0]
        
    print('Grading task05:')
    try:
        active_code_task = re.search(r'(Task 5 - Find the Point of Exceeding a Cumulative Sum Threshold \([\w\d]{1} points\))([\W\w]+)(Task 6 - Performing Linear Algebra Operations \([\w\d]{1} points\))',content)[2]
        points += [test_task05(active_code_task)]
    
    except Exception as e:
        print(e)
        points += [0]
        
    print('Grading task06:')
    try:
        active_code_task = re.search(r'(Task 6 - Performing Linear Algebra Operations \([\w\d]{1} points\))([\W\w]+)',content)[2]
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
    origin_task = 'task07'
    
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
                appendix = pd.DataFrame([[path, name, rz, points[0], points[1], points[2], points[3], points[4], points[5], int(np.sum(points)), int(np.sum(points))/20]], columns=columns)
                df = pd.concat([df, appendix], axis=0)
        
        else:
            print(f'Failed autograding validation for task {path}.')
            shutil.move(path, f"./submissions/{origin_task}/manual/"+path[path.find('submission_'):])
    
    df.to_csv(f'./autograding/{origin_task}.csv',index=False)

if __name__ == "__main__":
    main()