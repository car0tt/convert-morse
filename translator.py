def TtM(minput):
    import unidecode
    minput = unidecode.unidecode(minput.lower())
    morsePI = open('morse.txt', 'r')
    morseI = (morsePI.read()).split('\n')
    moutput = ''
    for mi in minput:
        if mi == ' ':
            None
        else:
            res=mi.isalpha()
            if res == False:
                res = mi.isnumeric()
                if res == False:
                    print("error special characters can't be translated")
                    return
    for m in list(minput):
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

def MtT(minput):
    from data import special_match
    vinput = special_match(minput)
    morseFI = open('morse.txt', 'r')
    morseI = (morseFI.read()).split('\n')
    moutput = ''
    sp_suit = 0
    if minput == '' or minput == ' ' or minput == '*':
        print('error')
        morseFI.close()
        return
    elif vinput:
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
        print(moutput)
    else:
        print("error")
    morseFI.close()