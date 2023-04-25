import sys 
sys.path.append( './Entity' )
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from admin import admin

class adminLoginController:
    def addStaff(self, stackedWidget):
        self.stackedWidget = stackedWidget
        print("in Controller")
        newStaff = admin()
        staff22 = newStaff.fuc(self.stackedWidget)