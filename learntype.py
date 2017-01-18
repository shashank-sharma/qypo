from bs4 import BeautifulSoup
import time
import requests
from random import randint

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
        que.append(y)
    return check

print 'LearnType - Make typing interesting'
print '"Increase your typing speed by reading quotes"'
raw_input('Press Enter to continue...')
print '\ntip: Make sure everything is exactly typed same'
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
            x+=1
            if x == 5:
                print 'Check your internet connetion'
                end()
                break
print '\n\nAll ready'
print 'Starting in '
time.sleep(1)
print '3'
time.sleep(1)
print '2'
time.sleep(1)
print '1'
time.sleep(1)
print '\n'
totalTime = 0
totalWords = 0
testingArea = []
for i in text:
    t = time.time()
    print i
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
                print text[i][j],'--------',testingArea[i][j]
                print text[i],'--------',testingArea[i]
                wrongc += 1
        except:
            wrongc += 1
grosswpm = ((wordc+wrongc)/5)/(totalTime/60)
print '\n\n\nTotal time: ', totalTime
print 'Gross WPM:',grosswpm
print 'Total Errors:',wrongc
print 'Total words:',wordc
netwpm = grosswpm - (wrongc/(totalTime/60))
print '\nOverall your Typing Speed is:',netwpm