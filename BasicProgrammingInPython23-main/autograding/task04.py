import os
import re
import shutil
import math
from math import pi

import numpy as np
import pandas as pd

from difflib import SequenceMatcher
from tqdm import tqdm

def test_task01(code : str) -> int:
    '''One point per working function. Working means full requested functionality. Overwriting the sum function or using it gives zero points.'''
    
    points = 0
    
    sum_part = re.search(r'(def get_sum)([\w\W]+)(Area of a circle)',code)[0]
    circle_part = re.search(r'(def circle_area)([\w\W]+)',code)[0]
    
    global get_sum
    
    #we overwrite to make sure it really fails and no previous version was kept
    def get_sum(a,b,c,d):
        return None
    
    #exclude sum overwrite cases and sum function usage
    if not 'sum=' in sum_part.lower().replace(' ','') and not 'sum\(\[a,b,c,d\]\)' in sum_part.lower().replace(' ',''):
        try:
            exec(sum_part,globals())
        
        except Exception as e:
            print('Sum def:',e)
    
    global circle_area
    
    #we overwrite to make sure it really fails and no previous version was kept
    def circle_area(radius):
        return None
    
    try:
        exec(circle_part,globals())
        
    except Exception as e:
        print('circle def:',e)
    
    try:
        if get_sum(1,2,3,4) != None:
            if get_sum(1,2,3,4) == 10 and np.isclose(get_sum(1.23,9.27,8,0.328),sum([1.23,9.27,8,0.328])) and np.isclose(get_sum(-82,2.78,-7.82,3),sum([-82,2.78,-7.82,3])):
                points += 1
            
    except Exception as e:
        print('Sum test:',e)
    
    try:
        if circle_area(7) != None:
            if np.isclose(circle_area(7),pi*7**2) and np.isclose(circle_area(4.532),pi*4.532**2):
                points += 1
            
    except Exception as e:
        print('circle test:',e)
    
    return points

def test_task02(code : str) -> int:
    '''One point if input and output types work, two points for correct functionality.'''
    
    points = 0
    
    function = re.search(r'(def intersection)([\w\W]+)',code)[0]
    
    global intersection
    
    #we overwrite to make sure it really fails and no previous version was kept
    def intersection(list_a, list_b):
        return None
    
    try:
        exec(function,globals())
        
    except Exception as e:
        print(e)
    
    #one point if input and output works as intended
    try:
        if type(intersection([1,2,3,4,5,6],[-2,-1,0,1,2])) == list and type(intersection(['a','c'],[1,3.4])) == list:
            points += 1
            
    except Exception as e:
        print(e)
    
    #two points if working correctly
    try:
        if set(intersection([1,2,3,4,5,6],[-2,-1,0,1,2])) == set([1,2]) and set(intersection(['a','b','c'],['d','e','f'])) == set([]) and set(intersection(['a',2,'c',5],['c',2,'h',-2])) == set(['c',2]):
            points += 2
            
    except Exception as e:
        print(e)
    
    return points

def test_task03(code : str) -> int:
    '''One point for typecoding correctly, one point each for handling it for either lower or capitalized cases, last point for no changes if no vowels.'''
    
    points = 0
    
    function = re.search(r'(def remove_vowels)([\w\W]+)',code)[0]
    
    try:
        function = function[:function.find('my_str=input')]
    
    except Exception as e:
        print(e)
        
    function = "".join([line+'\n' for line in function.split('\n') if not 'input' in line and not 'remove_vowels\(my_str' in line])
    
    global remove_vowels
    
    #we overwrite to make sure it really fails and no previous version was kept
    def remove_vowels(string):
            return None
    
    try:
        exec(function,globals())
        
    except Exception as e:
        print(e)
        
    try:
        if type(remove_vowels('abc')) == str:
            points += 1
            
    except Exception as e:
        print(e)
        
    try:
        if remove_vowels('abc12def34') == 'bc12df34':
            points += 1
            
    except Exception as e:
        print(e)
        
    try:
        if remove_vowels('Abc12dEf34') == 'bc12df34':
            points += 1
            
    except Exception as e:
        print(e)
        
    try:
        if remove_vowels('bhq?-12') == 'bhq?-12':
            points += 1
            
    except Exception as e:
        print(e)
    
    return points

