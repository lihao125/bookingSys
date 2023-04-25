import sys 
sys.path.append( './Entity' )
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from backB import backB

class backButtonController:
    def backButtonC(self, stackedWidget):
        self.stackedWidget = stackedWidget
        print("in Controller")
        newStaff = backB()
        staff22 = newStaff.fuc(self.stackedWidget)