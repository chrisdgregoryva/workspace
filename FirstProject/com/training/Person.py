'''
Created on Feb 3, 2017

@author: cgregory
'''
class Person(object):
    def __init__(self, firstname="", lastname=""):
        self.firstname = firstname
        self.lastname = lastname
    def __str__(self):
        return self.firstname + " " + self.lastname

if __name__=='__main__':   
    p=Person('Chris', 'Gregory')
    print(p)

    
    