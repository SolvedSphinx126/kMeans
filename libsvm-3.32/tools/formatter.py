#Formatted data to be compliant with checkdata.py

fileName = "iris.data"
lineCount = 0

with open(fileName, 'r') as input, open('iris.txt', 'w') as output:
    for line in input:
        values = line.split(',')
        outputLine = ""
        if lineCount < 50:
            outputLine = f"1 1:{values[0]} 2:{values[1]} 3:{values[2]} 4:{values[3]}\n"
        elif lineCount < 100:
            outputLine = f"2 1:{values[0]} 2:{values[1]} 3:{values[2]} 4:{values[3]}\n"
        else:
            outputLine = f"3 1:{values[0]} 2:{values[1]} 3:{values[2]} 4:{values[3]}\n"
        output.write(outputLine)
        lineCount += 1
        


