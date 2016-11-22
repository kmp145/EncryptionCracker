import hashlib
import string

def crack(target):
    sampleSpace = string.ascii_lowercase + string.ascii_uppercase + string.digits
    hashTester = [sampleSpace[0]]
    count = 1
    while 1:
        hashTest = ''
        for i in range (0,len(hashTester)):
            hashTest += hashTester[i]
        hashTest.strip()

        #print(hashTest)#FOR DEBUGGING
        
        #Check if correct
        h = hashlib.md5()
        h.update(hashTest.encode('utf-8'))
        if h.hexdigest() == target:
            return hashTest
        
        #Check if max
        if hashTest == sampleSpace[len(sampleSpace)-1] * count:
            count += 1
            for i in range (0, count-1):
                hashTester[i] = sampleSpace[0]
            hashTester.append(sampleSpace[0])
            continue

            
        #Check if hashTest[0] = max
        elif hashTester[0] == sampleSpace[len(sampleSpace)-1]:#make elif
            hashTester[0] = sampleSpace[0]
            for i in range (1, len(hashTest)):
                if hashTester[i] == sampleSpace[len(sampleSpace)-1]:
                    hashTester[i] = sampleSpace[0]
                    #hashTester[i+1] = sampleSpace[sampleSpace.find(hashTester[i])+1]
                    continue
                else:
                    hashTester[i] = sampleSpace[sampleSpace.find(hashTester[i])+1]
                    break

        else:
            hashTester[0] = sampleSpace[sampleSpace.find(hashTester[0])+1]

    pass

#Define input/output
h = hashlib.md5()
hashList = input('Enter name of hashlist:\t')
outputList = input('Enter name of the output file:\t')
try:
    file = open(hashList, 'r')
    hashRead = file.read()
    print ('Loaded hashes:\n' + str(hashRead))
    file.close()
except:
    print ('Invalid input file')

#Looping through hashes
hashes = hashRead.splitlines()
data = ''
for line in hashes:
    file = open(outputList, 'w')
    print ('Now cracking:\t' + line)
    result = crack(line)
    print ('Result found!\t'+ line + ' = ' + result)
    data += line + ' = ' + result +'\n'
    file.write(data)
    file.close()


