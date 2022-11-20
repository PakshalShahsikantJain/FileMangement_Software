######################################################################################################################################################################
##
##  Authors : Pakshal Shashikant Jain 
##  Date : 14/05/2021
##  Program/Project : File Management Software
##
#######################################################################################################################################################################

#Required Imports 

#All Reqiured Modules/Libraries Are Imported From This File
from All_imports import *

#Required Delete Package/Function To Delete Duplicate Files
from Delete import *

#Reuired Sorting Package/Function To Sort The Folder/Files
from Sort import *

#################################################################################################################################################################

def Click(window) :
    #Required Variables
    res = txt.get();
    res2 = txt2.get();
    res3 = txt3.get();
    
    if (len(res) == 0 or len(res2) == 0 or len(res3) == 0) :
        #Message Box Used To Display Specific Message
        messagebox.showinfo("Error : ","Please Fill Up The Required Data!\nTry Again!")
        window.destroy();
        main();
        return;

    txt.delete(0,END);
    txt2.delete(0,END);
    txt3.delete(0,END);

    #Asking User To Select Specific Directory Path To Delete Duplicate Files 
    filepath = filedialog.askdirectory(title="Dialog Box");
    if (len(filepath) == 0) :
        window.destroy();
        main();
        return;

    #Printing Values On Terminal for testing Purpose
    print("Admin Email Address : ",res);
    print("Password of Email Address: ",res2);
    print("Recipient's Email Address : ",res3);
    print("Directory Path  : ",filepath);
    
    #Call to click() function imported from Delete Package
    click(filepath,res,res2,res3);

##################################################################################################################

def SCRIPT(window) :
    window.destroy();

    #Second GUI(Window) of Software
    window2 = Tk()
    
    #Title of Second Window 
    window2.title("Folder Management Software")
    
    #Geometry of Second Window 
    window2.geometry('800x500')

    #Required Variables Declared(Globally)
    global txt;
    global txt2;
    global txt3;

    #Required Labels
    lbl = Label(window2,font=(20),text="Admin Email Address  : ")
    lbl2 = Label(window2,font=(20),text="Password (Email Address)  : ")
    lbl3 = Label(window2,font=(20),text = "Recipient's Email Address : ")

    #Setting Postion of Labels in Window
    lbl.grid(column=1, row=0,sticky= W,pady= 20)
    lbl2.grid(column= 1, row = 3,sticky=W,pady=20)
    lbl3.grid(column= 1, row = 6,sticky=W,pady=20)

    #Required Text Fiels
    txt = Entry(window2,width=50)
    txt2 = Entry(window2,show="*",width=50)
    txt3 = Entry(window2,width=50)

    #Setting Postion of Text Fields In Window
    txt.grid(column=2,row=0,pady = 20)
    txt2.grid(column= 2, row = 3,pady=20)
    txt3.grid(column= 2, row = 6,pady=20)

    #Label Used To Dispaly Notes
    Note =  Label(window2,font=("20"),foreground="Red",text="Note : Please Make Sure That Your Internet Connection is Turned On....!!")
    Note.place(relx = 0.5,rely=0.5,anchor=CENTER)

    #Using Below Button Click() Function is Called
    Btn = tkinter.Button(window2, text='Select Folder',font=(24),height=2,width=16,command=lambda : Click(window2),bg="Dark Gray",fg="white")
    Btn.place(relx = 0.3,rely=0.7,anchor=CENTER)

    #Using Below Button Close() Function is Called
    Quit_btn = tkinter.Button(window2, text="Close", font=(24),bg="Dark Gray",fg="white",height=2,width=16,command=lambda:Close(window2))
    Quit_btn.place(relx = 0.7,rely=0.7,anchor=CENTER);

##################################################################################################################################################

def Click2(window) :
    filepath = filedialog.askdirectory(title="Dialog Box");
    if (len(filepath) == 0) :
        window.destroy();
        main();
        return;

    #Call to Sort() function imported from Sort package
    Sort(filepath);

##################################################################################################################################################

def SORT(window) :
    window.destroy();

    #Third GUI(Window) of Software
    window3 = Tk()
    
    #Title of Third Window 
    window3.title("Folder Management Software")
    
    #Geometry(Size) of Third Window 
    window3.geometry('800x300')

    #Label Used To Display Warnings 
    Warning =  Label(window3,font=("20"),foreground="Dark Red",text="Warning : Don't Try To Sort Main OS Folder!!!!")
    Warning.place(relx = 0.5,rely=0.3,anchor=CENTER)

    #Using Below Button Click2() function is Called
    Btn = tkinter.Button(window3, text='Select Folder',font=(24),height=2,width=20,command=lambda:Click2(window3),bg="Dark Gray",fg="white")
    Btn.place(relx = 0.3,rely=0.6,anchor=CENTER)

    #Using Below Button Close() function is Called 
    Quit_btn = tkinter.Button(window3, text="Close", font=(24),bg="Dark Gray",fg="white",height=2,width=20,command=lambda:Close(window3))
    Quit_btn.place(relx = 0.7,rely=0.6,anchor=CENTER);

#############################################################################################################################################################

def Close(window) :
    window.destroy();
    main();

##############################################################################################################################################################

#First Function From Where Project Starts To Execute    
def main() :
    print("Jay Ganesh....");
    
    #First GUI(Window) of Software
    window = Tk()
    
    #Title of First Window 
    window.title("Folder Manangement Software")
    
    #Geometry(Size) of First Window
    window.geometry('1000x300')

    #Lable/Header
    Header =  Label(window,font=("Courier","30","italic","bold"),foreground="Dark Magenta",text="Marvellous Softwares")
    Header.place(relx = 0.5,rely=0.3,anchor=CENTER)
    
    #Buttons Used in First Window

    #Using Below Button SORT() function is Called
    Btn = tkinter.Button(window, text='Sort',font=(24),height=2,width=20,command = lambda:SORT(window),bg="Dark Gray",fg="white")
    Btn.place(relx = 0.2,rely=0.6,anchor=CENTER)

    #Using Below Button SCRIPT() function is Called 
    Btn2 = tkinter.Button(window, text='Delete Duplicate Files',font=(24),height=2,width=25,command=lambda:SCRIPT(window),bg="Dark Gray",fg="white")
    Btn2.place(relx = 0.5,rely=0.6,anchor=CENTER)
    
    #Using Below Button Whole Project is Closed
    Quit_btn = tkinter.Button(window, text="Close", font=(24),bg="Dark Gray",fg="white",height=2,width=20,command=window.destroy)
    Quit_btn.place(relx = 0.8,rely=0.6,anchor=CENTER);

    window.mainloop()

#Starting Point of Project
if __name__ == "__main__" :
    #Call To main() function
    main();