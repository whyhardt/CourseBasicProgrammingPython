import os
import re
import shutil

import numpy as np
import pandas as pd

import math

from difflib import SequenceMatcher
from tqdm import tqdm

def test_task01(lines : list) -> int:
    '''Grading scheme, one point per correct variable declaration.'''
    
    points = 0
    global a; global b; global c; global d; global e; global f; global g; global h
    a, b, c, d, e, f, g, h = None, None, None, None, None, None, None, None
    
    for line in lines:
        try:
            exec(line, globals())
            
        except:
            pass #making sure a single line with fatal error will not break the entire code
        
    if a == "hello world" and type(a) == str:
        points += 1
        
    if b == -19 and type(b) == int:
        points += 1
        
    if c == 7.29 and type(c) == float:
        points += 1
        
    if d == False and type(d) == bool:
        points += 1
        
    if e == (1, 2, 4.56) and type(e) == tuple:
        points += 1
        
    if f == ['a', 'b', 'c'] and type(f) == list:
        points += 1
        
    if g == True and type(g) == bool:
        points += 1
        
    if float(h) == float(((28*2)-14)):
        points += 1
    
    return points

def test_task02(lines : list) -> int:
    '''One point per correct formula. Requires a  check for all 0 point autograded solutions.'''
    
    cor_form = {
        'a' : lambda a, b, c, d: (a+b)/(c+d),
        'b' : lambda a, b, c, d: (a+b+c+d)/4,
        'c' : lambda a, b, c, d: (a**2+b**3)/(1+(c/d)),
        'd' : lambda a, b, c, d: math.sqrt(a-b)
    }
    
    value_sets = [(1,1,1,1),(10,20,30,40),(9.283,7.28,9.28,-6.94),(-1,4.72,-893.83,42)]
    
    global test_form
    test_form = {'a' : lambda a, b, c, d: 0, 'b' : lambda a, b, c, d: 0, 'c' : lambda a, b, c, d: 0, 'd' : lambda a, b, c, d: 0}
    
    code_lines_cleaned = []
    for i, line in enumerate(lines):
        if "=" in line:
            code_lines_cleaned.append(re.sub(r'([\w\d\_]+=)',"",line.replace(" ","")))
        else:
            code_lines_cleaned.append(line)
    
    for i, line in enumerate(code_lines_cleaned):
        #handle non-declarative form e,g. no smth = formula
        try:
            exec(f'test_form[{list(test_form.keys())}[{i}]] = lambda a, b, c, d: {line}', globals())
                
        except Exception as e:
            print(e)
            print(f"Unable to evaluate single line {i}") #we pass to ensure a fatal error in one line will only affect one line and not the whole task grading
    
    points = 4
    
    for i, key in enumerate(list(test_form.keys())[:-1]):
        for value_set in value_sets:
            if not np.isclose(test_form[key](*value_set), cor_form[key](*value_set)):
                print('Lost point due to:',f'Formula {key}:',value_set,test_form[key](*value_set),cor_form[key](*value_set),code_lines_cleaned[i])
                points -= 1
                break
                
    for value_set in [(2,1,0,0),(2,0,0,0),(10,5,0,0),(7.162,2.71,0,0)]:
        if not np.isclose(test_form['d'](*value_set), cor_form['d'](*value_set)):
            print('Lost point due to:',f'Formula d:',value_set,test_form['d'](*value_set),cor_form['d'](*value_set),code_lines_cleaned[-1])
            points -= 1
            break
    
    return points

def test_task03(lines : str) -> int:
    '''Grading scheme, one point for doing a single input statement correctly, the rest for a successful switch.
    This task will be checked with possible sample solutions instead of a flexible solution, therefore check all cases with zero or one point individually again.'''
    
    points = 0
    
    if 'a=input(' in lines.replace(" ","") or 'b=input(' in lines.replace(" ","") or 'a=(input(' in lines.replace(" ","") or 'b=(input(' in lines.replace(" ",""):
        if "\')" in lines.replace(" ","") or "\")" in lines.replace(" ",""):
            points += 1
            
        elif "=input()" in lines.replace(" ","") or "=(input())" in lines.replace(" ",""):
            points += 1
    
    #multiple declaration case
    if 'a,b=b,a' in lines.replace(" ","") or 'b,a=a,b' in lines.replace(" ",""):
        points += 2

    #dummy case for a and b
    elif '=a' in lines.replace(" ","") and 'a=b' in lines.replace(" ","") and 'b=' in lines.replace(" ",""):
        points += 2

    elif '=b' in lines.replace(" ","") and 'b=a' in lines.replace(" ","") and 'a=' in lines.replace(" ",""):
        points += 2
    
    return points

