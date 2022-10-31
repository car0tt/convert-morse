import unidecode

def TtM(minput):
    minput = unidecode.unidecode(minput.lower())
    morsePI = open('morse.txt', 'r')
    morseI = (morsePI.read()).split('\n')
    moutput = ''
    for mi in minput:
        if mi == ' ':
            exit
        else:
            res=mi.isalpha()
            if res == False:
                res = mi.isnumeric()
                if res == False:
                    print('error special characters have not been translated')
    for m in list(minput.strip()):
        
        if m == ' ':
            moutput = moutput + '   '
        else:
            for i in morseI:
                if m == i[0]:
                    moutput = moutput + i[1:]
                    break
            moutput = moutput + ' '
    morsePI.close()
    if moutput == '':
        print('error')
    else:
        print(moutput)

import re
def special_match(strg, search=re.compile(r"[^'='-.-'   '-' ']").search):
    return not bool(search(strg))

def MtT(minput):
    vinput = special_match(minput)
    morseFI = open('morse.txt', 'r')
    morseI = (morseFI.read()).split('\n')
    moutput = ''
    sp_suit = 0
    if vinput:
        for m in minput.split(' '):
            if m == '':
                sp_suit += 1
                if sp_suit == 3:
                    moutput = moutput + ' '
            else:
                sp_suit = 0
                for i in morseI:
                    if m == i[1:]:
                        moutput = moutput + i[0]
                        break
    else:
        print("error")
    morseFI.close()
    print(moutput)