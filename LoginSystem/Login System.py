# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 13:39:52 2019

@author: nicol
"""

from tkinter import *
import tkinter as tk
import os

class Login_System:         
      def login(self):
          global f
          self.log=Toplevel(self.root)
          self.log.title('Login')
          self.log.configure(bg='grey')
          self.log.geometry('400x200+120+120')
          self.lb5=Label(self.log,fg='white',bg='grey',text='Username').place(x=160,y=70)
          self.lb6=Label(self.log,fg='white',bg='grey',text='Password').place(x=160,y=100)
          Button(self.log,fg='grey',bg='black',text='Login',command=lambda:self.login_r()).place(x=220,y=130)
          Button(self.log,fg='grey',bg='black',text='Exit',command=lambda: self.log.destroy()).place(x=270,y=130)
       #   Button(self.log,fg='grey',bg='black',text='reset',command=lambda: self.reseting()).place(x=320,y=130)
          self.UsernameEntry=StringVar()
          self.passwordEntry=StringVar()
          Label(self.log,text='Login',fg='grey',bg='black',font=('Courier 12 bold')).place(x=230,y=40)
          self.e5=Entry(self.log,textvariable=self.UsernameEntry).place(x=230,y=70)
          self.e6=Entry(self.log,textvariable=self.passwordEntry).place(x=230,y=100)
      def login_r(self):
          self.Username_n=self.UsernameEntry.get()
          self.password_n=self.passwordEntry.get()
          list_file=os.listdir()
          if self.Username_n+'.txt' in list_file:
              with open(self.Username_n+'.txt','r') as rr:
                  
                  
                  self.verify=rr.read()
                 
                  if self.password_n in self.verify:
                      Label(self.log,text='Login Successfully',fg='green',bg='grey').place(x=220,y=160)
                  else:
                    Label(self.log,text='Empty Password field',fg='red',bg='grey').place(x=220,y=160)  
          else:
             Label(self.log,text='Insuccessful',fg='red',bg='grey').place(x=220,y=160)
      def register(self):
          
          self.Username_i=self.Username.get()
          self.password_i=self.password.get()
          with open(self.Username_i+'.txt','w') as ww:
              ww.write(self.Username_i)
              ww.write(self.password_i)
              Label(self.s,text='Registration Successful Proceed to the Login',fg='green',bg='grey').place(x=160,y=170)
      def Signup(self):
          self.s=Toplevel()
          self.s.title('Sign Up')
          self.s.configure(bg='grey')
          self.s.geometry('400x200+120+120')
          self.e1=Entry(self.s).place(x=220,y=30)
          self.e2=Entry(self.s).place(x=220,y=60)
          self.Username=StringVar()
          self.e3=Entry(self.s,textvariable=self.Username).place(x=220,y=90)
          self.password=StringVar()
          self.e4=Entry(self.s,textvariable=self.password).place(x=220,y=120)
          Label(self.s,text='Sign Up',fg='grey',bg='black',font=('Courier 12 bold')).place(x=230,y=4)
        
          self.lb1=Label(self.s,fg='white',bg='grey',text='First name').place(x=160,y=30)
         #self.lb1.configure(font=('Courier 40 bold'))
          self.lb2=Label(self.s,fg='white',bg='grey',text='Last name').place(x=160,y=60)
        # self.lb2.configure(font=('Courier 40 bold'))
          self.lb3=Label(self.s,fg='white',bg='grey',text='Username').place(x=160,y=90)
         #self.lb3.configure(self.root,font=('Courier 40 bold'))
          self.lb4=Label(self.s,fg='white',bg='grey',text='Password').place(x=160,y=120)
       #  self.lb5=Label(self.master,fg='white',bg='grey',text='Username').place(x=160,y=70)
       #  self.lb6=Label(self.master,fg='white',bg='grey',text='Password').place(x=160,y=100)
        # self.lb4.configure(font=('Courier 40 bold'))
          Button(self.s,fg='grey',bg='black',text='Login',command=lambda : self.login()).place(x=160,y=150)
          Button(self.s,fg='grey',bg='black',text='Sign Up',command=lambda : self.register()).place(x=210,y=150)
         # Button(self.s,fg='grey',bg='black',text='reset',command=lambda:self.reset()).place(x=270,y=150)
          Button(self.s,fg='grey',bg='black',text='Exit',command=lambda : self.s.destroy()).place(x=270,y=150)
        #  Button(self.master,fg='grey',bg='black',text='Login').place(x=220,y=130)
      
      def __init__(self,root):
         self.root=root
         self.gridl=[[0 for x in range(3)] for y in range(3)]
         self.root.title('Waiting For User Response')
         
         
         self.root.geometry('400x200+120+120')
         
        # root.resizable('False','False')
        
         Label(root,text='if you do not have an account please sign up',font=('Courier 9 bold'),bg='grey').place(x=50,y=30)
         Button(self.root,fg='grey',bg='black',text='Login',command=lambda:self.login()).place(x=140,y=50)
         Button(self.root,fg='grey',bg='black',text='SignUp',command=lambda : self.Signup()).place(x=220,y=50)
        #  Button(self.master,fg='grey',bg='black',text='Login').place(x=220,y=130)
      
if __name__=='__main__':
    root=Tk()
    root.configure(bg='grey')
 
   
    ob=Login_System(root)
    print(ob.gridl)
    root.mainloop()
   
    
         