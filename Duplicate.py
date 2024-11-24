#Required Imports
from All_imports import *
from datetime import datetime
# import ctypes

k = 0;
start = time.time();

#Saving Project Report in Marvellous Folder and Sending Report To User using GMAIL Service
def Duplicate(duplicate,sendersemailadd,FolderName = 'Marvellous'):
    # print("Inside Duplicate Function")
    global start;
    global k; 
    Str = "-"*50;
    icnt = 0;
    i = 0;
    j = 0;
    l = 1;
    usersemailadd = "thechainsmokers78@gmail.com";
    password = "novk pyah rwvj pipx";
    
    # Your folder path and base file name
    # folder = "Marvellous"
    base_filename = "Marvellous"

    # Format the current timestamp in a file-safe way
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')  # This replaces colons with hyphens

    # Combine to create the file path
    file_name = f"{base_filename}{timestamp}.log"
    # file_path = os.path.join(folder, file_name)

    output = list(filter(lambda x : len(x) > 1,duplicate.values()))

    if not os.path.exists(FolderName) :
        os.mkdir(FolderName)
    
    File_Path = os.path.join(FolderName,file_name)
    k = k + 1
    
    fd = open(File_Path,'w',encoding='utf-8')
    fd.write("%sFinal Output of This Project%s\n" % (Str, Str))
    fd.write("\nDuplicate Files Names With Their Directory Names are:\n")

    # Writing the table headers
    fd.write("=" * 100 + "\n")  # Line separator for table
    fd.write(f"{'Duplicate Group'.ljust(20)}{'File Path'}\n")
    fd.write("=" * 100 + "\n")  # Line separator for table

    # Writing each group of duplicates in table format
    for index, duplicate_group in enumerate(output, start=1):
        fd.write(f"Group {index}:\n")
        for file_path in duplicate_group:
            fd.write(f"{''.ljust(20)}{file_path}\n")
        fd.write("\n")  # Blank line between groups for clarity
   
    fd.write("=" * 100 + "\n")  # Line separator for table

    #Point Where Duplicate Files Are Deleted Present in Specified Directory
    fd.write("Path Deleted are : \n")
    for result in output :
        icnt = 0
        for path in result :
            icnt += 1
            i += 1
            value = [] 
            if icnt >= 2 :
                fd.write("%d.%s\n"%(l,path));
                j+=1;
                os.remove(path);
                l+=1;
    
    fd.write("=" * 100 + "\n")  # Line separator for table

    fd.write("Total Numbers of Duplicate Files in Entered Directory are : %d\n"%i)
    fd.write("Number of Files After Deleteing Duplicate Files are : %d\n"%(i - j))
    fd.write("%sThank You For Using This Application Now You Can Check Your Directory%s"%(Str,Str));

    end = time.time();
    Time = end - start;
    fd.write("\nTime Taken BY Program is : %.2f min :"%(Time / 60));
    
    #Accepting Email Addresses and Password
    EMAIL_ADDRESS = usersemailadd;
    EMAIL_PASSWORD = password;
    sentTo = sendersemailadd;
    # print(EMAIL_ADDRESS);
    # print(EMAIL_PASSWORD);
    # print(sentTo);
    subject = "Report Of Duplicate Files Deleted"
    message = "Following is The Report of Duplicate Files Deleted Present in Entered Server Directory Path"

    #Using GMAIL Service to Send Report 
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = sentTo
    msg['Subject'] = subject

    filename = os.path.basename(File_Path)
    fd = open((File_Path),'rb')
    part = MIMEBase('application','octet-stream')
    part.set_payload((fd).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= %s"%filename)

    msg.attach(part)
    msg.attach(MIMEText(message));

    #Secure Connection To GMAIL Servers
    
    try :
        server = smtplib.SMTP_SSL('smtp.gmail.com',465);
        server.login(EMAIL_ADDRESS,EMAIL_PASSWORD);
        text = msg.as_string();
        server.sendmail(EMAIL_ADDRESS,sentTo,text);
        server.quit();

        messagebox.showinfo("Message","Duplicate Files Deleted Successfully, For Detailed Report Please Check Your Mail!!");

    except :
        print("Exception Occured While Sending Mail");
        messagebox.showerror("Error","Unable To Send Mail Please Enter Valid Email ID's and Password");

    #ctypes.windll.user32.MessageBoxW(0, "File deletion completed successfully For Report Please Check Your Mail!", "File Deletion", 1)

# def Duplicate(duplicate,usersemailadd,password,sendersemailadd,FolderName = 'Marvellous'):
#     # print("Inside Duplicate Function")
#     global start
#     global k 
#     icnt = 0;
#     i = 0;
#     j = 0;
#     usersemailadd = "thechainsmokers78@gmail.com";
#     password = "novk pyah rwvj pipx";

#     output = list(filter(lambda x : len(x) > 1,duplicate.values()))

#     if not os.path.exists(FolderName) :
#         os.mkdir(FolderName)
    
#     File_Path = os.path.join(FolderName,"Marvellous%d.txt"%k)
#     k = k + 1
    
#     fd = open(File_Path,'w',encoding='utf-8')
#     fd.write("------------------------------------Final Output of This Project------------------------------------\n")
#     fd.write("\nDuplicate Files Names With There Directory Names are : %s\n"%output)

#     #Point Where Duplicate Files Are Deleted Present in Specified Directory
#     fd.write("\nPath Deleted are : ")
#     for result in output :
#         icnt = 0
#         for path in result :
#             icnt += 1
#             i += 1
#             value = [] 
#             if icnt >= 2 :
#                 fd.write("%s, "%path);
#                 j+=1;
#                 os.remove(path);
    

#     fd.write("\n\nTotal Numbers of Duplicate Files in Entered Directory are : %d\n"%i)
#     fd.write("\nNumber of Files After Deleteing Duplicate Files are : %d\n"%(i - j))
#     fd.write("\n---------------------Thank You For Using This Application Now You Can Check Your Directory--------------------")

#     end = time.time();
#     Time = end - start;
#     fd.write("\nTime Taken BY Program is : %.2f min :"%(Time / 60));
    
#     #Accepting Email Addresses and Password
#     EMAIL_ADDRESS = usersemailadd;
#     EMAIL_PASSWORD = password;
#     sentTo = sendersemailadd;
#     # print(EMAIL_ADDRESS);
#     # print(EMAIL_PASSWORD);
#     # print(sentTo);
#     subject = "Report Of Duplicate Files Deleted"
#     message = "Following is The Report of Duplicate Files Deleted Present in Entered Server Directory Path"

#     #Using GMAIL Service to Send Report 
#     msg = MIMEMultipart()
#     msg['From'] = EMAIL_ADDRESS
#     msg['To'] = sentTo
#     msg['Subject'] = subject

#     filename = os.path.basename(File_Path)
#     fd = open((File_Path),'rb')
#     part = MIMEBase('application','octet-stream')
#     part.set_payload((fd).read())
#     encoders.encode_base64(part)
#     part.add_header('Content-Disposition',"attachment; filename= %s"%filename)

#     msg.attach(part)
#     msg.attach(MIMEText(message));

#     #Secure Connection To GMAIL Servers
    
#     try :
#         server = smtplib.SMTP_SSL('smtp.gmail.com',465);
#         server.login(EMAIL_ADDRESS,EMAIL_PASSWORD);
#         text = msg.as_string();
#         server.sendmail(EMAIL_ADDRESS,sentTo,text);
#         server.quit();

#         messagebox.showinfo("Message","Duplicate Files Deleted Successfully, For Detailed Report Please Check Your Mail!!");

#     except :
#         print("Exception Occured While Sending Mail");
#         messagebox.showerror("Error","Unable To Send Mail Please Enter Valid Email ID's and Password");

#     #ctypes.windll.user32.MessageBoxW(0, "File deletion completed successfully For Report Please Check Your Mail!", "File Deletion", 1)