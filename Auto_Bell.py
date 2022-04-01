from tkinter import *
import datetime
from pydub import playback,AudioSegment
from time import strftime
import tkinter.messagebox as messagebox
from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk
import time,socket,aysms
from functools import partial
from twilio.rest import Client
from configparser import ConfigParser
import os,sys,getpass,encoding,webbrowser



#paths
bell_ico='Sources/Images/bell_1.ico'
bell_png='Sources/Images/IMG_0431.PNG'
login_png='Sources/Images/IMG_0441.PNG'
exit_png='Sources/Images/IMG_0442.PNG'
scl_logo = "Sources/Images/2020-01-17 19.03.23.JPEG"
ay_jpg='Sources/Images/aystudios.jpg'
masty_img='Sources/Images/masty.png'
scl_jpg='Sources/Images/scl jpg.png'
fb='Sources/Images/fb.png'
shedule_list='Morning Assembly','Period 1','Period 2','Period 3','Period 4','Interval','Period 5','Period 6','Period 7','Period 8','Sweeping','End prayer'
        
def quitt():
    quit_message=messagebox.askquestion(' Exit AutoBell!','  Are You Sure Want to Exit the AutoBell App?  ',icon='warning')
    if quit_message=='yes':
        root.destroy()

def verification(command):
    loginpage(command=command)


#LoginWindow
def loginpage(command=None):
    try:
        auth=open('autobellAuth.dll').read()
    except:
        messagebox.showerror('error!','dll missing!! reinstall may fix the error!')
        root.destroy()
    ent=''
    for i in auth:
        ent=ent+encoding.decode[i]
    login_pass = str(ent)
    loginwindow =tk.Toplevel(root)
    loginwindow.geometry(f'500x300+{loginwindow.winfo_screenwidth()//3}+200')
    loginwindow.title('AutoBell - Verification')
    loginwindow.resizable(False,False)
    loginwindow.iconbitmap(bell_ico)
    loginwindow.grab_set()
    def login():
        password_1 = password.get()
        users =user_var.get()
        if users!='' and password_1!='':
            if login_pass == password_1:
                with open('users' + '.dll',"a+") as file_object:
                    file_object.write('('+(user_var.get().upper())+')'+' '+'('+time.strftime('%c').replace(' ','-')+')'+'\n')
                loginwindow.destroy()
                listbox_index('login','Logged in.')                                    
                if command=='ring':
                    msg_box=messagebox.askquestion(' Unsheduled Bell! ','''     This Bell is not in Shedule!
     Are you sure want to Ring?     ''',icon='warning')
                    if msg_box=='yes':
                        listbox_index('unshedule','Unsheduled Bell.') 
                        play(audios[0])
                        with open('IM_Bells' + '.dll',"a+") as file_object:
                            file_object.write('On '+(time.strftime('%c')+' Rang by '+(user_var.get()).upper()+'\n'))
                else:
                    command()
                    
            else:
                listbox_index('Tried','Security Warning!')
                messagebox.showerror(' error! ','    Incorrect Password!   ')                                
                with open('Tried_to_unlock' + '.dll','a+') as file_object:
                    file_object.write('('+(user_var.get().upper())+')'+' '+'('+password.get()+')'+' '+'('+time.strftime('%c').replace(' ','-')+')'+'\n')
                password.delete(0,'end')
                password.focus()
        else:
            listbox_index('Tried','Security Warning!')
            messagebox.showerror('Warning!','      Enter a valid username or Password!!      ')
            username.delete(0,'end')
            password.delete(0,'end')
            username.focus()
    user_var = StringVar()
    password_var = StringVar()


    def label(parent,text,font,x,y,fg = 'black'):
        ttk.Label(parent,text = text,font = font).place(x = x,y = y)

    panel = ttk.PanedWindow(loginwindow)
    panel.pack(expand = 1,fill = BOTH)

    label(panel,"Verify that you are an Authorized User!",('times',22,),30 , 25)
    
    label(panel,'username :',20,60,100)
    label(panel,'password :',20,60,140)
    
    username = ttk.Entry(panel,width = 40,textvar = user_var)
    username.focus()
    username.place(x = 150,y = 103)
    password = ttk.Entry(panel,width = 40,show = '•',textvar = password_var)
    password.place(x = 150,y = 143)
    ttk.Button(loginwindow,image = login_logo,command = login).place(x = 390,y = 200)
    ttk.Button(loginwindow,image = exit_logo,command =loginwindow.destroy).place(x = 50,y = 200)

    def exitt(key):
        loginwindow.destroy() 
    def Return(key):
            login()
    def down(key):
        if username.focus_get():
            password.focus()
    def up(key):
        if password.focus_get():
            username.focus()
    loginwindow.bind('<Return>',Return)
    loginwindow.bind('<Escape>',exitt)
    loginwindow.bind('<Down>',down)
    loginwindow.bind('<Up>',up)
    loginwindow.mainloop()

