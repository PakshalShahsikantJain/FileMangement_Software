#Required Imports
from All_imports import *

k = 0
start = time.time()

#Saving Project Report in Marvellous Folder and Sending Report To User using GMAIL Service
def Duplicate(duplicate,usersemailadd,password,sendersemailadd,FolderName = 'Marvellous'):
    global k 
    global start

    output = list(filter(lambda x : len(x) > 1,duplicate.values()))

    if not os.path.exists(FolderName) :
        os.mkdir(FolderName)

    File_Path = os.path.join(FolderName,"Marvellous%d.txt"%k)
    k = k + 1

    fd = open(File_Path,'w')
    fd.write("------------------------------------Final Output of This Project------------------------------------\n")
    fd.write("\nDuplicate Files Names With There Directory Names are : %s\n"%output)

    icnt = 0
    i = 0
    j = 0

    #Point Where Duplicate Files Are Deleted Present in Specified Directory
    fd.write("\nPath Deleted are : ")
    for result in output :
        icnt = 0
        for path in result :
            icnt += 1
            i += 1
            value = [] 
            if icnt >= 2 :
                fd.write("%s, "%path)
                j += 1
                os.remove(path)

    fd.write("\n\nTotal Numbers of Duplicate Files in Entered Directory are : %d\n"%i)
    fd.write("\nNumber of Files After Deleteing Duplicate Files are : %d\n"%j)
    fd.write("\n---------------------Thank You For Using This Application Now You Can Check Your Directory--------------------")

    end = time.time()
    Time = end - start
    fd.write("\nTime Taken BY Program is : %f sec :"%Time)

    #Accepting Email Addresses and Password
    EMAIL_ADDRESS = usersemailadd;
    EMAIL_PASSWORD = password;
    sentTo =  sendersemailadd;
    print(EMAIL_ADDRESS);
    print(EMAIL_PASSWORD);
    print(sentTo);
    subject = "Report Of Duplicate Files Deleted"
    message = "Follwing is The Report of Duplicate Files Deleted Present in Entered Server Directory Path"

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
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    text = msg.as_string()
    server.sendmail(EMAIL_ADDRESS,sentTo,text)
    server.quit()
