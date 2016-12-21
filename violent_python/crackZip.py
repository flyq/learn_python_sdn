# coding = UTF-8

"""
crack zip using dictionary
"""

import zipfile
import threading
def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print("Found Passwd : ", password)
        return password
    except:
        pass
def main():
    zFile = zipfile.ZipFile('test.zip')
    passFile = open('pass.txt')
    for line in passFile.readlines():
        password = line.strip('\n')
        t = threading.Thread(target=extractFile, args=(zFile, password))
        t.start()
        """
        guess = extractFile(zFile, password)
        if guess:
            print('Password = ', password)
            return
        else:
            print("can't find password")
            return
        """
        
if __name__ == '__main__':
    main()