def savetofile():
    config=ConfigParser()
    config.add_section('setting')
    config.set('setting','assembly_time',assembly_time)
    config.set('setting','period1',period1)
    config.set('setting','period2',period2)
    config.set('setting','period3',period3)
    config.set('setting','period4',period4)
    config.set('setting','interval',interval)
    config.set('setting','period5',period5)
    config.set('setting','period6',period6)
    config.set('setting','period7',period7)
    config.set('setting','period8',period8)
    config.set('setting','sweep ',sweep )
    config.set('setting','end_prayer',end_prayer)
    with open('autoBell' + '.dll',"w") as configfile:
        config.write(configfile)
    try:listbox_index('shedule','Shedule Updated.')
    except:
        activity_listbox.delete('shedule')
        listbox_index('shedule','Shedule Updated.')
    finally:None
    messagebox.showinfo('Edit Shedule.','    Belling Shedule successfully Saved and Ready to Ring!!   ')  
                    
def shedule():
    setting=tk.Toplevel(root)
    setting.geometry(f'420x420+{setting.winfo_screenwidth()//3}+180')
    setting.title('AutoBell-Shedule')
    setting.resizable(False,False)
    setting.iconbitmap(bell_ico)
    setting.grab_set()
    Label(setting,text=" Edit Belling Shedule ",font=('times',18)).place(x=25,y=10)
    times=( assembly_time,period1,period2,period3,period4,interval,period5,period6,period7,period8,sweep,end_prayer)
    value_h=('00','01','02','03','04','05','06','07','08','09','10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23')
    value_m=('00','01','02','03','04','05','06','07','08','09','10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23','24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')


    def combo(y,i):
        combobox=ttk.Combobox(setting,width=5,state='readonly')
        combobox['values']=value_h
        combobox.place(x=150,y=y+30)
        combobox2=ttk.Combobox(setting,width=5,state='readonly')
        combobox.current(int(times[i].split(':')[0]))                                      
        combobox2['values']=value_m
        combobox2.current(int(times[i].split(':')[1]))
        combobox2.place(x=220,y=y+30)
        Label(setting,text=shedule_list[i]).place(x=30,y=y+30)
        return combobox,combobox2
       
    assem_h,assem_m=combo(30,0)
    p2_h,p2_m      =combo(90,2)
    p3_h,p3_m      =combo(120,3)
    p4_h,p4_m      =combo(150,4)
    int_h,int_m    =combo(180,5)
    p5_h,p5_m      =combo(210,6)
    p6_h,p6_m      =combo(240,7)
    p7_h,p7_m      =combo(270,8)
    p8_h,p8_m      =combo(300,9)
    sw_h,sw_m      =combo(330,10)
    ep_h,ep_m      =combo(360,11)
    def p1_auto():        
        p1_h.config(state='readonly')
        p1_m.config(state='readonly')
        p1_h.current('07')
        p1_m.current('45')
         
        
    def p1_manual():
        p1_h.config(state='disabled')
        p1_m.config(state='disabled')

    check=BooleanVar()    
    auto=Checkbutton(setting,text='Auto',onvalue=True,offvalue=False,variable=check,command=p1_auto)
    auto.place(x=280,y=90)
    manual=Checkbutton(setting,text='Manual',onvalue=False,offvalue=True,variable=check,command=p1_manual)
    manual.place(x=340,y=90)
        
    p1lbl=Label(setting,text=shedule_list[1])
    p1lbl.place(x=30,y=90)
    p1_h=ttk.Combobox(setting,width=5)
    p1_h['values']=value_h
    p1_m=ttk.Combobox(setting,width=5)
    p1_m['values']=value_m

    if period1=='Manual':
        check.set(False)
        p1_h.config(state='disabled')
        p1_m.config(state='disabled')

    else:
        check.set(True)
        p1_h.current(int(times[1].split(':')[0]))
        p1_m.current(int(times[1].split(':')[1]))    
    p1_h.place(x=150,y=90)
    p1_m.place(x=220,y=90)

                


    
    
    def save_changes():
        global assembly_time,period1,period2,period3,period4,interval,period5,period6,period7,period8,sweep,end_prayer
        if check.get()==True:
            period1=('%s:%s')%(p1_h.get(),p1_m.get())
        else:period1='Manual'
        assembly_time=('%s:%s')%(assem_h.get(),assem_m.get())
        period2 = ('%s:%s')%(p2_h.get(),p2_m.get())
        period3 = ('%s:%s')%(p3_h.get(),p3_m.get())
        period4 = ('%s:%s')%(p4_h.get(),p4_m.get())
        interval = ('%s:%s')%(int_h.get(),int_m.get())
        period5 = ('%s:%s')%(p5_h.get(),p5_m.get())
        period6 = ('%s:%s')%(p6_h.get(),p6_m.get())
        period7 = ('%s:%s')%(p7_h.get(),p7_m.get())
        period8 = ('%s:%s')%(p8_h.get(),p8_m.get())
        sweep =('%s:%s')%(sw_h.get(),sw_m.get())
        end_prayer =('%s:%s')%(ep_h.get(),ep_m.get())
        setting.destroy()
        savetofile()

    def restore_changes():
    
        global assembly_time,period1,period2,period3,period4,interval,period5,period6,period7,period8,sweep,end_prayer
        assembly_time = '07:25'
        period1       ='Manual'
        period2       = '08:30'
        period3       = '09:10'
        period4       = '09:50'
        interval      = '10:30'
        period5       = '10:50'
        period6       = '11:30'
        period7       = '12:10'
        period8       = '12:50'
        sweep         = '13:25'
        end_prayer    = '13:35'
        setting.destroy()
        savetofile()
        

    def Info():
        messagebox.showinfo(" Info. ",'''
   You can not set shedule for "Period-01" and "Final" Bells.
    A prompt will appear after the previous shedule of them.   ''')

       
    ttk.Button(setting,text='  Save  ',command=save_changes).place(x=325,y=300)
    ttk.Button(setting,text=' Reset ',command=restore_changes).place(x=325,y=330)
    ttk.Button(setting,text='  Info  ',command=Info).place(x=325,y=360)

    setting.mainloop()
