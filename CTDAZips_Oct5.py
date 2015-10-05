######################################################
##          Connecticut Digital Archive             ##
##              Zip Upload Script                   ##
##          Developed by Kate Johnson, Fall 2015    ##
######################################################

## PURPOSE ##
# Add assets and metadata into 2048 MB zip files to make uploading more efficient.

## STEPS ##
# 1. Access file directory with assets and metadata
# 2. Loop through assets/metadata in directory and add to zip file
# 3. Stop adding and finish zip if file size gets up to 2048 MB
# 4. But only add an even number of files so as not to separate the asset & metadata
# 5. Continue to loop starting at the next file after 2048 MB

# Zips can be named anything because they will be deleted afterwards
# Zip1, Zip2. Name of the last thing zipped?


import os,os.path, zipfile
from decimal import *
from time import *

#################################################
##      Function to create zipfile             ##
#################################################

# Add the files from the list to the zip archive
def zipFunction(zipList):

    # Specify zip archive output location and file name
    zipName = "D:\USERS\kmj12002\Documents\ziptest1.zip"

    # Create the zip file object
    zipA = zipfile.ZipFile(zipName, "w", allowZip64=True)  

    # Go through the list and add files to the zip archive
    for w in zipList:

        # Create the arcname parameter for the .write method. Otherwise the zip file
        # mirrors the directory structure within the zip archive (annoying).
        arcname = w[len(root)+1:]

        # Write the files to a zip
        zipA.write(w, arcname, zipfile.ZIP_DEFLATED) # Have to add the zip64 bit when archive is over 2 GB. Remove for less.

    # Close the zip process
    zipA.close()
    return       
#################################################
#################################################

sTime = clock()

# Set the size counter
totalSize = 0
subtotal = 0

# Create an empty list for adding files to count MB and make zip file
zipList = []

tifList = []

xmlList = []

# Specify the directory to look at
searchDirectory = "Y:\Loading Dock\CHO Contributor Files\Wadsworth Atheneum"

# Create a counter for the zip name
count = 0

# Set the root, directory, and file name
for root,direc,f in os.walk(searchDirectory):

        #Go through the files in directory
        for name in f:
            # Set the os.path file root and name
            full = os.path.join(root,name)

            # Split the file name from the file extension
            n, ext = os.path.splitext(name)

            # Get size of each file in directory, size is obtained in BYTES
            fileSize = os.path.getsize(full)

            # Set parameters for Decimal to convert from bytes to megabytes
            #getcontext().prec = 6
            #getcontext().rounding = ROUND_UP
            
            # Get the individual file size in megabytes
                # 1 kilobyte = 1,024 bytes
                # 1 megabyte = 1,048,576 bytes
                # 1 gigabyte = 1,073,741,824 bytes

            # Convert from bytes to megabytes
            megabytes = float(totalSize)/float(1048576)
            #megabytes = totalSize/1048576
            print megabytes

            if ext == ".tif":  # should be everything that is not equal to XML (could be TIF, PDF, etc.)
                tifList.append(n)#, fileSize/1048576])
                tifSorted = sorted(tifList)
            elif ext == ".xml":
                xmlList.append(n)#, fileSize/1048576])
                xmlSorted = sorted(xmlList)

            subtotal += fileSize # convert to megabvytes

            if full.endswith(".xml") or full.endswith(".tif"):
                if subtotal < 2040:
                    zipList.append(full)

            if subtotal <= 2040:
                zipFunction(zipList)
                subtotal = 0

            count +=1


#zipFunction(zipList)

##for t,x in zip(tifSorted,xmlSorted):
##    zipList.append([t,x])

##if tifSorted == xmlSorted:
##    zipFunction(zipList)
##elif tifSorted != xmlSorted:
##    print "The TIF file names and XML file names do not match"

            #for item in fileList:
                # need to check that the TIF name matches the XML name. Then add the sizes together and add to Zip list for zipping.
                # Need to make sure that the combined file size does not go over 2048 MB.

##            while megabytes < 10 and len(fileList) % 2 == 0 :
##                fileList.append(full)
##                continue
##            #if megabytes == 10 and len(fileList) % 2 == 0:   # see if there is a way to round this up from 3.999999 etc to 3.99 or something??
##                zipFunction(fileList)

##        # Check the file size
##        if megabytes == 10 and len (fileList) % 2 == 0:
##        zipFunction(fileList)
                    

eTime = clock()
elapsedTime = eTime - sTime
print "Run time is %s seconds"%(elapsedTime)



        
