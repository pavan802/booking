from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def singleton(arg):
    l=[]
    def inner():
        if len(l)==0:
            obj=arg()
            l.append(obj)
        return l[0]
    return inner
@singleton
class movie1():
    def __init__(self):
        self.totalticket=200
    def booking(self):
        reqticket=int(input('enter the no.of ticket:'))
        if reqticket<=self.totalticket:
            print('ticket booked successfully...')
            self.totalticket-=reqticket
            print(f' available tickets are{self.totalticket}')
        else:
            print('tickets not available')

@singleton
class movie2():
    def __init__(self):
        self.totalticket=200
    def booking(self):
        reqticket=int(input('enter the no.of ticket:'))
        if reqticket<=self.totalticket:
            print('ticket booked successfully...')
            self.totalticket-=reqticket
            print(f' available tickets are{self.totalticket}')
        else:
            print('tickets not available')

@singleton
class movie3():
    def __init__(self):
        self.totalticket=200
    def booking(self):
        reqticket=int(input('enter the no.of ticket:'))
        if reqticket<=self.totalticket:
            print('ticket booked successfully...')
            self.totalticket-=reqticket
            print(f' available tickets are{self.totalticket}')
        else:
            print('tickets not available')
def bmyshow(self):
    print('1. movie1 \n 2.movie2 \n 3.movie3')
    choice=int(input('enter the movie choice'))
    if choice==1:
        user=movie1()
        user.booking()
    if choice==2:
        user=movie2()
        user.booking()
    if choice==3:
        user=movie3()
        user.booking()
    else:
        print('no movie available')
user=bmyshow()
user.booking()
print('-'*20)

    