def test_task04(code : str) -> int:
    '''One point for typecoding, two points for five correct primes, one point for returning False for 0 and 1.'''
    
    points = 0
    
    function = re.search(r'(def is_prime)([\w\W]+)',code)[0]
    
    global is_prime
    
    #we overwrite to make sure it really fails and no previous version was kept
    def is_prime(num):
        return None
    
    try:
        exec(function,globals())
        
    except Exception as e:
        print(e)
    
    try:
        if type(is_prime(5)) == bool:
            points += 1
            
    except Exception as e:
        print(e)
        
    try:
        if is_prime(2) == True and is_prime(7) == True and is_prime(41) == True and is_prime(4) == False and is_prime(69) == False:
            points += 2
            
    except Exception as e:
        print(e)
        
    try:
        if is_prime(1) == False and is_prime(0) == False:
            points += 1
            
    except Exception as e:
        print(e)
        
    return points

def test_task05(code : str) -> int:
    '''Grading scheme for each function:
    Fibonacci: One point for base cases n=1 -> 0 and n=2 -> 1 and two points for 5 correct numbers.
    GCD: One point for base case b=0, one point for 5 correct numbers.'''
    
    points = 0
    
    fib_part = re.search(r'(def fibonacci)([\w\W]+)',code.split('Greatest common divisor')[0])[0]
    fib_part = fib_part[:fib_part.find('n = int(input(')-1]
    
    gcd_part = re.search(r'(def gcd)([\w\W]+)',code.split('Greatest common divisor')[1])[0]
    gcd_part = gcd_part[:gcd_part.find('a = int(input(\"Enter first number: \"))')-1]
    
    global fibonacci
    global gcd
    
    def fibonacci(n):
        return None
    
    def gcd(a,b):
        return None
    
    try:
        exec(fib_part,globals())
        
    except Exception as e:
        print(e)
        
    try:
        exec(gcd_part,globals())
        
    except Exception as e:
        print(e)
    
    try:
        if fibonacci(2) == 1 and fibonacci(1) == 0:
            points += 1
            
    except Exception as e:
        print(e)
        
    try:
        if fibonacci(3) == 1 and fibonacci(4) == 2 and fibonacci(5) == 3 and fibonacci(10) == 34 and fibonacci(33) == 2178309:
            points += 2
            
    except Exception as e:
        print(e)
        
    try:
        if gcd(10,0) == 10 and gcd(0,17) == 17:
            points += 1
            
    except Exception as e:
        print(e)
        
    try:
        if gcd(28,14) == 14 and gcd(928,172) == 4 and gcd(728,102) == 2 and gcd(82,9) == 1 and gcd(9,3) == 3:
            points += 2
            
    except Exception as e:
        print(e)
    
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
        active_code_task = re.search(r'(Task 1 Simple mathematical functions \(2 points\))([\w\W]+)(Task 2 Recall of  loops and lists \(3 poins\))',content)[2]
        points += [test_task01(active_code_task)]
    
    except Exception as e:
        print(e)
        points += [0]
        
    print('Grading task02:')
    try:
        active_code_task = re.search(r'(Task 2 Recall of  loops and lists \(3 poins\))([\w\W]+)(Task 3 Vowel removal \(4 points\))',content)[2]
        points += [test_task02(active_code_task)]
    
    except Exception as e:
        print(e)
        points += [0]
        
    print('Grading task03:')
    try:
        active_code_task = re.search(r'(Task 3 Vowel removal \(4 points\))([\w\W]+)(Task 4 Prime Number Checker \(5 points\))',content)[2]
        points += [test_task03(active_code_task)]
    
    except Exception as e:
        print(e)
        points += [0]
        
    print('Grading task04:')
    try:
        active_code_task = re.search(r'(Task 4 Prime Number Checker \(5 points\))([\w\W]+)(Task 5 Recursion \(6 points\))',content)[2]
        points += [test_task04(active_code_task)]
    
    except Exception as e:
        print(e)
        points += [0]
        
    print('Grading task05:')
    try:
        active_code_task = re.search(r'(Task 5 Recursion \(6 points\))([\w\W]+)',content)[2]
        points += [test_task05(active_code_task)]
    
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
    origin_task = 'task04'
    
    #move manual grading task back to auto for new attempt
    for path in [f"./submissions/{origin_task}/manual/"+path for path in os.listdir(f"./submissions/{origin_task}/manual/") if path[-3:] == '.py']:
        shutil.move(path, "./submissions/task01/auto/"+path[path.find('submission_'):])
    
    columns = ["Path","Student","Student_rz","Task01","Task02","Task03","Task04","Task05","Total","Percentage"]
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
                appendix = pd.DataFrame([[path, name, rz, points[0], points[1], points[2], points[3], points[4], sum(points), sum(points)/20]], columns=columns)
                df = pd.concat([df, appendix], axis=0)
        
        else:
            print(f'Failed autograding validation for task {path}.')
            shutil.move(path, f"./submissions/{origin_task}/manual/"+path[path.find('submission_'):])
    
    df.to_csv(f'./autograding/{origin_task}.csv',index=False)

if __name__ == "__main__":
    main()