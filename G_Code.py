import re

lower_value= 3.440924
upper_value= 14.573949



def finding_lines():
    with open("C:\Python\UM2+_magnetTest.py", "r") as f:
        fileArray = f.readlines()

    with open("C:\Python\\newmagnetTest.py", "w") as f:
        lookingForLow  = True
        lookingForHigh = True
        for line in fileArray:
            print line 
            regex = re.compile(r'G0\sX\d+\.\d+\sY\d+\.\d+\sZ([0-9][0-9]?\.\d+)')
            searchedLine = regex.search(line)

            if searchedLine:
                Z_number = float(searchedLine.group(1))

                if Z_number > lower_value and lookingForLow:
                    print   "M226\n" + line
                    f.write("M226\n" + line)
                    lookingForLow = False

                if Z_number > upper_value and lookingForHigh:
                    print   "M226\n" + line
                    f.write("M226\n" + line)
                    lookingForHigh = False
            else:
                f.write(line)


finding_lines()