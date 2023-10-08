###################################################################################################################################
##
##  Author : Pakshal Shashikant Jain 
##  Date : 21/05/2021
##  Program : Automated Python Script : Sorting of Files According To Their Extensions
##
###################################################################################################################################

from All_imports import *
import shutil 
import os

def Sort(path) :
    current_Directory = path
    
    i = 0

    for Folder,SubFolder,Filename in os.walk(path) :
        
        for file in Filename :
            arr = [] 
            brr = []
            brr.append(file)
            
            file_extension = os.path.splitext(file)[-1].lower()
            
            arr.append(file_extension)

            final_Directory = os.path.join(current_Directory,file_extension)
            
            if not os.path.exists(final_Directory) :
                os.mkdir(final_Directory)
            
            try : 
                for i in range(len(arr)) :
                    shutil.move(current_Directory+'/'+file,current_Directory+'/'+arr[i]+'/'+file);
            except FileNotFoundError :
                print("File Already Have Been Moved");
                messagebox.showinfo("Message","Files Sorted Successfully");
                return;
            except :
                print("Another Error Occured");
                return;