#changepassword
def auth_config():
    def auth_win():
        def change():
            if cur.get()!='' and len(new.get())>=8 and con.get()!='':
                auth=open('autobellAuth.dll').read()
                ent=''
                for i in auth:
                    ent=ent+encoding.decode[i]
                    login_pass=str(ent)
                if cur.get() == login_pass:
                    if new.get()== con.get():
                        ent=''
                        for i in new.get():
                            ent=ent+encoding.encode[i]
                        with open('autobellAuth' + '.dll',"w+") as auth:
                            auth.write(ent)
                        setting.destroy()
                        try:
                            listbox_index('auth','Security Configured!')
                        except:
                            activity_listbox.delete('Tried')
                            listbox_index('auth','Security Configured!')
                        messagebox.showinfo('Success!','    AutoBell Security Configured Successfully!   ')
                        body='Password Changed to %s On %s..' %(new.get(),time.strftime('%G-%B-%d'))
                        Client=aysms.Client
                        Client.messages.create(to=aysms.ay,from_=aysms.ay2,body=str(body))
                    else:
                        messagebox.showerror('error!',"  New Password doesn't match!  ")
                        cur_pass.delete(0,'end')
                        new_pass.delete(0,'end')
                        con_pass.delete(0,'end')
                        cur_pass.focus()
                else:
                    try:
                        listbox_index('Tried','Security Warning!')
                    except:
                        activity_listbox.delete('Tried')
                        listbox_index('Tried','Security Warning!')
                    messagebox.showerror('error!','   Incorrect password!  ')
                    setting.destroy()
                    verification(auth_config)
            else:
                messagebox.showwarning('warning!','  Password Must be Minimum 8 Characters!  ')
                cur_pass.delete(0,'end')
                new_pass.delete(0,'end')
                con_pass.delete(0,'end')
                cur_pass.focus()
                
        setting=tk.Toplevel(root)
        setting.grab_set()
        panel = ttk.PanedWindow(setting)
        panel.pack(expand = 1,fill = BOTH)
        setting.geometry(f'500x300+{setting.winfo_screenwidth()//3}+200')
        setting.resizable(0,0)
        setting.title('AutoBell-Security')
        setting.iconbitmap(bell_ico)
        cha=lambda event:change()
        def down(key):
            if cur_pass.focus_get():
                new_pass.focus()
            elif new_pass.focus_get():
                con_pass.focus()
        def up(key):
            if con_pass.focus_get():
                new_pass.focus()
            elif new_pass.focus_get():
                cur_pass.focus()
        setting.bind('<Return>',cha)
        setting.bind('<Down>',down)
        setting.bind('<Up>',up)
        setting.bind('<Escape>',setting.destroy)
        Label(setting,text=" Security Configuration ",font=('times',19)).place(x=20,y=10)
        Label(setting,text='''
You need to choose a password which Include Numbers, Symbols,
 Capital Letters, Lower-case Letters that has Minimum 8 characters.''',font=(11)).place(x=5,y=40)
        Label(setting,text="Current Password").place(x=50,y=135)
        Label(setting,text="New Password").place(x=50,y=165)
        Label(setting,text="Confirm Password").place(x=50,y=195)
        ttk.Button(setting,text=' Continue ',command=change).place(x=310,y=250)
        ttk.Button(setting,text='    Close    ',command=setting.destroy).place(x=390,y=250)
        cur=StringVar()
        new=StringVar()
        con=StringVar()
        cur_pass=ttk.Entry(panel,width=30,textvar=cur)
        cur_pass.focus()
        cur_pass.place(x=180,y=135)
        new_pass=ttk.Entry(panel,width=30,textvar=new)
        new_pass.place(x=180,y=165)
        con_pass=ttk.Entry(panel,width=30,textvar=con)
        con_pass.place(x=180,y=195)
        setting.mainloop()
    #checkconnection
    try:
        socket.create_connection(('www.google.com',80))
        verification(auth_win)
    except:     
        messagebox.showerror('Connection Lost!',' Internet Connection Required to Configure Security! ')
    

