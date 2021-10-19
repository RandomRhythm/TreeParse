#parses:
# tree /a 
# tree /a /f
def depth(strPath):
    myCount = 0
    for chartest in strPath:
        if chartest == " " or chartest == "|":
            myCount += 1
        else:
            return myCount


def TreeParse(strInputFile, strOutputFile, excludeString, boolLogFolder, newColumn):
    global boolHeaderWritten
    f1 = open(strInputFile, 'r', encoding="utf-8")
    f2 = open(strOutputFile, 'a+', encoding="utf-8")
    directory = []
    rootdir = ""
    for line in f1:
        if "\\---" in line or "+---" in line:
            intDepth = depth(line) #line.count("|") + line.count("+---") + line.count("\---") + line.count("   +---") 

            if intDepth >=4:
                intDepth = intDepth /4

            if intDepth <= 1:
                print ("Pause")
            while len(directory) >= intDepth + 1:
                directory.pop(len(directory) -1)
            intStart = line.rfind("---")
            if intStart != -1:
                intStart +=3
            else:
                intStart = 0
            folderName = line[intStart: -1]
            if "|" in folderName:
                print("Pause")
            if len(directory) == intDepth + 1:
                directory.pop(len(directory) -1)
                directory.append(folderName)
            else:
                directory.append(folderName)
            #print(directory)
            if boolLogFolder == True:
                lineout =rootdir + "\\".join(directory) + "\n"
                if newColumn != "":
                    lineout = newColumn + "|" + lineout
                f2.write(lineout) #write log entry
        elif "" != line.replace("\n", "").replace(" ", "").replace("|", "") :
            if "\\" in line and rootdir == "" and excludeString not in line: #set root directory to argument value passed to the tree command
                rootdir = line[:-1]
                if rootdir[-1] != "\\": #add separator
                    rootdir = rootdir + "\\" 
            textDepth = depth(line)
            lineout = rootdir + "\\".join(directory) + "\\" + line[textDepth:]
            if newColumn != "":
                lineout = newColumn + "|" + lineout
            f2.write(lineout) #write log entry
    f1.close()
    f2.close()


TreeParse ("E:\\tree_test.txt", "E:\\tree_output.txt", "executing ", True, "myCompName" )