def test_task04(codestring : str) -> int:
    '''
    Grading scheme (n/5):
    1 point if the code contains if statements and runs.
    1 point if the variable "allowed" works as it should.
    1 point if the variable "price" works as it should (including no price for allowed=False).
    1 point if the fringe cases of variable "age" work as they should (12,18)
    1 point if the fringe cases of variable "height" work as they should (120+-1).
    Requires a check for all 0 point autograded solutions.
    '''
    
    if 'def ' in codestring:
        print('Tried to define a function -> manual grading.')
        raise ValueError("Codestring needs to be graded manually.")
    
    points = 5
    
    allow_func = lambda height, age: False if height < 120 else True
    price_func = lambda height, age: {
        5: 5, 10: 5, 12: 8, 13 : 8,14 : 8, 15 : 8, 16 : 8, 17 : 8,
        18 : 8, 19 : 15, 20 : 15, 43 : 15
    }[age]
    
    global allowed
    global price
    global age
    global height
    
    allowed, price = True, 0
    
    # test_user_code = lambda height, age, scope: exec(codestring, scope)
    
    try:
        #tests if the code works at all
        height, age, allowed, price = 190, 21, True, None
        exec(codestring,globals())
        
    except:
        print('Lost point due to:','Code not working')
        return 0
    
    #tests if the code does any casehandling at all
    if not (('if' in codestring) and ('age' in codestring) and ('height' in codestring)):
        print('Lost point due to:','Code not working')
        return 0
    
    #test price
    for age in [5,10,13,14,15,16,17,19,20,43]:
        height, age, allowed, price = 120, age, True, None
        exec(codestring, globals())
        if not (price == price_func(120,age)):
            points -= 1
            print('Lost point due to:','Price not correct for ages.')
            break
    
    #test allowed
    for height in [1,5,10,100,110,122,130,200,250]:
        height, age, allowed, price = height, 16, True, None
        exec(codestring, globals())
        if not (allowed == allow_func(height,16)):
            points -= 1
            print('Lost point due to:','Allowed not correct for height.')
            break
    
    #test fringe allowed and price
    for age in [12,18]:
        height, age, allowed, price = 120, age, True, None
        exec(codestring, globals())
        if not (price == price_func(120,age)):
            points -= 1
            print('Lost point due to:','Price not correct for 12,18.')
            break
    
    for height in [119,120,121]:
        height, age, allowed, price = height, 16, True, None
        exec(codestring, globals())
        if not (allowed == allow_func(height,16)):
            points -= 1
            print('Lost point due to:','Allowed not correct for 119,120,121.')
            break
    
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
        active_code_task_1 = [line for line in re.search(r'(The result of 28 times 2 minus 14)([\w\W]+)(Task 2 Implementing formulas)',content)[2].split('\n') if '=' in line]
        points += [test_task01(active_code_task_1)]
    
    except Exception as e:
        print(e)
        points += [0]
    
    print('Grading task02:')
    try:
        active_code_task_2 = [line for line in re.search(r'(frac{A\+B}{C\+D})([\w\W]+)(Task 3)',content)[2].split('\n') if (('a' in line) and ('b' in line)) and not line.startswith('#') and not 'if' in line]
        active_code_task_2 = [re.sub(r'print',"",line) for line  in active_code_task_2]
        if not len(active_code_task_2) == 4:
            raise ValueError('Detected more patterns than supposed to in input code.')
        # print(active_code_task_2)
        points += [test_task02(active_code_task_2)]
    
    except Exception as e:
        print(e)
        points += [0]
    
    print('Grading task03:')
    try:
        active_code_task_3 = re.search(r'(information from the users.)([\w\W]+)(Task 4)',content)[2]
        points += [test_task03(active_code_task_3)]
        active_code_task_3 = "".join([line+'\n' for line in active_code_task_3.split('\n') if not 'print' in line])
    
    except Exception as e:
        print(e)
        points += [0]
    
    print('Grading task04:')
    try:
        active_code_task_4 = re.search(r'(age = int\(input\(\)\))([\w\W]+)', content)[2]
        active_code_task_4 = "".join([line+'\n' for line in active_code_task_4.split('\n') if not 'input' in line and not 'height=' in line.strip() and not 'age=' in line.strip() and not 'print' in line and not line.startswith('#') and not line == '\n' and not line == ''])
        # print(f'{path}:\n\n')
        # print(active_code_task_4)
        points += [test_task04(active_code_task_4)]
        
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
    origin_task = 'task01'
    
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
            shutil.move(path, "./submissions/task01/manual/"+path[path.find('submission_'):])
    
    df.to_csv('./autograding/task01.csv',index=False)

if __name__ == "__main__":
    main()