try:
    config_0=ConfigParser()
    config_0.read('autoBell.dll')

    assembly_time = config_0.get('setting','assembly_time')
    period1 = config_0.get('setting','period1')
    period2 = config_0.get('setting','period2')
    period3 = config_0.get('setting','period3')
    period4 = config_0.get('setting','period4')
    interval = config_0.get('setting','interval')
    period5 = config_0.get('setting','period5')
    period6 = config_0.get('setting','period6')
    period7 = config_0.get('setting','period7')
    period8 = config_0.get('setting','period8')
    sweep = config_0.get('setting','sweep')
    end_prayer = config_0.get('setting','end_prayer')


except:
    assembly_time = '07:25'
    period1       ='Manual'
    period2       = '08:30'
    period3       = '09:10'
    period4       = '09:50'
    interval      = '10:30'
    period5       = '10:50'
    period6       = '11:30'
    period7       = '12:10'
    period8       = '12:50'
    sweep         = '13:25'
    end_prayer    = '13:35'
    savetofile()

    

def security():
    security_window = Toplevel(root)
    security_window.title("AutoBell - Security Breachers")
    security_window.geometry(f'500x400+{root.winfo_screenwidth()//3}+180')
    security_window.iconbitmap(bell_ico)
        
    frame = ttk.PanedWindow(security_window)
    frame.pack(expand = 1,fill = BOTH)

    scrollbar = ttk.Scrollbar(frame)
    scrollbar.pack(side = RIGHT,fill = Y)

    listbox = ttk.Treeview(frame,yscrollcommand = scrollbar.set)
    listbox.pack(expand = 1,fill = BOTH)
    listbox.heading('#0',text = 'Username , Used Password , Date&Time')
    users=open('Tried_to_unlock.dll','r').readlines()
    def del_unsh():
        if len(users)!=0:
            with open('Tried_to_unlock.dll','w') as users_:
                users_.write('')
            security_window.destroy()
            messagebox.showinfo('Success','   Cleaned! ')
            security()
        else:
            messagebox.showinfo('Empty','   No Data Found !')
            security_window.focus()
    if len(users)!=0:
        for name in users:
            listbox.insert('','end',name,text = name)        

    else:
        listbox.insert('','0','none',text = 'No Data Found!')
    ttk.Button(security_window,text=' Clear Data ',command=del_unsh).place(x=370,y=312)

    scrollbar.config(command = listbox.yview)

