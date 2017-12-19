# The program replaces the parameters set in the template .dck file with values
# that we want to conduct the parametric study. Then it launches trnsys for 
# batch simulation
import os
import subprocess

# Specify the path to the directory containing the Template deck file 
# and txt file with the series of values to use to replace %Paras%.
trnsysFilesPath = r'C:\TRNSYS18\MyProjects\eSim'
# Change directory.
os.chdir(trnsysFilesPath)
textfilename = os.path.join(trnsysFilesPath,'Parameters.txt')
templatefilename = os.path.join(trnsysFilesPath,'EbcA67Ce3-template.dck')
# Open 'Parameters.txt' file for reading.
textFile = open(textfilename, 'r')
# create a .dck file for every value (one per line) in 'Parameters.txt'
for variableLine in textFile:
    variable = variableLine.replace('\n','')
    # Create a file filename for copying edited contents into.
    deckfilename = os.path.join(trnsysFilesPath,'batchfile.dck')
    print(deckfilename)
    # Open the deck file for writing.
    deckFile = open(deckfilename, 'w')
    # Open Template deck file for reading.
    templateDeckFile = open(templatefilename, 'r')
    # For loop: for every line in the  Template deck file
    for line in templateDeckFile:
    # Replace '%Paras%' with variable
        line = line.replace('%TSetHeatNightShift%', variable)
        # Write the line to the new deck file.
        deckFile.write(line)
    # Close the deck file.
    deckFile.close()
    # Run TRNSYS on the deckfile.
    subprocess.call(["C:\TRNSYS18\Exe\TrnEXE64.exe", deckfilename, '/n'])
    # Close the template file.
    templateDeckFile.close()
