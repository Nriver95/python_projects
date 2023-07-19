

class Protected:        #creates the class 
    def __init__(self):
        self._protectedVar = 420   # uses a single underscore to express that this variable is protected and should not be changed or used outside of the class, but can be changed.
        self.__privateVar = 7      # uses a double underscore to express that this variable is private and 

    def getPrivate(self):   #defines function "getPrivate" which will print"__privateVar)
        print(self.__privateVar)

    def setPrivate(self, private):  #defines a function "setPrivate" with the parameter 'private' and sets the private variable equal to the argument.
        self.__privateVar = private

obj = Protected() #sets obj to represent Protected() without having to type it out every time
obj._protectedVar = 360 #changes _protectedVar from within Protected() to equal 360
print(obj._protectedVar)#prints the variable
obj.getPrivate()    #uses obj to call the getPrivate() method which prints the private variable which equals 7
obj.setPrivate(777) #uses the method setPrivate() to change the private variable without directly interacting with it. setting it to whatever the argument is.
obj.getPrivate()    #again prints the private variable through the method getPrivate().