def unsheduled():
    emergency_window = Toplevel(root)
    emergency_window.title("AotoBell-Unsheduled Bell info")
    emergency_window.geometry(f'500x400+{emergency_window.winfo_screenwidth()//3}+180')
    emergency_window.iconbitmap(bell_ico)
    emergency_window.grab_set()  
    frame = ttk.PanedWindow(emergency_window)
    frame.pack(expand = 1,fill = BOTH)

    scrollbar = ttk.Scrollbar(frame)
    scrollbar.pack(side = RIGHT,fill = Y)
    imbells_file=open('IM_Bells.dll','r').readlines()
    def del_unsh():
        if len(imbells_file)!=0:
            with open('IM_Bells.dll','w') as imbells:
                imbells.write('')
            emergency_window.destroy()
            messagebox.showinfo('Success','  Cleaned! ')
            unsheduled()
        else:
            messagebox.showinfo('Empty',' List is Empty! ')
            emergency_window.focus()
    ttk.Button(emergency_window,text=' Clear Data ',command=del_unsh).place(x=370,y=312)
    ttk.Button(emergency_window,text='      Close      ',command=emergency_window.destroy).place(x=370,y=343)
    

    listbox = ttk.Treeview(frame,yscrollcommand = scrollbar.set)
    listbox.pack(expand = 1,fill = BOTH)
    listbox.heading('#0',text = 'Date & Time , User Name')
    imbells_file=open('IM_Bells.dll','r').readlines()
    if len(imbells_file)!=0:
        for i in range(0,len(imbells_file)):
            listbox.insert('','end',i,text = imbells_file[i])
    else:listbox.insert('','end',text = '  No Data Found!')
                   
    scrollbar.config(command = listbox.yview)

def view_shedule():
    view_shedule_window = Toplevel(root)
    view_shedule_window.title("AutoBell-Shedule")
    view_shedule_window.geometry(f'500x400+{view_shedule_window.winfo_screenwidth()//3}+180')
    view_shedule_window.iconbitmap(bell_ico)
    view_shedule_window.grab_set()
    view_shedule_window.resizable(0,0)
    frame = ttk.PanedWindow(view_shedule_window)
    frame.pack(expand = 1,fill = BOTH)

    listbox = ttk.Treeview(frame)
    listbox.pack(fill = BOTH,expand=1)
    listbox.heading('#0',text = 'AutoBell Shedule')
    listbox.config(column = ('Time'))
    listbox.heading('Time',text = " Time ")
    def edit_view():
        view_shedule_window.destroy()
        verification(shedule)
    ttk.Button(view_shedule_window,text='  Edit  ',command=edit_view).place(x=280,y=320)
    ttk.Button(view_shedule_window,text=' Close ',command=view_shedule_window.destroy).place(x=360,y=320)
    times=( assembly_time,period1,period2,period3,period4,interval,period5,period6,period7,period8,sweep,end_prayer)

    def all_shedules():
        global viewshedules_
        for i in range(0,12):
            listbox.insert('','end','p%s'%(viewshedules_),text = shedule_list[i])
            listbox.set('p%s'%(viewshedules_),'Time',times[i])
            viewshedules_=viewshedules_+1
    all_shedules()
viewshedules_=1   



def about_autobell():
    about_win=Toplevel(root)
    about_win.title('About AutoBell 1.0 ')
    about_win.geometry(f'300x450+500+120')
    about_win.iconbitmap(bell_ico)
    about_win.resizable(0,0)
    about_win.grab_set()
    Label(about_win,text='AutoBell v1.0',fg='darkred',font=('times',20)).place(x=85,y=55)
    Label(about_win,text="""Automatic Belling System
     of St.Anthony's T.M.V Col-14.""",font=('calbri')).place(x=1,y=150)
    Label(about_win,image=bell_img).place(x=10,y=20)
    Label(about_win,text='About',font=('italic')).place(x=130,y=297)
    def readme():
        webbrowser.open('README.txt')
    ttk.Button(about_win,text='          Developers         ',command=about_developers).place(x=95,y=355)
    ttk.Button(about_win,text=' README ',command=readme).place(x=10,y=415)
    ttk.Button(about_win,text=' Close ',command=about_win.destroy).place(x=215,y=415)
    ttk.Button(about_win,text="  St.Anthony's T.M.V  ",command=about_school).place(x=95,y=320)
    
    
    
