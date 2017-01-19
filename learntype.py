from bs4 import BeautifulSoup
import time
import requests
from random import randint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def offlineMode():
	try:
		file = open("quotes.txt","r")
	except:
		print 'Nothing found in offline data'

def compareResult():
	file = open("result.txt","r")
	data = file.read().splitlines()
	file.close()
	if data[-1] == max(data):
		print 'It is your highest score'
	else:
		print bcolors.BOLD+bcolors.OKGREEN+'Your highest score is: '+str(max(data))+bcolors.ENDC

def addResult(result):
	file = open("result.txt","a+")
	file.write(result+'\n')
	file.close()

def testingArea(real,typed):
    wordCount = 0
    wrongCount = 0
    for i in xrange(len(real)):
        for j in xrange(len(real[i])):
            if real[i][j] == typed[i][j]:
                if real[i][j] == ' ':
                    pass
                else:
                    wordCount += 1
            else:
                wrongCount += 1
    return wordCount,wrongCount

def randomNum(mx):
    return randint(1,mx)

def getQuotes():
    que = []
    check = []
    x = randomNum(219)
    url = "http://www.values.com/inspirational-quotes?page="+str(x)

    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    h = soup.find_all("h6")
    for i in xrange(2):
        y = randomNum(len(h))
        while True:
            if y in que:
                y = randomNum(len(h))
            else:
                break
        check.append(str(h[y-1].text))
        file = open("quotes.txt","a+")
        file.write(str(h[y-1].text)+'\n')
        file.close()
        que.append(y)
    return check

print bcolors.OKBLUE+'\n\n\nQypo - Make typing interesting'+bcolors.ENDC
print bcolors.OKBLUE+'"Increase your typing speed by reading quotes"'+bcolors.ENDC
raw_input(bcolors.WARNING+'Press Enter to continue...'+bcolors.ENDC)
print bcolors.OKBLUE+'\nTip: Make sure everything is exactly typed same.'+bcolors.ENDC
try:
    text = getQuotes()
except:
    xx = 1
    while True:
        print 'Trying . . .',xx
        try:
            text = getQuotes()
            break
        except:
            xx+=1
            if xx == 5:
                print 'Internet is dead I guess'
                print 'Want to try offline ? [Y]es / [N]o'
                en = raw_input()
                if en == 'Y':
                	offlineMode()
                elif en == 'N':
                	print 'Ok Bye'
                break
print bcolors.BOLD+bcolors.FAIL+'\n\nAll ready'+bcolors.ENDC
print bcolors.FAIL+'Starting in '+bcolors.ENDC
time.sleep(1)
print bcolors.FAIL+'3'+bcolors.ENDC
time.sleep(1)
print bcolors.FAIL+'2'+bcolors.ENDC
time.sleep(1)
print bcolors.FAIL+'1'+bcolors.ENDC
time.sleep(1)
print '\n'
totalTime = 0
totalWords = 0
testingArea = []
for i in text:
    t = time.time()
    print '--------------------------\n'
    print bcolors.BOLD+i+bcolors.ENDC
    print '\n--------------------------'
    test = raw_input()
    print time.time() -t
    totalTime += time.time() -t
    testingArea.append(test)
    time.sleep(1)

wordc = 0
wrongc = 0
#wordc,wrongc = testingArea(text,testing
for i in xrange(len(text)):
    for j in xrange(len(text[i])):
        try:
            if text[i][j] == testingArea[i][j]:
                if text[i][j] == ' ':
                    pass
                else:
                    wordc += 1
            else:
                wrongc += 1
        except:
            wrongc += 1
if wrongc >= 1:
	print bcolors.BOLD+bcolors.FAIL+'\n\nYou failed. Better luck next time'+bcolors.ENDC
else:
	grosswpm = ((wordc+wrongc)/5)/(totalTime/60)
	print bcolors.OKGREEN+'\n\n\nTotal time: ' + str(totalTime)+bcolors.ENDC
	print bcolors.OKGREEN+'Gross WPM: '+ str(grosswpm)+bcolors.ENDC
	print bcolors.FAIL+'Total Errors: '+str(wrongc)+bcolors.ENDC
	print bcolors.OKGREEN+'Total words:' +str(wordc)+bcolors.ENDC
	netwpm = grosswpm - (wrongc/(totalTime/60))
	print bcolors.BOLD+bcolors.OKGREEN+'\nOverall your Typing Speed is: '+str(netwpm)+'\n\n'+bcolors.ENDC
        addResult(str(netwpm))
        compareResult()