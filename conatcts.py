'''
It should be announced that this code is for fun
'''


from time import sleep
import pickle
class card:
    def __init__(self,name = '',email = '',adress = '', phone = '',user = ''):
        self.name = name
        self.email = email
        self.adress = adress
        self.phone = phone
        self.user = user
    def show(self):
        print('\n @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
              ,self.name,self.email,self.adress, self.phone
              ,'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ \n'
              ,'log by',user,'\n'
              ,sep = '\n' )
flag = True
 
pickle_in = open('cont.pickle','rb')
contacts = pickle.load(pickle_in)
pickle_in.close()
user = input('May I be honor by knowing your name sir? (name)')
while flag:
    print('Sir , Would like an over view of your contacts? yes or no')
    if input()== 'yes':
        print('With pleasue master' , user)
        for i in range(len(contacts)):
            contacts[i].show()
    else:
        print('Fine sir, Would you like to add any contacts of yours? yes or no')
        if input()=='yes':
            print('Please insert name , email , adress ,phone(don\'t forget to enter each sir)')
            contacts.append(card(input(),input(),input(),input()))
        else :
            print('As you wish master',user ,'\n I \'m wondering if you want to continue sir? yes or no')
            if input()=='no':
                print('Perhaps another time sir, have a good day....')
                sleep(3)
                flag = False
            else:
                print('ok sir')
    #cont1 = card('ahmed','ahmed@ah','221b Baker st','07775000')
pickle_out = open('cont.pickle','wb')
pickle.dump(contacts , pickle_out)
pickle_out.close()
exit()
