from tkinter import *
from PIL import Image, ImageTk
from customer import cust_win
from room import roombooking
class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800")  # Adjusted geometry string
        
        # image 1
        img1 = Image.open("C:\\Users\\HP\\Desktop\\p1.png")
        img1 = img1.resize((1550, 140),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg1.place( x=0,y=0,width=1550, height=140)

        lbl_title=Label(self.root,text="Hotel Management System",font=("times new roman",40,"bold"),bg="black",fg="red",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)
        #main frame

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=630)

        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",bd=4,fg="red",relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)
        #button
        

        button_frame=Frame(main_frame,bd=4,relief=RIDGE)
        button_frame.place(x=0,y=35,width=228,height=190)

        cust_button=Button(button_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",bd=0,fg="red")
        cust_button.grid(row=0,column=0,pady=1)

        room_button=Button(button_frame,text="ROOM",command=self.roombooking,width=22,font=("times new roman",14,"bold"),bg="black",bd=0,fg="red")
        room_button.grid(row=1,column=0,pady=1)

        service_button=Button(button_frame,text="SERVICE",width=22,font=("times new roman",14,"bold"),bg="black",bd=0,fg="red")
        service_button.grid(row=2,column=0,pady=1)

        details_button=Button(button_frame,text="DETAILS",width=22,font=("times new roman",14,"bold"),bg="black",bd=0,fg="red")
        details_button.grid(row=3,column=0,pady=1)

        logout_button=Button(button_frame,text="LOGOUT",width=22,font=("times new roman",14,"bold"),bg="black",bd=0,fg="red")
        logout_button.grid(row=4,column=0,pady=1)

        #image 2-image shown in center
        img2 = Image.open("C:\\Users\\HP\\Desktop\\photo1.jpeg")
        img2 = img2.resize((1310, 590),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(main_frame, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg2.place( x=225,y=0,width=1310, height=590)

        #down images
        img3 = Image.open("C:\\Users\\HP\\Desktop\\food.png")
        img3 = img3.resize((230, 210),Image.LANCZOS)
        self.photoimg3= ImageTk.PhotoImage(img3)

        lblimg3 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg3.place( x=0,y=225,width=230, height=210)


        img4 = Image.open("C:\\Users\\HP\\Desktop\\p1.png")
        img4 = img4.resize((230, 190),Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg4 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg4.place( x=0,y=420,width=230, height=190)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_win(self.new_window)
    
    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=roombooking(self.new_window)
            
# Create the Tkinter root instance outside the class
root = Tk()

# Create an instance of HotelManagementSystem
obj = HotelManagementSystem(root)

# Start the Tkinter main loop
root.mainloop()


