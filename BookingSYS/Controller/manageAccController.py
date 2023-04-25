import sys 
sys.path.append( './Entity' )
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from accManage import accManage

class manageAccController:
    def manAcc(self, stackedWidget):
        self.stackedWidget = stackedWidget
        print("in Controller")
        newStaff = accManage()
        staff22 = newStaff.fuc(self.stackedWidget)