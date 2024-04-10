import os
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", default=None)
args = parser.parse_args()

def isolate_nameless(path : str):
    notebook_paths = [path for path in os.listdir(path) if path[-6:] == '.ipynb']
    
    isolated = []
    for notebook_path in notebook_paths:
        try:
            file = open(path+notebook_path,'r',encoding='utf-8')
            content = file.read()
            file.close()
            
            #case normal \n split
            if not sum([len(line) for line in content.lower().split('\n') if 'example' in line]) >= (0.5*len(content.lower())):
                if any([part in "".join([line for line in content.lower().split('\n') if 'example' in line]) for part in ['your name here','mail','@']]):
                    isolated += [notebook_path]
            else:
                #case with broken document which does not properly split with \n
                if any([part in "".join([line for line in content.lower().split('\\n') if 'example' in line]) for part in ['your name here','mail','@']]):
                    isolated += [notebook_path]
        
        except:
            isolated += [notebook_path]
            
    if not os.path.exists(path+'isolated/'):
        os.mkdir(path+'isolated/')
        
    for iso_path in isolated:
        shutil.move(path+iso_path, path+'isolated/'+iso_path)
        
    if len(isolated) != 0:
        print('Isolated nameless documents for manual fix.')
        return False
        
    else:
        return True
        
def rename_notebooks(path : str):
    notebook_paths = [path for path in os.listdir(path) if path[-6:] == '.ipynb']
    
    for i, notebook_path in enumerate(notebook_paths):
        os.rename(path+notebook_path, path+f'submission_{i}.ipynb')

def convert_directory(path : str):
    notebook_paths = [path for path in os.listdir(path) if path[-6:] == '.ipynb']
    
    for notebook_path in notebook_paths:
        os.system(f'jupyter nbconvert --to python "{path+notebook_path}"')
    
    os.mkdir(path+'/manual/')
    os.mkdir(path+'/auto/')
    os.mkdir(path+'/original/')
    
    for notebook_path in notebook_paths:
        shutil.move(path+notebook_path, path+'original/')
    
    for script_path in [path for path in os.listdir(path) if path[-3:] == '.py']:
        shutil.move(path+script_path, path+'/auto/')
    
def main(args):
    if args.path != None:
        if os.path.exists(args.path+'isolated/'):
            notebooks = [path for path in os.listdir(args.path+'isolated/') if path[-6:] == '.ipynb']
            
            #move notebooks from isolated back into submissions folder
            for notebook_path in notebooks:
                shutil.move(args.path+'isolated/'+notebook_path, args.path+notebook_path)
        
        if isolate_nameless(args.path):
            # if os.path.exists(args.path+'isolated/'):
            #     os.remove(args.path+'isolated/')
            rename_notebooks(args.path)
            convert_directory(args.path)
            print(f'Successfully set up the grading folder for {args.path}.')
        else:
            print('Please run again with including the student names in the nameless files.')
        
    else:
        raise ArgumentError("Please provide a file path in the script call.")

if __name__ == "__main__":
    main(args)