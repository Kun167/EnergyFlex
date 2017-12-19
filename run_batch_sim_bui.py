# Replace varaibles in .dck and/or .bui files with values we want to simulate
# Create new deck files and then launch Trnsys for simulation

import os
import shutil
import subprocess
import glob

# Specify the path to the directory containing the template deck file
# and template building file.
trnsysFilesPath = r'C:\TRNSYS18\MyProjects\eSim'
# Change directory.
os.chdir(trnsysFilesPath)
# Join template bui filename to path.
template_buifilename = os.path.join(trnsysFilesPath,'Behouse_temp.b17')
# Calculate a 25% glazing fraction
windowArea = 100
glazingFraction = 0.25*windowArea
# Open a temporary file for writing.
tempfilename = r'C:\TRNSYS18\MyProjects\eSim\temp.txt'
tempFile = open(tempfilename, 'w')
# Open the template file
templateFile = open(template_buifilename, 'r')
# iterate over each line in the template file
for line in templateFile:
        # Replace '%FFRAME%' with variable (if '%FFRAME% is found)
        line = line.replace('%FFRAME%', str(glazingFraction))
        # Write the line to the temporary file.
        tempFile.write(line)
# Close the template file.
tempFile.close()
# Close the temporary file.
templateFile.close()
# Copy the temporary file over the template file
shutil.copyfile(tempfilename, template_buifilename)

# Join template dck filename to path.
template_dckfilename = os.path.join(trnsysFilesPath,'Template.dck')
# Calculate something random
randomCalculation = (100 - 60)/20
# Open the temporary file for writing.
tempFile = open(tempfilename, 'w')
# Open the template file
templateFile = open(template_dckfilename, 'r')
# itterate over each line in the template file
for line in templateFile:
        # Replace '%FFRAME%' with variable (if '%TURN% is found)
        line = line.replace('%TURN%', str(randomCalculation))
        # Write the line to the temporary file.
        tempFile.write(line)
# Close the template file.
tempFile.close()
# Close the temporary file.
templateFile.close()
# Copy the temporary file over the template file
shutil.copyfile(tempfilename, template_dckfilename)

for file in glob.glob("*.dck"):
    # Add the path to the deck file
    deckfilename = os.path.join(trnsysFilesPath,file)
    # Run TRNSYS on the deckfile.
    subprocess.call(["C:\Trnsys\17-2-Bee\Exe\TRNExe", deckfilename, '/n'])
