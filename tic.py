from tkinter import *
import tkinter.messagebox
#frame declaration
main=Tk()
main.title("TIC TAC TOE")
main.configure(bg="#00BE70")

f=Frame(main,bg="#00BE70")
f.pack()
main.geometry("600x600")
l=Label(f,text="Just Click With Mouse",fg='blue',bg="#00BE70")
l.grid(row=0,columnspan=4)
count=0

#Checking_Definition
ar=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
v=[0]*9
d={3:'X',-3:'O'}

#Validating_function
def check():
    for t in ar:
         tot=v[t[0]-1]+v[t[1]-1]+v[t[2]-1]
         #print(tot)
         if tot==3 or tot==-3:
                return 1,tot
                break         
    return 0,0


#Button Function
def rightcli(v1):
    flag=1
    a=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
    v1-=1
    global count
    count+=1
    if(count%2!=0):
        v[v1]=1
        a[v1].config(text="X",fg="red")
    else:
        v[v1]=-1 
        a[v1].config(text="O",fg="red")
    a[v1].config(state="disabled")
    if(count>3):
        bo,w=check()
        if(bo):
            tkinter.messagebox.showinfo("Winner!!",d[w]+" Wins")
            main.destroy()
            flag=0
    if(count==9) and (flag) :
        tkinter.messagebox.showinfo("Waste!!","Nobody won ra!!")
        main.destroy()
         
#Button Defintion
b1=Button(f,command=lambda:rightcli(1),width=20,height=10,bd=4)
b2=Button(f,command=lambda:rightcli(2),width=20,height=10,bd=4)
b3=Button(f,command=lambda:rightcli(3),width=20,height=10,bd=4)
b4=Button(f,command=lambda:rightcli(4),width=20,height=10,bd=4)
b5=Button(f,command=lambda:rightcli(5),width=20,height=10,bd=4)
b6=Button(f,command=lambda:rightcli(6),width=20,height=10,bd=4)
b7=Button(f,command=lambda:rightcli(7),width=20,height=10,bd=4)
b8=Button(f,command=lambda:rightcli(8),width=20,height=10,bd=4)
b9=Button(f,command=lambda:rightcli(9),width=20,height=10,bd=4)
b1.grid(row=2,column=1)
b2.grid(row=2,column=2)
b3.grid(row=2,column=3)
b4.grid(row=3,column=1)
b5.grid(row=3,column=2)
b6.grid(row=3,column=3)
b7.grid(row=4,column=1)
b8.grid(row=4,column=2)
b9.grid(row=4,column=3)
b=Button(f,text="Exit",bg="red",fg="White",command=lambda:main.destroy(),width=8)
b.grid(row=8,columnspan=7)
main.resizable(True,True)
main.mainloop()