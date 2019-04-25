
# coding: utf-8

# In[ ]:


import random
myList=['rock', 'scissors','paper']


while True:
    r1= input("make a move!(rock/scissors/paper)")
    r2= random.choice(myList)
    print('You chose ' + r1, 'and the computer chose '+ r2) 
    if r1 == r2:
        print('Try again! It\'s a draw')

    if r1 == 'rock'and r2 ==('scissors'or 'paper'):
        print('You win!')

    if r1 == 'scissors' and r2=='paper':
        print('You win!')
    if r1 == 'paper':
        print('You lose!')
    else:
        print ('Do you want to play again?') 

    answer = input('y/n')
    if answer == 'y':
        continue
    else:
        print('Thanks! Bye')
        break

