from tkinter import *
from PIL import Image, ImageTk
from tkinter import  messagebox,ttk
import mysql.connector
import random

class roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")  # Adjusted geometry string
        # variables
        self.var_Customer_Contact=StringVar()
        self.var_Check_In_Date=StringVar()
        self.var_Check_Out=StringVar()
        self.var_Available_Room=StringVar()
        self.var_Room_Type=StringVar()
        self.var_Meal=StringVar()
        self.var_Number_Of_Days=StringVar()
        self.var_Total_Cost=StringVar()
        


        
        lbl_title=Label(self.root,text="ROOM BOOKING",font=("times new roman",40,"bold"),bg="black",fg="red",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        img2 = Image.open("C:\\Users\\HP\\Desktop\\p4.png")
        img2 = img2.resize((100, 40),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg2.place( x=5,y=2,width=100, height=40)

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",font=("Arial Black",12,"bold"),padx=2)
        labelframeleft.place( x=5,y=50,width=425, height=490)
        #customer contact
        lbs_cust_contact=Label(labelframeleft,text="Customer_Contact",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbs_cust_contact.grid(row=0,column=0,sticky=W)
        
        entry_contact=Entry(labelframeleft,textvariable=self.var_Customer_Contact,width=20,font=("times new roman",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        btnFetchData=Button(labelframeleft,command=self.fetch_contact,text="Fetch Data",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnFetchData.place(x=347,y=4)


        #check in
        check_in_date=Label(labelframeleft,text="Check_In_Date:",font=("times new roman",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)

        txtcheck_in_date=Entry(labelframeleft,textvariable=self.var_Check_In_Date,width=29,font=("times new roman",13,"bold"))
        txtcheck_in_date.grid(row=1,column=1)

        #check out
        lbl_check_out=Label(labelframeleft,text="Check_Out:",padx=2,pady=6,font=("times new roman",12,"bold"))
        lbl_check_out.grid(row=2,column=0,sticky=W)

        txt_check_out=Entry(labelframeleft,textvariable=self.var_Check_Out,width=29,font=("times new roman",13,"bold"))
        txt_check_out.grid(row=2,column=1)
        # available room
        lblAvailable_room=Label(labelframeleft,text="Available_Room:",padx=2,pady=6,font=("times new roman",12,"bold"))
        lblAvailable_room.grid(row=3,column=0,sticky=W)

        txtAvailable_room=Entry(labelframeleft,textvariable=self.var_Available_Room,width=29,font=("times new roman",13,"bold"))
        txtAvailable_room.grid(row=3,column=1)
        # room type
        label_roomtype=Label(labelframeleft,text="Room_Type",padx=2,pady=6,font=("times new roman",12,"bold"))
        label_roomtype.grid(row=4,column=0,sticky=W)

        combo_roomtype=ttk.Combobox(labelframeleft,textvariable=self.var_Room_Type,width=27,state="readonly",font=("times new roman",12,"bold"))
        combo_roomtype["value"]=("single","Double","Luxury")
        combo_roomtype.current(0)
        combo_roomtype.grid(row=4,column=1)
        #meal
        lblmeal=Label(labelframeleft,text="Meal:",padx=2,pady=6,font=("times new roman",12,"bold"))
        lblmeal.grid(row=5,column=0,sticky=W)

        txtmeal=ttk.Entry(labelframeleft,textvariable=self.var_Meal,font=("times new roman",12,"bold"),width=29)
        txtmeal.grid(row=5,column=1)

        # number of days
        lblnoofdays=Label(labelframeleft,text="Number_Of_Days:",padx=2,pady=6,font=("times new roman",12,"bold"))
        lblnoofdays.grid(row=6,column=0,sticky=W)

        txtnoofdays=Entry(labelframeleft,textvariable=self.var_Number_Of_Days,width=29,font=("times new roman",13,"bold"))
        txtnoofdays.grid(row=6,column=1)
        #total cost
        lbltotal_cost=Label(labelframeleft,text="Total_Cost :",padx=2,pady=6,font=("times new roman",12,"bold"))
        lbltotal_cost.grid(row=8,column=0,sticky=W)

        txttotal_cost=Entry(labelframeleft,textvariable=self.var_Total_Cost,width=29,font=("times new roman",13,"bold"))
        txttotal_cost.grid(row=8,column=1)
        # bill button
        btnAdd=Button(labelframeleft,text="Bill",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=9,column=0,padx=1,sticky=W)


        button_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        button_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(button_frame,text="Add",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(button_frame,text="Update",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(button_frame,text="Delete",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(button_frame,text="Reset",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)
        #right side image
        img3 = Image.open("C:\\Users\\HP\\Desktop\\bed.png")
        img3 = img3.resize((520, 200),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(self.root, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg3.place( x=760,y=55,width=520, height=200)
        
        #table frame
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("Arial Black",12,"bold"),padx=2)
        Table_Frame.place( x=435,y=280,width=860, height=260)

        lbsSearchBY=Label(Table_Frame,text="Search By",font=("times new roman",12,"bold"),bg="red",fg="white")
        lbsSearchBY.grid(row=0,column=0,sticky=W,padx=2)
        
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,width=24,state="readonly",font=("times new roman",13,"bold"))
        combo_Search["value"]=("contact","room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txt_search=Entry(Table_Frame,textvariable=self.txt_search,width=24,font=("times new roman",13,"bold"))
        txt_search.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

        details_Table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_Table.place(x=0,y=50,width=860,height=180)

        scroll_x=Scrollbar(details_Table,orient=HORIZONTAL)
        scroll_y=Scrollbar(details_Table,orient=VERTICAL)

        self.room_Table=ttk.Treeview(details_Table,column=("Customer_Contact","Check_In_Date","Check_Out","Available_Room","Room_Type","Meal","Number_Of_Days","Total_Cost",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_Table.xview)
        scroll_y.config(command=self.room_Table.yview)

        self.room_Table.heading("Customer_Contact", text="Customer_Contact")
        self.room_Table.heading("Check_In_Date",text="Check_In_Date")
        self.room_Table.heading("Check_Out",text="Check_Out")
        self.room_Table.heading("Available_Room",text="Available_Room")
        self.room_Table.heading("Room_Type",text="Room_Type")
        self.room_Table.heading("Meal",text="Meal")
        self.room_Table.heading("Number_Of_Days",text="Number_Of_Days")
        self.room_Table.heading("Total_Cost",text="Number_Of_Days")

        self.room_Table["show"]="headings"

        self.room_Table.column("Customer_Contact",width=100)
        self.room_Table.column("Check_In_Date",width=100)
        self.room_Table.column("Check_Out",width=100)
        self.room_Table.column("Available_Room",width=100)
        self.room_Table.column("Room_Type",width=100)
        self.room_Table.column("Meal",width=100)
        self.room_Table.column("Number_Of_Days",width=100)
        self.room_Table.column("Total_Cost",width=100)
        


        self.room_Table.pack(fill=BOTH,expand=1)
    def fetch_contact(self):
        if self.var_Customer_Contact.get()=="":
            messagebox.showerror("Error","Please enter contact number")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="record")
            my_cursor=conn.cursor()
            query=("select CustomerName from customer where mobilenumber=%s")
            value=(self.var_Customer_Contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This number not found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=55,y=55,width=300,height=180)
                lblName=Label(showDataframe,text="Name",font=("times new roman",12,"bold"))
                lblName.place(x=0,y=0)


    def add_data(self):
            if self.var_mobilenumber.get()=="" or self.var_Customername.get()==""or self.var_fathername.get()=="" or self.var_gender.get()==""or self.var_city.get()==""or self.var_Customername.get()==""or self.var_state.get()==""or self.var_emailid.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
               try:
                 conn=mysql.connector.connect(host="localhost",user="root",password="root",database="record")
                 my_cursor=conn.cursor()
                 my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                             self.var_Customerid.get(), 
                                                                             self.var_Customername.get(),
                                                                             self.var_mothername.get(),
                                                                             self.var_fathername.get(),
                                                                             self.var_gender.get(),
                                                                             self.var_city.get(),
                                                                             self.var_mobilenumber.get(),
                                                                             self.var_state.get(),
                                                                             self.var_emailid.get()
                                                                         ))
                 conn.commit()
                 self.fetch_data()
                 conn.close()
                 messagebox.showinfo("Success","customer has been added",parent=self.root)
               except Exception as es:
                 messagebox.showwarning("warning",f"something went wrong:{str(es)}",parent=self.root)
        

                    








        
        














