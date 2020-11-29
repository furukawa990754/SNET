# coding: utf-8
import tkinter
from tkinter import ttk
import subprocess
import sys
import time
import threading
from tkinter import messagebox
import os,pickle
import winsound
import copy
import hashlib
import shutil
import traceback
import configparser
import tkinter.filedialog
import random
import base64

print('')
print(' GUIを操作してください')

def resourcePath(filename):
  if hasattr(sys, "_MEIPASS"):
      return os.path.join(sys._MEIPASS, filename)
  return os.path.join(filename)
ccf=0
try:

    def dcall(event):
        thread1 = threading.Thread(target=opendec,args=(event,))
        thread1.start()
        return "break"

    def Decall(event):
        thread1 = threading.Thread(target=openDecy,args=(event,))
        thread1.start()
        return "break"

    def butd():
        Button.config(state="disable")
        Button2.config(state="disable")
        Button3.config(state="disable")
        root.withdraw()
        return "break"

    def buta():
        root.deiconify()
        Button.config(state="active")
        Button2.config(state="active")
        Button3.config(state="active")
        return "break"

    def exitf(event):
        ret=messagebox.askyesno("VM manager", "このプログラムを終了しますか?")
        if ret==True:
            try:
               from subprocess import DEVNULL
            except ImportError:
               DEVNULL = os.open(os.devnull, os.O_RDWR)
            c=subprocess.check_output("java -jar "+resourcePath("resources/Task.jar"), stdin=DEVNULL, stderr=DEVNULL,shell=True)
        else:
            return "break"

    def opendec(event):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        try:
                config = configparser.ConfigParser()
                config.read("resources/config/config.conf")
                typ=config['type'].get('type')
                ens=config['type'].get('active')
                ens=int(ens)
                typ=int(typ)
                fTyp = [("DATファイル", "*.dat")]
                iDir = os.path.abspath("./resources/profile/")
                ile_name = tkinter.filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)
                if ile_name=="" or ile_name==None:
                    messagebox.showwarning("VM manager", "仮想マシンの起動処理を中止します。")
                    return "break"
                with open(ile_name, 'rb') as web:
                    intf1 = pickle.load(web)
                intf1s=copy.copy(intf1[0])
                intf1[0]=base64.b64decode(intf1s).decode()
                hashd = hashlib.md5(intf1[0].encode() ).hexdigest()
                hashs=[intf1[0],hashd]
                if hashs[1]!=intf1[1]:
                    messagebox.showerror("VM manager", "鍵認証に失敗しました、\n 仮想マシンの起動処理を中止します。")
                    return "break"
                if typ==1 and ens==1:
                    uuid=copy.copy(intf)
                    intf1[0]=intf1[0]+" --type headless"
                    messagebox.showwarning("VM manager", "仮想マシンをヘッドレスモードで起動しようとしています。\n このモードを使用する際は接続を確立してください。\n このモードは時刻のずれ等の悪影響を仮想マシンに与える可能性があります")
        except:
            messagebox.showerror("VM manager", "例外が発生しました、\n エラーの詳細は「err.log」を参照してください。\n 仮想マシンの起動処理を中止します。")
            with open('./resources/log/error.log', 'a') as fs:
                traceback.print_exc(file=fs)
            return "break"
        uuid=copy.copy(intf1[0]) 
        try:
           from subprocess import DEVNULL
        except ImportError:
           DEVNULL = os.open(os.devnull, os.O_RDWR)
        dir="仮想マシン  \n UUID "+uuid+" を起動しますか?"
        ret=messagebox.askyesno("VM manager", dir) 
        if ret!=True:
            return "break"
        
        winsound.PlaySound("resources/wav/boot.wav", winsound.SND_FILENAME)
        try:
            uuid=" "+uuid
            c=subprocess.check_output("java -jar "+resourcePath("resources/startvm.jar")+uuid, stdin=DEVNULL, stderr=DEVNULL,shell=True)
        except:
            messagebox.showerror("VM manager", "例外が発生しました、\n エラーの詳細は「err.log」を参照してください。")
            with open('./resources/log/error.log', 'a') as fs:
                traceback.print_exc(file=fs)
                fs.write("\nこのエラーの発生後はプロセスの開放が正常に動作しない場合があるため、\n以下の操作を手動で行う必要があります。\n 「VM manager.exe」が存在する場合は以下のコマンドを実行\n「taskkill /f /pid VM manager.exe」\nここまでを簡単に実行できるファイルも出力しました「task.bat」です。\n このエラーはVMUUIDが間違っている可能性があることを意味します。")
                fs.write("\nエラーになった設定ファイルのセクションはSECTION"+index+"です。\n 以下のコマンドでUUIDを確認できます。\n\n 「VBoxManage list vms」")
            #subprocess.run(resourcePath("resources/task.bat"),shell=True)
            try:
               from subprocess import DEVNULL
            except ImportError:
               DEVNULL = os.open(os.devnull, os.O_RDWR)
        c=subprocess.check_output("java -jar "+resourcePath("resources/Task.jar"),stdin=DEVNULL, stderr=DEVNULL,shell=True)
        return "break"
    args = sys.argv
    with open("./resources/usr/user.dat", 'rb') as web:
        cgh = pickle.load(web)
    hashd = hashlib.md5(args[2].encode() ).hexdigest()
    

    if hashd!="f03278e848f875387c2083f5d838f207":
        sys.exit()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    root = tkinter.Tk()
    root.resizable(False, False)
    Static1 = tkinter.Label(text=u' ')
    Static4 = tkinter.Label(text=u' ')
    root.title(u"VM")
    root.geometry("200x100")
    root.iconbitmap(default="resources/icon/ifs.ico")
    Static1.pack()
    Static1.pack()

    Button = tkinter.Button(text=u'仮想マシン起動',font=("",10))
    Button.bind("<Button-1>",dcall) 
    Button.pack()
    if (os.getlogin()!=cgh and ccf==0):
        ret=messagebox.askyesno("VM manager", "使用されているユーザーが異なります。\nプロファイルを削除しますか?")
        if ret==True:
            try:
               from subprocess import DEVNULL
            except ImportError:
               DEVNULL = os.open(os.devnull, os.O_RDWR)
            c=subprocess.check_output("java -jar "+resourcePath("resources/clean.jar"),stdin=DEVNULL, stderr=DEVNULL,shell=True)
            with open("./resources/usr/user.dat", 'wb') as web:
                pickle.dump(os.getlogin(), web)
        ccf=1
    Static4 = tkinter.Label(text=u' ')
    Static4.pack()
    
    Button3 = tkinter.Button(text=u'閉じる',font=("",10))
    Button3.bind("<Button-1>",exitf)
    Button3.pack()

    Static3 = tkinter.Label(text=u' ')
    Static3.pack()

    root.mainloop()
except SystemExit:
    pass

except:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with open('./resources/log/error.log', 'a') as fs:
        traceback.print_exc(file=fs)
