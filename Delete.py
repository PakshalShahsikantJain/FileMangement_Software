#Required imports for Project
from All_imports import *
from CheckExists import *

#Conncetion To Other Function's of Project
def click(res,res2,res3,res4) :

    schedule.every(1).minutes.do(CheckExits,res,res2,res3,res4)

    while True :
        schedule.run_pending()
        time.sleep(1)



