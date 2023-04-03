import os
import csv

newDir = "modified"
all_statements = ["assertEquals", "assertNull", "assertNotNull", "assertSame", "assertNotSame", "assertFalse", "assertTrue", "assertArrayEquals", "assertToken"]
all_imports = ["import static org.junit.Assert.*;", "import org.hamcrest.CoreMatchers.*;", "import static org.hamcrest.core.Is.is;", "import org.junit.Rule;", "import org.junit.rules.ErrorCollector;", "import static org.hamcrest.CoreMatchers.equalTo;","import static org.hamcrest.CoreMatchers.sameInstance;"]


def needToModify(filePath):
    with open(filePath, 'r') as f:
        content = f.read()
        for statement in all_statements:
            if statement + "(" in content:
                return True
        return False


def reWrite(sourcePath, destinationPath):
    newFile = open(destinationPath, 'a')

    with open(sourcePath, 'r') as f:
        all_lines = f.readlines()
        for line in all_lines:
            newFile.write(line)

    newFile.close()
    return [sourcePath, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def modify(sourcePath, destinationPath):
    assertEqualsCount = 0
    assertNullCount = 0
    assertNotNullCount = 0
    assertSameCount = 0
    assertNotSameCount = 0
    assertFalseCount = 0
    assertTrueCount = 0
    assertArrayEqualsCount = 0
    assertTokenCount = 0

    newFile = open(destinationPath, 'a')

    with open(sourcePath, 'r') as f:
        all_lines = f.readlines()

        import_added = False
        classFound = False
        bracketFound = False
        prevLine = ""
        for line in all_lines:
            if prevLine != "":
                line = prevLine.rstrip() + " " + line.lstrip()
                prevLine = ""

            if import_added == False and line.startswith("package "):
                newFile.write(line + "\n")
                for import_line in all_imports:
                    newFile.write(import_line + "\n")
                import_added = True
                continue


            if classFound == False and "public class" in line:
                classFound = True
                if "{" in line:
                    bracketFound = True
                    newFile.write(line + "\n")

                    spaceCount = line.index("public class") + 4
                    for i in range(spaceCount):
                        newFile.write(" ")
                    newFile.write("@Rule\n")
                    for i in range(spaceCount):
                        newFile.write(" ")
                    newFile.write("public ErrorCollector collector = new ErrorCollector();\n\n")
                else:
                    newFile.write(line)
                continue

            if classFound == True and bracketFound == False:
                if "{" in line:
                    bracketFound = True
                    newFile.write(line + "\n")

                    spaceCount = line.index("{") + 4
                    for i in range(spaceCount):
                        newFile.write(" ")
                    newFile.write("@Rule\n")
                    for i in range(spaceCount):
                        newFile.write(" ")
                    newFile.write("public ErrorCollector collector = new ErrorCollector();\n\n")
                    continue

            if "assertEquals(" in line:
                if ");" not in line:
                    prevLine = line[:-1]
                    continue

                startPos = line.index("assertEquals(")
                endPos = line.index(");") + 1
                assertString = line[startPos:endPos + 1]

                part2 = line.split("assertEquals(")[1]
                params = part2.split(");")[0].split(",")
                param1 = params[0].strip()
                param2 = params[1].strip()
                newString = "collector.checkThat(" + param1 + ", equalTo(" + param2 + "));"
                newStatement = line.replace(assertString, newString)
                newFile.write(newStatement)
                assertEqualsCount += 1
                continue

            if "assertNull(" in line:
                if ");" not in line:
                    prevLine = line[:-1]
                    continue

                startPos = line.index("assertNull(")
                endPos = line.index(");") + 1
                assertString = line[startPos:endPos + 1]

                part2 = line.split("assertNull(")[1]
                params = part2.split(");")[0]
                param1 = params.strip()
                newString = "collector.checkThat(" + param1 + ", equalTo(null));"
                newStatement = line.replace(assertString, newString)
                newFile.write(newStatement)
                assertNullCount += 1
                continue

            if "assertNotNull(" in line:
                if ");" not in line:
                    prevLine = line[:-1]
                    continue

                startPos = line.index("assertNotNull(")
                endPos = line.index(");") + 1
                assertString = line[startPos:endPos + 1]

                part2 = line.split("assertNotNull(")[1]
                params = part2.split(");")[0]
                param1 = params.strip()
                newString = "collector.checkThat(" + param1 + ", notNullValue());"
                newStatement = line.replace(assertString, newString)
                newFile.write(newStatement)
                assertNotNullCount += 1
                continue

            if "assertSame(" in line:
                if ");" not in line:
                    prevLine = line[:-1]
                    continue

                startPos = line.index("assertSame(")
                endPos = line.index(");") + 1
                assertString = line[startPos:endPos + 1]

                part2 = line.split("assertSame(")[1]
                params = part2.split(");")[0].split(",")
                param1 = params[0].strip()
                param2 = params[1].strip()
                newString = "collector.checkThat(" + param1 + ", sameInstance(" + param2 + "));"
                newStatement = line.replace(assertString, newString)
                newFile.write(newStatement)
                assertSameCount += 1
                continue

            if "assertNotSame(" in line:
                if ");" not in line:
                    prevLine = line[:-1]
                    continue

                startPos = line.index("assertNotSame(")
                endPos = line.index(");") + 1
                assertString = line[startPos:endPos + 1]

                part2 = line.split("assertNotSame(")[1]
                params = part2.split(");")[0].split(",")
                param1 = params[0].strip()
                param2 = params[1].strip()
                newString = "collector.checkThat(" + param1 + ", equalTo(" + param2 + "));"
                newStatement = line.replace(assertString, newString)
                newFile.write(newStatement)
                assertNotSameCount += 1
                continue

            if "assertTrue(" in line:
                if ");" not in line:
                    prevLine = line[:-1]
                    continue

                startPos = line.index("assertTrue(")
                endPos = line.index(");") + 1
                assertString = line[startPos:endPos + 1]

                part2 = line.split("assertTrue(")[1]
                params = part2.split(");")[0]
                param1 = params.strip()
                newString = "collector.checkThat(" + param1 + ", equalTo(true));"
                newStatement = line.replace(assertString, newString)
                newFile.write(newStatement)
                assertTrueCount += 1
                continue

            if "assertFalse(" in line:
                if ");" not in line:
                    prevLine = line[:-1]
                    continue

                startPos = line.index("assertFalse(")
                endPos = line.index(");") + 1
                assertString = line[startPos:endPos + 1]

                part2 = line.split("assertFalse(")[1]
                params = part2.split(");")[0]
                param1 = params.strip()
                newString = "collector.checkThat(" + param1 + ", equalTo(false));"
                newStatement = line.replace(assertString, newString)
                newFile.write(newStatement)
                assertFalseCount += 1
                continue
                
            if "assertArrayEquals(" in line:
                if ");" not in line:
                    prevLine = line[:-1]
                    continue

                startPos = line.index("assertArrayEquals(")
                endPos = line.index(");") + 1
                assertString = line[startPos:endPos + 1]

                part2 = line.split("assertArrayEquals(")[1]
                params = part2.split(");")[0].split(",")
                param1 = params[0].strip()
                param2 = params[1].strip()
                newString = "collector.checkThat(" + param1 + ", equalTo(" + param2 + "));"
                newStatement = line.replace(assertString, newString)
                newFile.write(newStatement)
                assertArrayEqualsCount += 1
                continue
                
            if "assertToken(" in line:
                if ");" not in line:
                    prevLine = line[:-1]
                    continue

                startPos = line.index("assertToken(")
                endPos = line.index(");") + 1
                assertString = line[startPos:endPos + 1]

                part2 = line.split("assertToken(")[1]
                params = part2.split(");")[0].split(",")
                param1 = params[0].strip()
                param2 = params[1].strip()
                newString = "collector.checkThat(" + param1 + ", equalTo(" + param2 + "));"
                newStatement = line.replace(assertString, newString)
                newFile.write(newStatement)
                assertTokenCount += 1
                continue    

            newFile.write(line)

    newFile.close()
    return [sourcePath, assertEqualsCount, assertNullCount, assertNotNullCount, assertSameCount, assertNotSameCount, assertFalseCount, assertTrueCount, assertArrayEqualsCount, assertTokenCount]




if __name__ == "__main__":

    os.makedirs(newDir, exist_ok=True)

    header = ["File_Name", "assertEquals", "assertNull", "assertNotNull", "assertSame", "assertNotSame", "assertFalse", "assertTrue", "assertArrayEquals", "assertToken"]
    csvFile = open(newDir + "/assert_counts.csv", "w", encoding="UTF8", newline='')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(header)

    allFiles = os.listdir(".")
    for curFile in allFiles:
        if os.path.isfile(curFile) and curFile.endswith(".java"):
            if needToModify(curFile):
                row = modify(curFile, newDir + "/" + curFile)
            else:
                row = reWrite(curFile, newDir + "/" + curFile)
            csvWriter.writerow(row)

    csvFile.close()

