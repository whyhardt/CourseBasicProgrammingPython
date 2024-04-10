# Basic Programming in Python Assignment Repo
This repository contains the assignments and autograding scripts for the Basic Programming in Python course from SuSe23 at the University of Osnabrück.

# Autograding system
## Submission folder
Task submissions need to be manually copied into the submissions folder.
This should be done by creating a subfolder named "task01", for the example of task 1.
If this is not done, the autograding script will not work.
The end result will be a folder at location "./submissions/task01/" with all jupyter notebooks inside.
During this process you also need to do some preprocessing, namely two things.
Firstly, make sure all notebooks have the name and mail of the student entered inside them, the name of the submission notebook is not enough!
Secondly, make sure, for traceability, that there are no duplicate submissions from the same student, if there are, it will be annoying to check which was which.

## Running the conversion script
Firstly, you will need to run the conversion.py script at base and provide it a folder path.
This can be done by running ```python conversion.py --path='./submissions/task01/'``` for the example of the first task.
The script will then convert all scripts into .py scripts and store them in a subfolder "auto".
All original notebooks will be kept for checking and stored in the subfolder "original".
Additionally, an empty folder "manual" will be created in which all scripts will be placed that the autograding failed on.
Scripts for which autograding failed can simply be changed and put back into the "auto" folder, or they can be graded manually.

# Running the specific autograding script
The autograding script for a given task can be found in the "autograding" folder.
To run it you will not have to provide any folder path, however, you will need to run the script from base by copying it.
This is because of the folder structure of the repository.
The script will proceed to process all scripts in the folder and autograde them.
A pandas dataframe with the results and the student names and mails will be generated and also a .txt file listing all students who failed the task.
From there on it is important to briefly check for errors in autograding, but then you can message all students who failed in a mail individually.
Additionally, in the generated .csv file, especially for tasks with high chance for autograding errors, all cases with 0 points should be checked manually.