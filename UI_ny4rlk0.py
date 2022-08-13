import os,subprocess,ctypes,time
fname=str(os.path.basename(__file__))
print(fname)
if ".py" in fname.lower():
    os.system("pip install tk")
    os.system('pip install requests')
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import requests as rq
cred="https://github.com/ny4rlk0/"
w=Tk();w.title('EDL MODE REBOOTER');w.configure(background='white');status='Waiting for user click.'
stat=Label (w, text=status ,background="white",font="none 12 bold");stat.place(rely=0, relx=0.3, x=0, y=0)
credit=Label (w, text=cred ,background="white",font="none 12 bold");credit.place(rely=0.8, relx=0.1, x=0, y=0)
w.geometry("400x200")

def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin
def download(url,filename):
    try:
        r = rq.get(url, allow_redirects=True)
        open(filename, 'wb').write(r.content)
    except:
        pass
def Main():
    os.system('edl.py reset')
    fixButton["state"] = "disabled"
    fixButton["text"] = "Waiting for device..."
    stat["text"] = "Waiting for device to connect..."
    #download("https://raw.githubusercontent.com/ny4rlk0/FixMyWindows/main/repairmywindows.bat","repairmywindows.bat")
    #subprocess.Popen("repairmywindows.bat")
def dl_python():
    download("https://www.python.org/ftp/python/3.10.6/python-3.10.6-amd64.exe","python3106x64.exe")
def install_python():
    ip["state"] = "disabled"
    stat["text"] = "Installing python... (Wait 2 min then click exit EDL)"
    dl_python()
    #os.system('python3106x64.exe /quiet InstallAllUsers=1 PrependPath=1 AssociateFiles=1 Include_symbols=1 TargetDir="C:\\Python"')
    subprocess.Popen('python3106x64.exe /quiet InstallAllUsers=1 PrependPath=1 AssociateFiles=1 Include_symbols=1 TargetDir="C:\\Python"')
if isAdmin():
    pass
else:
    messagebox.showinfo("Opps","This tool requires to run as Administrator. Will exit now!")
    os.sys.exit(0)
#fixButton
fixButton=Button(w,text="Exit From EDL",width=25,command=Main)
fixButton.place(rely=0.5, relx=0.5, x=0, y=0, anchor=S)
#fixButton
ip=Button(w,text="Install python",width=25,command=install_python)
ip.place(rely=0.7, relx=0.5, x=0, y=0, anchor=S)
w.mainloop()
os.sys.exit(0)