def about_developers():
    about_us = Toplevel(root)
    about_us.title("AutoBell - About Developers.")
    about_us.geometry(f'500x400+{about_us.winfo_screenwidth()//3}+180')
    about_us.iconbitmap(bell_ico)
    about_us.resizable(0,0)
    about_us.grab_set()
    Canvas(about_us,width=1000,height = 47,background='indianred',highlightthickness = 0).place(x=0,y=7)
    Canvas(about_us,width=1000,height = 47,background='gray',highlightthickness = 0).place(x=0,y=118)
    Canvas(about_us,width=1000,height = 40,background='indianred',highlightthickness = 0).place(x=0,y=216)

    Label(about_us,image=ay,relief='groove').place(x=122,y=70)
    Label(about_us,image=masty,relief='groove').place(x=244,y=70)
    Label(about_us,text=" We're Here :) ",fg='black',bg='indianred',font=('times',25,'bold')).place(x=20,y=10)
    Label(about_us,text="Contact Us.",fg='black',bg='indianred',font=('calibri',20,'bold')).place(x=10,y=216)
    Label(about_us,text="""+94764718304.
yuwankmr@gmail.com""",fg='blue',justify=LEFT,font=('arial',17)).place(x=20,y=258)
    def ayfacebook():
        webbrowser.open('https://www.facebook.com/iamanistanyoganath/')
    ttk.Button(about_us,text='Follow us on FaceBook',command=ayfacebook).place(x=303,y=370)
    ttk.Button(about_us,image=fblogo,command=ayfacebook).place(x=333,y=300)
    def ayweb():
        webbrowser.open('http://aystudios.website2.me')
    Button(about_us,text='aystudios.website2.me',command=ayweb,activeforeground='black',fg='gray28',border=0,justify=LEFT,font=('arial',17)).place(x=20,y=314)

    


def about_school():
    
    about_school = Toplevel(root)
    about_school.title("AutoBell - About School.")
    about_school.geometry(f'500x400+{about_school.winfo_screenwidth()//3}+180')
    about_school.iconbitmap(bell_ico)
    about_school.resizable(0,0)
    about_school.grab_set()
    Label(about_school,image=abt_scl,relief='groove').place(x=0,y=0)
    def fb():
        webbrowser.open('https://www.facebook.com/CSt-Anthonys-Tamil-Maha-Vidyalayam-Col-14-102566854626267/')
    ttk.Button(about_school,image=fblogo2,command=fb).place(x=139,y=362)
    Button(about_school,text=' Follow us on  ~',command=fb,border=0,font=('arial',12,'bold')).place(x=5,y=367)




#mainwindow
root=tk.Tk()
root.resizable(0,0)
root.geometry(f'1000x550+{root.winfo_screenwidth()//8}+60')
root.title("AutoBell-St.Anthony's T.M.V")
root.iconbitmap(bell_ico)
root.protocol('WM_DELETE_WINDOW',lambda:verification(quitt))
#menubarRoot    
menubar=Menu(root)    
filemenu=Menu(menubar,tearoff=0)
settingmenu=Menu(menubar,tearoff=0)
helpmenu=Menu(menubar,tearoff=0)


menubar.add_cascade(label='File',menu=filemenu)
menubar.add_cascade(label='Settings',menu=settingmenu)
menubar.add_cascade(label='Help',menu=helpmenu)


filemenu.add_command(label='Show Schedule',command = view_shedule)
filemenu.add_command(label='Show security Breachers',command=lambda:verification(security))
filemenu.add_command(label='Show Unsheduled bell info',command=lambda:verification(unsheduled))

filemenu.add_separator()        
filemenu.add_command(label='Exit',command=lambda:verification(quitt))

settingmenu.add_command(label='Edit Bell Shedule',command  = lambda:verification(shedule))
settingmenu.add_separator()
settingmenu.add_command(label='AutoBell Security',command=auth_config)


