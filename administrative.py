def combineJsonFiles(folderDir, destinationFileDir):
    import os
    finalJSON = open(destinationFileDir, "w") #open the destination file with the "w" parameter to write to the file
    collectedJSON = []
    for fn in os.listdir(folderDir):
        if fn.endswith(".json"):
            smallJSON = json.load(open(folderDir + fn)) #open each JSON file in the directory, if the activity type is "run," append it to the list
            if smallJSON["type"] == "run":
                collectedJSON.append(smallJSON)
    json.dump(collectedJSON, finalJSON) #drop the list of running logs into the final file

combineJsonFiles("data/", "mainJSON.json")