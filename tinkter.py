# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 12:05:12 2019

@author: Amiy
"""

import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title('Calculator')

label=tk.Label(root,text="Enter first number",pady=(10))
label.pack()
fn_entry=tk.Entry(root)
fn_entry.pack()


label1=tk.Label(root,text="Enter second number",pady=(10))
label1.pack()
sn_entry=tk.Entry(root)
sn_entry.pack()

operations=tk.Label(root,text="operations",pady=(10))
operations.pack()

def addition():
    first,second=takeValueInput()
    result=first+second
    
    rs_label.config(text="Result  after operation is:"+str(result))
    
def substraction():
    first,second=takeValueInput()
    result=first-second
    
    rs_label.config(text="Result  after operation is:"+str(result))
def multiply():
    first,second=takeValueInput()
    result=first*second
    #print(first+second)
    rs_label.config(text="Result  after operation is:"+str(result))

def divide():
    first,second=takeValueInput()
    if second==0:
        messagebox.showerror("error","cannot divide the value by zero")
    else:
    
        result=first/second

        result=round(result,2)
        rs_label.config(text="Result  after operation is:"+str(result))
        
def takeValueInput():
    first=fn_entry.get()
    second=sn_entry.get()
    try:
        first=int(first)
        second=int(second)
        return first,second
    except ValueError:
        if((len(fn_entry.get())==0)or(len(sn_entry.get())==0)):
            messagebox.showerror("Error","please enter a value")
        else:
             messagebox.showerror("Error","please enter only integer value")
             quit(0)
add_button=tk.Button(root,text="+",command=lambda:addition())
add_button.pack()

sub_button=tk.Button(root,text="-",command=lambda:substraction())
sub_button.pack()

mul_button=tk.Button(root,text="*",command=lambda:multiply())
mul_button.pack()

div_button=tk.Button(root,text="/",command=lambda:divide())
div_button.pack()

rs_label=tk.Label(root,text="operations result is:")
rs_label.pack()
root.mainloop()

