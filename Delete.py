#Required imports for Project
from All_imports import *
from CheckExists import *

#Conncetion To Other Function's of Project
def click(res,res2,res3,res4) :

    schedule.every(1).minutes.do(CheckExists,res,res2,res3,res4)

    while True :
        schedule.run_pending()
        time.sleep(1)

#Function To Stop Scheduling After Window is Closed
def Stop_Scheduling() :
    schedule.clear();
    return;

