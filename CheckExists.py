#Required imports
from All_imports import *
from DirectoryTraversal import *
from Duplicate import *

#Directory Path Entry From Where Duplicate Files Have to be deleted
def CheckExits(DirectoryName,UsersEmailAdd,Password,SendersMailAdd) :
    duplicate = {}

    if not os.path.exists(DirectoryName) :
        print("Directory Not Found..")
        exit()
    else :
        duplicate = DirectoryTraversal(DirectoryName)
    
    Duplicate(duplicate,UsersEmailAdd,Password,SendersMailAdd)
