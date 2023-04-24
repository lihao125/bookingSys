import sys 
sys.path.append( 'C:/Users/Owner/Desktop/CSIT314/bookingSys/BookingSYS/Entity' )
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from admin import admin

class adminLoginController:
    def addStaff(self):
        print("in Controller")
        newStaff = admin()
        staff22 = admin.fuc()