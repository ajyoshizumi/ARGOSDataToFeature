##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2018
## Author: alexander.yoshizumi@duke.edu (for ENV859)
##---------------------------------------------------------------------

# Import modules
import sys, os, arcpy

# Set input variables (Hard-wired)
inputFile = 'V:/ARGOSTracking/Data/ARGOSData/1997dg.txt'
outputFC = 'V:/ARGOSTracking/Scratch/ARGOStrack.shp'

# Open the ARGOS data file for reading
inputFileObj = open(inputFile, 'r')

# when doing a while loop, we do not load the entire thing to memory
# Get the first line so we can loop
lineString = inputFileObj.readline()
while lineString:

    # Set code to run only if the line contains "Date :"
    if "Date :" in lineString:

        # Split the line string into  list
        lineList = lineString.split()

        print(lineList[0])
        break

    # Get the next line
    lineString = inputFileObj.readline()


