from datetime import datetime
import pandas as pd

def issue_book():
    book=pd.read_csv('book.csv')
    student=pd.read_csv('student.csv')
    order=pd.read_csv('order.csv')
    roll=int(input('Enter roll number: '))
    if(roll in list(student['roll'])):
        name=input('Enter book name: ')
        if(name in list(book['name'])):
            ind=list((book['name'])).index(name)
            if((book['qty'][ind]>0)):
                book.loc[ind,'qty']=book['qty'][ind]-1
                book.to_csv('book.csv',index=False)
                print('book has been issued')
            else:
                print('book out of stock')
        else:
        print('book name is invalid')
      else:
        print('invalid roll number')
issue_book()




