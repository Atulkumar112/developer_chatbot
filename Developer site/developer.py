from tkinter import *
from PIL import ImageTk, Image   # for  open the jpg file

class Developer():
    def __init__(self,root):
        self.root=root


        self.root.title('Developer Details')
        
        w=root.winfo_screenwidth()
        h=root.winfo_screenheight()
        self.root.geometry("{}x{}+0+0".format(w,h))
        self.root.config(bg='black')
        self.root.title("Developers Details")
        self.root.iconbitmap("icon.png")

        self.title_name=Label(root,text='Developers Details',font=("algerian 35 bold"),bg='black',fg='#1ab3c4')
        self.title_name.place(x=0,y=130,width=w,height=45)
        # self.title_name.place(x=0,y=150,width=w,height=45)
        


        


# for  open the first image
        self.img=Image.open(r"img1.jpg")
        # self.img=self.img.resize((500,130),Image.ANTIALIAS)
        self.img=self.img.resize((500,150),Image.ANTIALIAS)
        self.photo=ImageTk.PhotoImage(self.img)
        self.img_l1=Label(root,image=self.photo)
        # self.img_l1.place(x=0,y=0,width=w/3,height=130)
        self.img_l1.place(x=0,y=0,width=w/3,height=130)




#for second image
        self.img=Image.open(r"img2.jpg")
        self.img=self.img.resize((502,130),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(self.img)
        self.img_l1=Label(root,image=self.photo2)
        self.img_l1.place(x=w/3,y=0,width=w/3,height=130)


#for third image
        self.img=Image.open(r"img3.jpg")
        self.img=self.img.resize((500,130),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(self.img)
        self.img_l1=Label(root,image=self.photo3)
        self.img_l1.place(x=2*w/3,y=0,width=w/3,height=130)


#for the frame of the developer details
        self.img=Image.open(r"img4.jpg")
        self.img=self.img.resize((1400,1100),Image.ANTIALIAS) 
        self.photo4=ImageTk.PhotoImage(self.img)   
        self.img_l1=Label(root, image=self.photo4)  
        self.img_l1.place(x=0,y=h/4.4,width=w,height=1100) 

#addinng the details of developers in the above frame
#first image of atul
        self.img=Image.open(r"img1rohit.png")
        self.img=self.img.resize((320,400),Image.ANTIALIAS) 
        self.photo5=ImageTk.PhotoImage(self.img)
        self.img_l1=Label(root, image=self.photo5, bg="#031129")
        self.img_l1.place(x=0,y=h/3, width=w/4,height=400)

#first image of atul
        self.img=Image.open(r"img2atul.png")
        self.img=self.img.resize((320,400),Image.ANTIALIAS) 
        self.photo6=ImageTk.PhotoImage(self.img)
        self.img_l1=Label(root, image=self.photo6, bg="#031129")
        self.img_l1.place(x=w/4,y=h/3,width=w/4,height=400)

#first image of atul  
        self.img=Image.open(r"img4manish.png")
        self.img=self.img.resize((320,400),Image.ANTIALIAS) 
        self.photo7=ImageTk.PhotoImage(self.img)
        self.img_l1=Label(root, image=self.photo7, bg="#031129")
        self.img_l1.place(x=2*w/4,y=h/3,width=w/4,height=400)

#first image of atul
        self.img=Image.open(r"img3deepak.png")
        self.img=self.img.resize((320,400),Image.ANTIALIAS) 
        self.photo8=ImageTk.PhotoImage(self.img)
        self.img_l1=Label(root, image=self.photo8, bg="#031129")
        self.img_l1.place(x=3*w/4,y=h/3,width=w/4,height=400)


        # self.img = Label(root, text="welcome",font=("algerian 35 bold"),fg='red' )
        # my_text.pack(pady=150)
        
        





root = Tk()

object = Developer(root)



root.mainloop()


