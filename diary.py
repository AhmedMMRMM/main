'''
It should be announced that this code is for fun
'''




from os import listdir
import datetime



def openfile(filename):
    x = open(filename, 'r+')
    for c in x:
        print (c)
    return x
while 1:
    today = False
    ask = input('Do u wish to edit an old day? y or n\n')
    if ask in ['n', 'N','NO','no','nO','No']:
        todayy=str(datetime.date.today())+'.txt'
        if not (todayy in listdir()):
            create=open(todayy,'a')
            create.close()
        filing = todayy
    else:
        for d in listdir():
            print ('    ',d,sep='\n')

        filing=input('type the file you want then enter(without a format):\n') + '.txt'
    while 1:
        for d in listdir():
            print (d,sep='\n')

        file = openfile(filing)
        flag = True
        closure = False
        while 1:

            navi=''
            if flag:
                navi = 'type your lines:\n'
            written=input(navi)
            if written in ['exit','break','close','shut','quit']:
                closure=True
                break
            file.write(written+'\n')

            flag=False

        file.close()
        if closure==True:
            break


