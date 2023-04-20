import sys 
sys.path.append('C:/Users/USER/Desktop/CSIT314/Entity')
from staff import staff

class LoginController:
    def addStaff(self):
        print("in Controller")
        newStaff = staff()
        staff22 = staff.fuc()