helpmenu.add_command(label='About AutoBell',command=about_autobell)
helpmenu.add_command(label='AutoBell Help',command=lambda:webbrowser.open('Help.txt'))
helpmenu.add_separator()
helpmenu.add_command(label='About School',command=about_school)
helpmenu.add_command(label='About Developers',command=about_developers)

root.config(menu=menubar)

#keybinding
es=lambda key:verification(quitt)
cs=lambda key:view_shedule()
cb=lambda key:verification(security)
cu=lambda key:verification(unsheduled)
ce=lambda key:verification(setting)
ci=lambda key:auth_config()
root.bind('<Escape>',es)    
root.bind('<Control-s>',cs)
root.bind('<Control-b>',cb)
root.bind('<Control-u>',cu)
root.bind('<Control-e>',ce)
root.bind('<Control-i>',ci)

def img(path,size):
    img = Image.open(path).resize(size)
    return ImageTk.PhotoImage(img)
#resizeImages
masty=img(masty_img,(135,120))
masty1=img(masty_img,(55,40))
ay=img(ay_jpg,(120,120))
ay1=img(ay_jpg,(40,40))
sl_logo=img(scl_logo,(110,110))
bell_img=img(bell_png,(70,70))
login_logo = img(login_png,(60,60))
abt_scl=img(scl_jpg,(500,360))
fblogo=img(fb,(57,57))
fblogo2=img(fb,(30,30))

exit_logo=img(exit_png,(60,60))
Canvas(root,width=1000,height = 140,background='indianred',highlightthickness = 0).place(x=0,y=245)
Canvas(root,width=1000,height = 95,background='gray',highlightthickness = 0).place(x=0,y=385)



Label(root,text=" ST.ANTHONY'S T.M.V COL-14 ",fg='darkred',font=("Times",32,"bold")).place(x=120,y=10)
Label(root,text=" Automatic Belling System. ",fg='black',font=("Harlow Solid Italic",30)).place(x=120,y=70)
Label(root,image=sl_logo,relief='groove').place(x=10,y=10)
describes=Label(root,text='Starting..',bg='indianred',justify=CENTER,font=('book antiqua',50))
describes.place(x=28,y=270)
Label(root,text=" Now : ",bg='indianred',font=('',13)).place(x=10,y=256)
Label(root,text=" Pre.Bell : ",bg='gray',font=('',13)).place(x=10,y=390)
Label(root,text=" Nxt.Bell : ",bg='gray',font=('',13)).place(x=500,y=390)
Label(root,text="This Automatic Bell System Was Developed By AY Studios in Associated with Mast.Y Studios. ",fg='gray28',font=("",13)).place(x=5,y=505)
Label(root,image=masty1,relief='groove').place(x=748,y=484)
Label(root,image=ay1,relief='groove').place(x=698,y=484)        
Next=Label(root,bg='gray',justify=LEFT,font=('book antiqua',27))
Next.place(x=540,y=415)
Pre=Label(root,bg='gray',justify=LEFT,font=('book antiqua',27))
Pre.place(x=30,y=415)
date_lbl=Label(root,font=('times',20))
date_lbl.place(x=260,y=154)        
time_lbl = Label(root,font=('times',42,'bold'))
time_lbl.place(x=20,y=131)
def nxtpre():
    times1=[assembly_time,period2,period3,period4,interval,period5,period6,period7,period8,sweep,end_prayer]
    shedule_list1=['Assembly','Period 2','Period 3','Period 4','Interval','Period 5','Period 6','Period 7','Period 8','Sweeping','End Prayer']
    if period1 != 'Manual':
        times1.append(period1)
        shedule_list1.append('Period 1')        
    for belltime in range(0,len(times1)):
        if (int(times1[belltime].replace(':','')+'00')>int(strftime('%H%M%S'))):            
            if(int(times1[belltime-1].replace(':','')+'00')<int(strftime('%H%M%S'))):
                Pre.config(text=times1[belltime-1]+':00 '+shedule_list1[belltime-1])
                Next.config(text=times1[belltime]+':00  '+shedule_list1[belltime])
                describes.config(text=shedule_list1[belltime-1])    
