import os
import re
import shutil
import math

import numpy as np
import pandas as pd

from difflib import SequenceMatcher
from tqdm import tqdm

def test_task01(code : str) -> int:
    '''Two points for right format of the programmer_joke list.
    Two more points for a conditional in which the length is correctly measured and true and false is given correctly.
    One more point for using input correctly.
    Requires manual grading of point 0 and point <=2 tasks since they may be flawed due to unecessary included code pieces.'''
    
    points = 0
    
    code_task1 = "".join([line + '\n' for line in code.split('\n') if "programmer_joke" in line])
    
    global programmer_joke
    global test
    
    programmer_joke = None
    test = None
    
    try:
        exec(code_task1, globals())
        if type(programmer_joke) == list:
            if "".join(programmer_joke) == "".join(['That', 'code', 'looks', 'like', 'it', 'is', 'snaking', 'around']):
                points += 2
                
    except:
        print('unable to run part 1 code.')
    
    #dont test the second one if not at least everything stated in task description is present
    if not 'input' in code or not 'print(True)' in code or not 'print(False)' in code or not 'if' in code:
        if "print(len(string_a)>len(string_b))" in code.replace(" ",""):
            if 'input' in code:
                return points+3
        return points
    
    #increment by one because tools have been used as asked
    points += 1
    
    code_task2 = [line for line in code.split('\n') if not "programmer_joke" in line]
    
    for i, line in enumerate(code_task2):
        #tests for one line case for print true false
        if 'len(string_a)' in line and 'len(string_b)' in line and ('>' in line or '<' in line) and 'print' in line:
            extract = "".join([char for char in line if char in ['a','b','>','<']])
            if 'a>b' in extract or 'b<a' in extract:
                return points+2
        
        if 'print ' in line:
            code_task2[i] = re.sub(r'print ', 'print',code_task2[i])
        
        if 'input' in line:
            if 'input ' in line:
                code_task2[i] = re.sub(r'input ',"input",code_task2[i])
                
            if 'string_a' in line:
                code_task2[i] = re.sub(r'(input\(\"|\')([\w\s:?]+)(\"|\')(\))|input\(\)',"\"I am longer than b\"",code_task2[i])
                
            else:
                code_task2[i] = re.sub(r'(input\(\"|\')([\w\s:?]+)(\"|\')(\))|input\(\)',"\"I am shorter\"",code_task2[i])
        
        if 'print(True)' in line:
            code_task2[i] = re.sub(r'print\(True\)','test = True',code_task2[i])
            
        if 'print(False)' in line:
            code_task2[i] = re.sub(r'print\(False\)','test = False',code_task2[i])
    
    code_task2 = "".join([line + '\n' for line in code_task2])
    
    try:
        # print(code_task2)
        exec(code_task2, globals())
        
    except Exception as e:
        print(e)
        print('unable to run part 2 code.')
    
    #test should be true here if everything worked out
    if type(test) == bool:
        if test == True:
            points += 2
    
    return points

def test_task02(code : str) -> int:
    '''Due to informing the students late about one error every students gets the first if condition graded as correct.
    For each correctly working condition one point is given'''
    
    points = 1 #we give one by default
    
    try:
        conditionals = [line for line in code.split('\n') if 'if' in line][1:] #we start with the second one to ignore the alphanum condition

        test_chars = ['A','1','a']

        methods = []
        for conditional in conditionals[:3]:
            methods.append(re.search(r'(\.\w+\([\w\s,]*\))',conditional)[0])   
        
        global result
        result = True

        #first test should be true iff char is a number
        for i, char in enumerate(test_chars):
            if 1 > len(methods):
                break

            try:
                exec(f'result = "{char}"{methods[0]}',globals())
                
            except:
                break
            
            #breakoff wrong conditions
            if i == 0 and result == True:
                break

            if i == 1 and result == False:
                break

            #correct last condition gives points
            if i == 2 and result == False:
                points += 1

        #first test should be true iff char is uppercase
        for i, char in enumerate(test_chars):
            if 2 > len(methods):
                break

            try:
                exec(f'result = "{char}"{methods[1]}',globals())
            except:
                break

            #breakoff wrong conditions
            if i == 0 and result == False:
                break

            if i == 1 and result == True:
                break

            #correct last condition gives points
            if i == 2 and result == False:
                points += 1

        #first test should be true iff char is lowercase
        for i, char in enumerate(test_chars):
            if 3 > len(methods):
                break

            try:
                exec(f'result = "{char}"{methods[2]}',globals())
            except:
                break

            #breakoff wrong conditions
            if i == 0 and result == True:
                break

            if i == 1 and result == True:
                break

            #correct last condition gives points
            if i == 2 and result == True:
                points += 1
    
    except Exception as e:
        print(e)
    
    return points

