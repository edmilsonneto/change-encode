import os
import codecs

PROJECT_PATH = "/Users/edmilsonneto/developer/git/autorizador"
FILE_EXTENSIONS = [".vm", ".java"]
FROM_ENCODE = "cp1252"
TO_ENCODE = "utf-8"

def convert(filePath):
    BLOCKSIZE = 1048576
    with codecs.open(filePath, "r", FROM_ENCODE) as sourceFile:
        with codecs.open(filePath + TO_ENCODE, "w", TO_ENCODE) as targetFile:
            while True:
                contents = sourceFile.read(BLOCKSIZE)
                if not contents:
                    break
                targetFile.write(contents)
                os.remove(filePath)
                os.rename(filePath + TO_ENCODE, filePath)

for root, dirs, files in os.walk(PROJECT_PATH):
    for file in files:
        if file.endswith(tuple(FILE_EXTENSIONS)):
            print("Convertendo : " + os.path.join(root, file))
            convert(os.path.join(root, file))
            print("Convertido! : "os.path.join(root, file))