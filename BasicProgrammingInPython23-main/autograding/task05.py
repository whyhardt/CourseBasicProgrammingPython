import os
import re
import shutil
import math

import numpy as np
import pandas as pd

from difflib import SequenceMatcher
from tqdm import tqdm

from datetime import datetime, timedelta
from math import pi, sqrt

def test_task01(code : str) -> int:
    '''Grading scheme: One point if an instance was created.
    One point if the class contains all variables.
    Then one point per method which works correctly including init.'''
    
    points = 0
    
    class_part = "".join([line+'\n' for line in code.split('\n') if 'student=' not in line.lower().replace(" ","") and not 'print(' in line and not 'input' in line])
    
    global Student
    global student
    
    student = None
    
    class Student: 
        def __init__(self):
            self.att = None
            
    try:
        exec(class_part, globals())
    
    except Exception as e:
        print(e)
        
    #test for variables and init, both are tested together
    try:
        exec(f'student = Student(name=\"Marlon\",age={22},grade={1.0})',globals())
        points += 1
        if student != None:
            if student.name == 'Marlon' and student.age == 22 and student.grade == 1.0:
                points += 1
    
    except Exception as e:
        print(e)    
    
    try:
        exec(f'student = Student(name=\"Marlon\",age={22},grade={1.0})',globals())

        if student.get_name() == 'Marlon':
            points += 1
            
    except Exception as e:
        print(e)
        
    try:
        exec(f'student = Student(name=\"Marlon\",age={22},grade={1.0})',globals())

        if student.get_age() == 22:
            points += 1
    
    except Exception as e:
        print(e)
        
    try:
        exec(f'student = Student(name=\"Marlon\",age={22},grade={1.0})',globals())
        if student.get_grade() == 1.0:
            points += 1
    
    except Exception as e:
        print(e)
        
    if re.search(r'(student\s*=\s*Student\()([\w\'\"\s\,\.]+)(\))',code) != None:
        points += 1
            
    return points

def test_task02(code : str) -> int:
    '''1 point for a working class (meaning an instance with arguments can be created).
    4 points, one each per method correctly implemented.'''
    
    points = 0
    global BankAccount
    global account
    
    account = None
    
    class BankAccount: 
        def __init__(self):
            self.att = None
            
    try:
        exec(code, globals())
    
    except Exception as e:
        print(e)
    
    #test instance creation
    try:
        exec(f'account = BankAccount(account_number=\"IBAN 2394 3827 1729 3029\", balance={100})',globals())

        points += 1 #since init was confirmed to work
        
        if account.account_number == "IBAN 2394 3827 1729 3029" and account.balance == 100:
            points += 1
    
    except Exception as e:
        print(e)
        
    #test str method
    try:
        exec(f'account = BankAccount(account_number=\"IBAN 2394 3827 1729 3029\", balance={100})',globals())

        if str(account) == f'The account IBAN 2394 3827 1729 3029 has a balance of {100}.':
            points += 1
    
    except Exception as e:
        print(e)
        
    #test withdrawal method
    try:
        exec(f'account = BankAccount(account_number=\"IBAN 2394 3827 1729 3029\", balance={100})',globals())

        account.withdraw(50)
        
        if account.balance == 50:
            if 'insufficient' in str(account.withdraw(51)).lower():
                points += 1
    
    except Exception as e:
        print(e)
        
    try:
        exec(f'account = BankAccount(account_number=\"IBAN 2394 3827 1729 3029\", balance={100})',globals())

        account.deposit(50)
        
        if account.balance == 150:
            points += 1
    
    except Exception as e:
        print(e)
    
    return points

def test_task03(code : str) -> int:
    '''One point for rectangle.perimeter().
    One point for rectangle.area().
    One point for circle.diameter().
    One point for traingle.__init__().
    One point for traingle.is_equilateral().'''
    
    points = 0
    global Rectangle
    global Circle
    global Triangle
    global rectangle
    global circle
    global triangle
    
    class Rectangle: 
        def __init__(self):
            self.att = None
            
    class Circle: 
        def __init__(self):
            self.att = None
            
    class Triangle: 
        def __init__(self):
            self.att = None
            
    triangle = None
    circle = None
    rectangle = None
    
    try:
        exec(code, globals())
    
    except Exception as e:
        print(e)
    
    #test rectangle area
    try:
        exec(f'rectangle = Rectangle(width={3},height={7})',globals())
        
        if rectangle.area() == 3 * 7:
            points += 1
    
    except Exception as e:
        print(e)
    
    #test rectangle perimeter
    try:
        exec(f'rectangle = Rectangle(width={3},height={7})',globals())
        
        if rectangle.perimeter() == 2 * (3 + 7):
            points += 1
    
    except Exception as e:
        print(e)
        
    #test circle diameter
    try:
        exec(f'circle = Circle(radius={5})',globals())
        
        if circle.diameter() == 2 * 5:
            points += 1
    
    except Exception as e:
        print(e)
        
    #test triangle init
    try:
        exec(f'triangle = Triangle(a={5},b={5},c={6})',globals())
        
        if triangle.perimeter() == 16 and triangle.area() == 18:
            points += 1
    
    except Exception as e:
        print(e)
        
    #test triangle init
    try:
        exec(f'triangle = Triangle(a={5},b={5},c={6})',globals())
        
        if triangle.is_equilateral() == True:
            exec(f'triangle = Triangle(a={3},b={4},c={5})',globals())
            if triangle.is_equilateral() == False:
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
        active_code_task = re.search(r'(Task 1 - Creating a Student Class \(6 points\))([\W\w]+)(Task 2 - Bank Account Class \(5 points\))',content)[2]
        points += [test_task01(active_code_task)]
    
    except Exception as e:
        print(e)
        points += [0]
        
    print('Grading task02:')
    try:
        active_code_task = re.search(r'(Task 2 - Bank Account Class \(5 points\))([\W\w]+)(#Create a BankAccount instance)',content)[2]
        active_code_task = "".join([line+'\n' for line in active_code_task.split('\n') if not 'input' in line])
        points += [test_task02(active_code_task)]
    
    except Exception as e:
        print(e)
        points += [0]
        
    print('Grading task03:')
    try:
        active_code_task = re.search(r'(Task 3 - Geometric Classes \(5 points\))([\W\w]+)(# Create an instance of the Rectangle class)',content)[2]
        points += [test_task03(active_code_task)]
    
    except Exception as e:
        print(e)
        points += [0]
        
    print('Grading task04:')
    try:
        active_code_task = ""
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
    origin_task = 'task05'
    
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