def test_task03(code : str) -> int:
    '''One point per correct box of this task'''
    
    points = 0
    
    #split the code into the specific subtasks
    code_processed = [line for line in code.split('print(result)') if not (line == '\n') ]
    
    global result
    result = None
    
    for i, box in enumerate(code_processed):
        result = None
        try:
            exec(box,globals())
            # print(box, result)
            if type(result) != type(None):
                #test conditionals in order
                if i == 0 and result == "Cherry" and not "result=cherry" in box.lower().replace("\"","").replace("\'","").replace(" ",""):
                    points += 1
                
                if i == 1 and result == ["Potato", "Onion"] and not "result=[potato,onion]" in box.lower().replace("\"","").replace("\'","").replace(" ",""):
                    points += 1
                    
                if i == 2 and result == ["Apple", "Banana","Potato", "Onion"] and not "result=[apple,banana,potato,onion]" in box.lower().replace("\"","").replace("\'","").replace(" ",""):
                    points += 1
                    
                if i == 3 and result == ['Apple', 'Cherry', 'Potato'] and not "result=[apple,cherry,potato]" in box.lower().replace("\"","").replace("\'","").replace(" ",""):
                    points += 1
                    
                if i == 4 and result == ['Onion', 'Potato', 'Tomato', 'Cherry', 'Banana', 'Apple'] and not "result=[onion,potato,tomato,cherry,banana,apple]" in box.lower().replace("\"","").replace("\'","").replace(" ",""):
                    points += 1
                    
                if i == 5 and result == ['Banana', 'Joghurt', 'Gummy bears'] and not "result=[banana,joghurt,gummybears]" in box.lower().replace("\"","").replace("\'","").replace(" ",""):
                    points += 1
                    
        except Exception as e:
            print(e)
    
    return points

def test_task04(code : str) -> int:
    '''Two points for the replacing task, one for conditional and one for replacement.
    Four points for each correct file assessment, including the else.
    It is required to check point=0 solutions manually.'''
    
    points = 0
    
    code_filtered = "".join([line+'\n' for line in code.split('\n') if not (line.startswith('#') or line == '' or 'input' in line or "hello,world." in line.lower().replace(" ",""))])
    code_filtered = re.sub(r'(print\([\'\"]{1}[Uu]{1}nsupported\s[Ff]{1}ile\s[Ff]{1}ormat[\'\"]\))',"file_type = \"Unsupported file format\"",code_filtered)
    # print(code_filtered)
    
    global file_type
    global file_name
    file_type = ""
    file_name = ""
    
    filenames_test = ['file.txt','lectu:re.pdf','something.doc','img.png','me.jpg','movie,.mp4','vid.mov','weird.ga']
    
    results = []
    
    for name in filenames_test:
        try:
            file_name = name
            exec(code_filtered, globals())
            results.append((file_name,file_type))
    
        except Exception as e:
            results.append(("",""))
            print(e)
        
    # print(results)
    
    correct = [
        ("file.txt","Document file"),
        ("lectu_re.pdf","Document file"),
        ("something.doc","Document file"),
        ("img.png","Image file"),
        ("me.jpg","Image file"),
        ("movie_.mp4","Video file"),
        ("vid.mov","Video file"),
        ("weird.ga","Unsupported file format")
    ]

    # print(correct)
    
    if len(results) != len(correct):
        return 0    

    categories = {'Names' : 0, 'Video' : 0, 'Document' : 0, 'Image' : 0,'Unsupported' : 0}
    
    for i, pair in enumerate(correct):
        if pair[0] == results[i][0]:
            categories['Names'] += 1
        if pair[1].lower() == results[i][1].lower():
            if i <= 2:
                categories['Document'] += 1
            elif i <= 4:
                categories['Image'] += 1
            elif i <= 6:
                categories['Video'] += 1
            else:
                categories['Unsupported'] += 1
                
    #give one point if one swap was successful, two if all cases were
    if categories['Names'] == 8:
        points += 2
    elif categories['Names'] >= 7:
        points += 1
        
    #give points per category max correct
    if categories['Video'] == 2:
        points += 1
    if categories['Document'] == 3:
        points += 1
    if categories['Image'] == 2:
        points += 1
    if categories['Unsupported'] == 1:
        points += 1
        
    print(categories)
    
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
        active_code_task = "".join([line+'\n' for line in re.search(r'(Multiline printing and number of characters \(5 points\))([\w\W]+)(If-statements, methods, and strings)',content)[2].split('\n') if not line.startswith('#') and not len(line) == 0])
        # print(active_code_task)
        points += [test_task01(active_code_task)]
    
    except Exception as e:
        print(e)
        points += [0]
        
    print('Grading task02:')
    try:
        active_code_task = "".join([line+'\n' for line in re.search(r'(If-statements, methods, and strings)([\w\W]+)(Slicing and Indexing)',content)[2].split('\n') if not line.startswith('#') and not len(line) == 0])
        # print(active_code_task)
        points += [test_task02(active_code_task)]
    
    except Exception as e:
        print(e)
        points += [0]
        
    print('Grading task03:')
    try:
        active_code_task = "".join([line+'\n' for line in re.search(r'(Slicing and Indexing \(5 points\))([\w\W]+)(Task 4 Manipulating strings)',content)[2].split('\n') if not line.startswith('#') and not len(line) == 0])
        # print(active_code_task)
        points += [test_task03(active_code_task)]
    
    except Exception as e:
        print(e)
        points += [0]
        
    print('Grading task04:')
    try:
        active_code_task = "".join([line+'\n' for line in re.search(r'(Task 4 Manipulating strings \(6 points\))([\w\W]+)',content)[2].split('\n') if not line.startswith('#') and not len(line) == 0])
        # print(active_code_task)
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
    origin_task = 'task02'
    
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