# Use a template deck file, replace %MyVar% in it with a series of values that the python program
# would read in a text file, and run each deck file.
import os
import subprocess

# Specify the path to the directory containing the Template deck file (containing %MyVar%) and txt file
# containing the series of values you wish to use to replace %MyVar%.
trnsysFilesPath = 'C:\Trnsys17\MyProjects\PythonEx2'
# Change directory.
os.chdir(trnsysFilesPath)
textfilename = os.path.join(trnsysFilesPath,'variables.txt')
templatefilename = os.path.join(trnsysFilesPath,'Template.dck')
# Open 'variable.txt' file for reading.
textFile = open(textfilename, 'r')
# For loop: for every variable (one per line) in the 'variable.txt' file create a .dck file
for variableLine in textFile:
    variable = variableLine.replace('\n','')
    # Create a file filename for copying edited contents into.
    deckfilename = os.path.join(trnsysFilesPath,'batchfile'+str(variable)+'.dck')
    print deckfilename
    # Open the deck file for writing.
    deckFile = open(deckfilename, 'w')
    # Open Template deck file for reading.
    templateDeckFile = open(templatefilename, 'r')
    # For loop: for every line in the  Template deck file
    for line in templateDeckFile:
            # Replace '%MyVar%' with variable (if '%MyVar% is found)
            line = line.replace('%MyVar%', variable)
            # Write the line to the new deck file.
            deckFile.write(line)
    # Close the deck file.
    deckFile.close()
    # Run TRNSYS on the deckfile.
    subprocess.call(["C:\Trnsys17\Exe\TRNExe.exe", deckfilename, '/n'])
    # Close the template file.
    templateDeckFile.close()