bell=lambda:verification('ring')
ttk.Button(root,text='Ring',image=bell_img,command=bell).place(x=875,y=400)
Button(root,fg='white',bg='indianred1',activeforeground = 'gray95',relief='groove',font = ('bold',10),activebackground = 'tomato',border = 0,text='     Ring!     ',command=bell).place(x=876,y=480)
def manual_bell(audio,item,text):
    manual_bell_button = Button(root,fg='gray',bg='white',activeforeground = 'gray95',relief='groove',font = ('bold',10),activebackground = 'tomato',border = 0,text='     Manual Bell     ',command=lambda:manual_bell(2,'p1','Period 1 '))
    manual_bell_button.place(x=820,y=340)        
    play(audios[audio])
    listbox_index(item,text)
    describes.config(text=text)
    manual_bell_button.destroy()
        
#audios
audios=['Sources/sounds/0.wav','Sources/sounds/1.wav','Sources/sounds/2.wav','Sources/sounds/3.wav','Sources/sounds/4.wav','Sources/sounds/5.wav','Sources/sounds/6.wav','Sources/sounds/7.wav','Sources/sounds/8.wav','Sources/sounds/9.wav','Sources/sounds/10.wav','Sources/sounds/11.wav','Sources/sounds/12.wav','Sources/sounds/13.wav']
def play(audio1):
    playback._play_with_simpleaudio(AudioSegment.from_wav(audio1))
activity_listbox=ttk.Treeview(root)
activity_listbox.place(x=767,y=0)
activity_listbox.heading('#0',text = 'AutoBell Activity')
activity_listbox.config(column = ('Time'))
activity_listbox.heading('Time',text = " Time ")
activity_listbox.column('#0',width = 150,anchor = 'center')
activity_listbox.column('Time',width = 80,anchor = 'center')
activity_listbox.insert('','0','StartUp',text = 'StartUp')
activity_listbox.set('StartUp','Time',time.strftime(' %I:%M:%S %p'))
def listbox_index(item,text):
    try:
        activity_listbox.insert('','0',item,text=text)
        activity_listbox.set(item,'Time',time.strftime(' %I:%M:%S %p'))
    except:
        activity_listbox.delete(item)
        activity_listbox.insert('','0',item,text=text)
        activity_listbox.set(item,'Time',time.strftime(' %I:%M:%S %p'))        
def function():
    now=datetime.datetime.now()
    date = now.strftime('%G-%B-%d(%A)')
    date_lbl.config(text=date)
    time = strftime('%H:%M:%S')
    time_lbl.config(text = time)   
    nxtpre()
    current_time =strftime("%H:%M:%S") 
    if assembly_time+':00' == current_time:
        play(audios[1])
        listbox_index('assm','Morning Assembly.')       
        if period1=='Manual':
            manual_bell_button.config(command=lambda:(manual_bell(13,'final',' God Bless You!')))
            manual_bell_button.place(x=820,y=340)        
        
    #1stPeriod
    elif period1+':00'==current_time:
        play(audios[2])    
        listbox_index('p1','Period-01.')                
    elif period2+':00' == current_time:
        play(audios[3])
        
        listbox_index('p2','Period-02.')         
    elif period3+':00' == current_time:
        play(audios[4])
        
        listbox_index('p3','Period-03.')
    elif period4+':00' == current_time:
        play(audios[5])
        listbox_index('p4','Period-04.')
    elif interval+':00' == current_time:
        listbox_index('interval','Interval bells.')
             
        play(audios[6])
    elif period5+':00' == current_time:
        play(audios[7])
        
        listbox_index('p5','Period-05.')
    elif period6+':00' == current_time:
        play(audios[8])
        
        listbox_index('p6','Period-06.')         
    elif period7+':00' == current_time:
        play(audios[9])
        
        listbox_index('p7','Period-07.')
        
    elif period8+':00' == current_time:
        play(audios[10])
        listbox_index('p8','Period-08.')    
    elif sweep+':00' == current_time:
        play(audios[11])
        listbox_index('clean',"Cleaning Bell.")  
    elif end_prayer+':00' == current_time:
        listbox_index('last',"Last Prayer.")
        play(audios[12])
        manual_bell_button.config(command=lambda:(manual_bell(13,'final',' God Bless You!')))
        manual_bell_button.place(x=820,y=340)    
    root.after(1000,function)
function()
root.mainloop()
