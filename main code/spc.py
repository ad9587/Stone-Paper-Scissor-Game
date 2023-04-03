from tkinter import *

from random import randint

w = Tk()
w.title("Stone Paper Scissor")
w.configure(background="black")

image_pstone= PhotoImage(name="stone1",file="i\st1.png")
image_pscissor= PhotoImage(name="scissor1",file="i\s1.png")
image_ppaper= PhotoImage(name="paper1",file="i\p1.png")
image_cstone= PhotoImage(name="stone2",file="i\st2.png")
image_cscissor= PhotoImage(name="scissor2",file="i\s2.png")
image_cpaper= PhotoImage(name="paper2",file="i\p2.png")

plabel=Label(w,image=image_pstone)

clabel=Label(w,image=image_cstone)

plabel.grid(row=1,column=0)
clabel.grid(row=1,column=4)


pindicate=Label(w,text="PLAYER",font=("papyrus",20,"bold"),fg="light blue",bg="black").grid(row=0,column=0)
cindicate=Label(w,text="COMPUTER  ",font=("papyrus",20,"bold"),fg="light blue",bg="black").grid(row=0,column=4)
vsindicate=Label(w,text="V/S",font=("algerian",50,"bold"),bg="black",fg="dark red").grid(row=1,column=2)




def wincondition(p,c):
	if(p==c):
		win.config(text="It's a Tie")
	elif p=="stone" :
		if c=="paper":
			win.config(text="Computer Wins!!!")
			 
		else:
			win.config(text="Player Wins!!!")
			
	elif p=="paper" :
		if c=="scissor":
			win.config(text="Computer Wins!!!")
			
		else:
			win.config(text="Player Wins!!!")
			
	elif p=="scissor" :
		if c=="stone":
			win.config(text="Computer Wins!!!")
			
		else:
			win.config(text="Player Wins!!!")
			
		
select=["stone","paper","scissor"]
		

def input(a):
	in_c=select[randint(0,2)]
	if in_c=="stone":
		clabel.configure(image=image_cstone)
	elif in_c=="scissor":
		clabel.configure(image=image_cscissor)
	else:
		clabel.configure(image=image_cpaper)
	
	if a=="stone":
		plabel.configure(image=image_pstone)
	elif a=="scissor":
		plabel.configure(image=image_pscissor)
	else:
		plabel.configure(image=image_ppaper)
	
	wincondition(a, in_c)

win = Label(w, text="", font=('Times New Roman', 30))
win.config(fg="gold",bg="dark blue", font=('Times New Roman', 30, 'bold'))
win.grid(row=5, column=2)

button_stone=Button(w,width=10,height=3,text="Stone",font=("algerian",18,"bold"),bg="silver",fg="red",relief="sunken",command=lambda:input("stone")).grid(row=4,column=1)
button_paper=Button(w,width=10,height=3,text="Paper",font=("algerian",18,"bold"),bg="silver",fg="red",relief="sunken",command=lambda:input("paper")).grid(row=4,column=2)
button_scissor=Button(w,width=10,height=3,text="Scissor",font=("algerian",18,"bold"),bg="silver",fg="red",relief="sunken",command=lambda:input("scissor")).grid(row=4,column=3)

w.mainloop()

