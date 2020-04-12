import Tkinter
import random
import ttk
import tkMessageBox
from PIL import ImageTk,Image
from Tkinter import Toplevel
from Tkinter import Label
from Tkinter import Frame
from Tkinter import StringVar
from Tkinter import Entry
from Tkinter import IntVar
from Tkinter import Radiobutton
from cassandra.cluster import Cluster




window = Tkinter.Tk()


class Connect_Cassandra:
    def __init__(self):
        self.cluster = Cluster
        self.cluster = Cluster(['127.0.0.1'], port=9042)
        self.session = cluster.connect()

   
class Home_Page:
    def __init__(self, root):
        self.root=root
        self.root.title("My Bags")
        self.root.geometry("1000x750+0+0")
        self.root.config(bg="#dae4f7")
        self.frame = Frame(self.root, bg= "#dae4f7")
        self.frame.pack()
        self.img = ImageTk.PhotoImage(Image.open("icon.jpg"))
        self.display = Tkinter.Label(image=self.img)
        self.display.place(y = 130)
        self.title = Label(self.root, text= "WELCOME TO MY BAGS", font = ("Gabriola", 50, 'bold'), bg="#dae4f7", fg = "black")
        self.title.pack()
        self.title.place(x=200)
        
        self.buttonRegist = Tkinter.Button(window, text = "Registrasi", bg = "#94b3eb", width = 25, command = self.Registrasi1)
        self.buttonRegist.pack()
        self.buttonRegist.config(font=("Verdana", 12))
        self.buttonRegist.place(x = 650, y=210)

        self.buttonLoginAdmin = Tkinter.Button(window, text = "Login Admin", bg = "#94b3eb", width = 25, command = self.LoginAdmin)
        self.buttonLoginAdmin.pack()
        self.buttonLoginAdmin.config(font=("Verdana", 12))
        self.buttonLoginAdmin.place(x = 650, y = 330)

        self.buttonLogin = Tkinter.Button(window, text = "Login", bg = "#94b3eb", width = 25, command = self.Login)
        self.buttonLogin.pack()
        self.buttonLogin.config(font=("Verdana", 12))
        self.buttonLogin.place(x = 650, y = 450)

    def LoginAdmin (self):
        self.newWindow = Toplevel(self.root)
        self.objek = Login_Admin(self.newWindow)
    def Registrasi1 (self) :
        self.newWindow = Toplevel(self.root)
        self.objek = Registrasi(self.newWindow)
    def Login (self):
        self.newWindow = Toplevel(self.root)
        self.objek = Login(self.newWindow)
    
#====================================================================== LOGIN ADMIN =================================================================================
class Login_Admin : 
    def __init__ (self, root) :
        self.root=root
        self.root.title("Bukti Pembelian")
        self.root.geometry("1000x750+0+0")
        self.root.config(bg="#dae4f7")
        self.frame = Frame(self.root, bg= "#dae4f7")
        self.frame.pack()

        self.title=Label(self.root, text= "LOGIN ADMIN MY BAGS", font = ("Gabriola", 75, 'bold'), bg="#dae4f7", fg = "black")
        self.title.pack()
        self.title.place(x=85, y=40)
        #======================================================Username =================================================================================
        self.titleUsername=Label(self.root, text= "Username :", font = ("Verdana", 25), bg="#dae4f7", fg = "black")
        self.titleUsername.pack()
        self.titleUsername.place(x = 250, y=270)
        self.Username = StringVar()
        self.Username_ent=Entry(self.root, textvariable=self.Username, width=50)
        self.Username_ent.pack()
        self.Username_ent.place(x=500, y=280)
        #======================================================Password =================================================================================
        self.titlePassword=Label(self.root, text= "Password  :", font = ("Verdana", 25), bg="#dae4f7", fg = "black")
        self.titlePassword.pack()
        self.titlePassword.place(x = 250, y=370)
        self.Password = StringVar()
        self.Password_ent=Entry(self.root, show="*", textvariable=self.Password, width=50)
        self.Password_ent.pack()
        self.Password_ent.place(x=500, y=380)

        self.buttonMasukAdmin = Tkinter.Button(self.root, text = "Masuk", bg = "#94b3eb", width = 35, command = self.MasukAdmin)
        self.buttonMasukAdmin.pack()
        self.buttonMasukAdmin.config(font=("Verdana", 12))
        self.buttonMasukAdmin.place(x= 350, y=470)        

    def MasukAdmin (self):
        self.newWindow = Toplevel(self.root)
        self.objek = Admin(self.newWindow)
        if self.Username.get()==""or self.Password.get()=="":
            tkMessageBox.showerror("Error", "Username dan Password Kosong")
        else:
            self.Username.get()=="Admin My Bags" or self.Password.get()=="1234567"
            command = self.MasukAdmin
#====================================================================== REGISTRASI =================================================================================        
class Registrasi : #REGISTRASI 
    def __init__ (self, root) :
        self.root=root
        self.root.title("Registrasi")
        self.root.geometry("1000x750+0+0")
        self.root.config(bg="#dae4f7")
        self.frame = Frame(self.root, bg= "#dae4f7")
        self.frame.pack()
        self.title=Label(self.root, text= "REGISTRASI PENGGUNA", font = ("Gabriola", 40, 'bold'), bg="#dae4f7", fg = "black")
        self.title.pack()
        self.title.place(x=280)
        #======================================================Nama Lengkap =============================================================================

        self.titleNangkap = Label(self.root, text= "Nama Lengkap   :", font = ("Verdana", 20), bg="#dae4f7", fg = "black")
        self.titleNangkap.pack()
        self.titleNangkap.place(x = 130, y=100)
        self.Nangkap = StringVar()
        self.Nangkap_ent = Entry(self.root, textvariable=self.Nangkap, width=50)
        self.Nangkap_ent.pack()
        self.Nangkap_ent.place(x=420, y=112)
        #======================================================Username =================================================================================
        self.titleUname = Label(self.root, text= "Username         :", font = ("Verdana", 20), bg="#dae4f7", fg = "black")
        self.titleUname.pack()
        self.titleUname.place(x = 130, y=160)
        self.Username1 = StringVar()
        self.Username_ent = Entry(self.root, textvariable=self.Username1, width=50)
        self.Username_ent.place(x=420, y=172)
        #======================================================Password =================================================================================        
        self.titlePass = Label(self.root, text= "Password          :", font = ("Verdana", 20), bg="#dae4f7", fg = "black")
        self.titlePass.pack()
        self.titlePass.place(x = 130, y=210)
        self.Password1 = StringVar()
        self.Password_ent = Entry(self.root, show="*", textvariable=self.Password1, width=50)
        self.Password_ent.pack()
        self.Password_ent.place(x=420, y=222)
        #======================================================Alamat Email ==============================================================================
        self.titleEmail = Label(self.root, text= "Alamat Email     :", font = ("Verdana", 20), bg="#dae4f7", fg = "black")
        self.titleEmail.pack()
        self.titleEmail.place(x = 130, y=260)
        self.Email = StringVar()
        self.Email_ent = Entry(self.root, textvariable=self.Email, width=50)
        self.Email_ent.pack()
        self.Email_ent.place(x=420, y=272)
        #======================================================Jenis Kelamin ==============================================================================        
        self.titleJK = Label(self.root, text= "Jenis Kelamin    :", font = ("Verdana", 20), bg="#dae4f7", fg = "black")
        self.titleJK.pack()
        self.titleJK.place(x = 130, y=320)
        self.JK_ent = ttk.Combobox(self.root,  values=["Laki-Laki", "Perempuan"], width=25) 
        self.JK_ent.pack()
        self.JK_ent.place(x=420, y=332)
        #======================================================Tempat Lahir ==============================================================================
        self.titleTemptL=Label(self.root, text= "Tempat Lahir     :", font = ("Verdana", 20), bg="#dae4f7", fg = "black")
        self.titleTemptL.pack()
        self.titleTemptL.place(x = 130, y=380)
        self.TemptL = StringVar()
        self.TemptL_ent=Entry(self.root, textvariable=self.TemptL, width=50)
        self.TemptL_ent.pack()
        self.TemptL_ent.place(x=420, y=392)
        #======================================================Tanggal Lahir ==============================================================================
        self.titleTglL=Label(self.root, text= "Tanggal Lahir    :", font = ("Verdana", 20), bg="#dae4f7", fg = "black")
        self.titleTglL.pack()
        self.titleTglL.place(x = 130, y=440)
        self.TglL = list(range(1,32))
        self.TglL_ent=ttk.Combobox(self.root, values=self.TglL, width=15)
        self.TglL_ent.pack()
        self.TglL_ent.place(x=420, y=452)
        #======================================================Alamat Rumah ==============================================================================
        self.titleAR=Label(self.root, text= "Alamat Rumah   :", font = ("Verdana", 20), bg="#dae4f7", fg = "black")
        self.titleAR.pack()
        self.titleAR.place(x = 130, y=500)
        self.AR = StringVar()
        self.AR_ent = Entry(self.root, textvariable=self.AR, width=50)
        self.AR_ent.pack()
        self.AR_ent.place(x=420, y=512)
        
        
        self.buttonSelesai = Tkinter.Button(self.root, text = "Selesai", bg = "#94b3eb", width = 35, command = self.Login1)
        self.buttonSelesai.pack()
        self.buttonSelesai.config(font=("Verdana", 12))
        self.buttonSelesai.place(x= 350, y=600)
       
    def Login1 (self):
        self.newWindow = Toplevel(self.root)
        self.objek = Login(self.newWindow)
        text  = "Registrasi Pengguna :"
        print(text)
        Nama= "Nama Lengkap:", self.Nangkap.get()
        print(Nama)
        Username="Username:", self.Username1.get()
        print(Username)
        Pass="Password:", self.Password1.get() 
        print(Pass)
        email="Alamat Email:", self.Email.get()
        print(email)
        JK="Jenis Kelamin:", self.JK_ent.get()
        print(JK)
        TL="Tempat Lahir:", self.TemptL.get()
        print(TL)
        Tgll="Tanggal Lahir:", self.TglL_ent.get()
        print(Tgll)
        Alamat="Alamat Rumah:", self.AR.get()
        print(Alamat)
        print("---------------------------------------------")
      
        if self.Nangkap_ent.get()=="" or self.Username_ent.get()==""and self.Password_ent.get()=="":
            tkMessageBox.showerror("Error", "All fields are required!!")
        else:
            command = self.Login1
#====================================================================== Login =================================================================================        
class Login : 
    def __init__ (self, root) :
        self.root=root
        self.root.title("Login")
        self.root.geometry("1000x750+0+0")
        self.root.config(bg="#dae4f7")
        self.frame = Frame(self.root, bg= "#dae4f7")
        self.frame.pack()

           
        self.title=Label(self.root, text= "LOGIN MY BAGS", font = ("Gabriola", 95, 'bold'), bg="#dae4f7", fg = "black")
        self.title.pack()
        self.title.place(x=150)
        #======================================================Username =================================================================================
        self.titleUsername=Label(self.root, text= "Username :", font = ("Verdana", 25), bg="#dae4f7", fg = "black")
        self.titleUsername.pack()
        self.titleUsername.place(x = 250, y=270)
        self.Username = StringVar()
        self.Username_ent=Entry(self.root, textvariable=self.Username, width=50)
        self.Username_ent.pack()
        self.Username_ent.place(x=500, y=280)
        #======================================================Password =================================================================================
        self.titlePassword=Label(self.root, text= "Password  :", font = ("Verdana", 25), bg="#dae4f7", fg = "black")
        self.titlePassword.pack()
        self.titlePassword.place(x = 250, y=370)
        self.Password = StringVar()
        self.Password_ent=Entry(self.root, show="*", textvariable=self.Password, width=50)
        self.Password_ent.pack()
        self.Password_ent.place(x=500, y=380)
        
        
        self.buttonMasuk = Tkinter.Button(self.root, text = "Masuk", bg = "#94b3eb", width = 35, command = self.Masuk1)
        self.buttonMasuk.pack()
        self.buttonMasuk.config(font=("Verdana", 12))
        self.buttonMasuk.place(x= 350, y=470)        

    def Masuk1 (self):
        self.newWindow = Toplevel(self.root)
        self.objek = Produk_Tas(self.newWindow)
        print("Login Pengguna :" , self.Username_ent.get(), self.Password_ent.get())
        print("---------------------------------------------")
        if self.Username.get()==""or self.Password.get()=="":
            tkMessageBox.showerror("Error", "All fields are required!!")
        else:
            command = self.Masuk1

#==================================================================== PRODUK TAS =================================================================================        
class Produk_Tas : 
    def __init__ (self, root) :
        self.root=root
        self.root.title("Gambar Produk Tas")
        self.root.geometry("1000x750+0+0")
        self.root.config(bg="#ebedf0")
        self.frame = Frame(self.root, bg= "#ebedf0")
        self.frame.pack()
        self.title=Label(self.root, text= "GAMBAR PRODUK TAS", font = ("Gabriola", 30, 'bold'), bg="#ebedf0", fg = "black")
        self.title.pack()
        self.title.place(x=300)
        
        self.img1 = ImageTk.PhotoImage(Image.open("ProdukBags.png"))
        self.display = Tkinter.Label(self.root, image=self.img1)
        self.display.place(y = 55)
        self.title=Label(self.root, text= "Tas 001  ", font = ("Constantia", 15), bg="#ebedf0", fg = "black")
        self.title.pack()
        self.title.place(x=10, y=255)
        self.title=Label(self.root, text= "SlingBag Rantai", font = ("Constantia", 15), bg="#ebedf0", fg = "black")
        self.title.pack()
        self.title.place(x=10, y=285)
        self.title=Label(self.root, text= "Rp 150.000 ", font = ("Constantia", 15), bg="#ebedf0", fg = "black")
        self.title.pack()
        self.title.place(x=10, y=315)
           
        self.title=Label(self.root, text= "Tas 002", font = ("Constantia", 15), bg="#ebedf0", fg = "black")
        self.title.pack()
        self.title.place(x=255, y=255)
        self.title=Label(self.root, text= "Tote Bag", font = ("Constantia", 15), bg="#ebedf0", fg = "black")
        self.title.pack()
        self.title.place(x=255, y=285)
        self.title=Label(self.root, text= "Rp 60.000 ", font = ("Constantia", 15), bg="#ebedf0", fg = "black")
        self.title.pack()
        self.title.place(x=255, y=315)

        self.title=Label(self.root, text= "Tas 003", font = ("Constantia", 15), bg="#ebedf0", fg = "black")
        self.title.pack()
        self.title.place(x=505, y=255)
        self.title=Label(self.root, text= "Bag Bluecream", font = ("Constantia", 15), bg="#ebedf0", fg = "black")
        self.title.pack()
        self.title.place(x=505, y=285)
        self.title=Label(self.root, text= "Rp 200.000 ", font = ("Constantia", 15), bg="#ebedf0", fg = "black")
        self.title.pack()
        self.title.place(x=505, y=315)

        self.title=Label(self.root, text= "Tas 004", font = ("Constantia", 15), bg="#ebedf0", fg = "black")
        self.title.pack()
        self.title.place(x=753, y=255)
        self.title=Label(self.root, text= "Bag Men", font = ("Constantia", 15), bg="#ebedf0", fg = "black")
        self.title.pack()
        self.title.place(x=753, y=285)
        self.title=Label(self.root, text= "Rp 100.000 ", font = ("Constantia", 15), bg="#ebedf0", fg = "black")
        self.title.pack()
        self.title.place(x=753, y=315)

        self.title=Label(self.root, text= "Tas 005", font = ("Constantia", 14), bg="#ebedf0", fg = "black")
        self.title.pack()
        self.title.place(x=10, y=580)
        self.title=Label(self.root, text= "Bag Woman", font = ("Constantia", 15), bg="#ebedf0", fg = "black")
        self.title.pack()
        self.title.place(x=10, y=608)
        self.title=Label(self.root, text= "Rp 160.000 ", font = ("Constantia", 15), bg="#ebedf0", fg = "black")
        self.title.pack()
        self.title.place(x=10, y=635)

        self.title=Label(self.root, text= "Tas 006", font = ("Constantia", 14), bg="#ebedf0", fg = "black")
        self.title.pack()
        self.title.place(x=255, y=580)
        self.title=Label(self.root, text= "Sling Bag", font = ("Constantia", 15), bg="#ebedf0", fg = "black")
        self.title.pack()
        self.title.place(x=255, y=608)
        self.title=Label(self.root, text= "Rp 100.000 ", font = ("Constantia", 15), bg="#ebedf0", fg = "black")
        self.title.pack()
        self.title.place(x=255, y=635)

        self.title=Label(self.root, text= "Tas 007", font = ("Constantia", 14), bg="#ebedf0", fg = "black")
        self.title.pack()
        self.title.place(x=505, y=580)
        self.title=Label(self.root, text= "Backpack", font = ("Constantia", 15), bg="#ebedf0", fg = "black")
        self.title.pack()
        self.title.place(x=505, y=608)
        self.title=Label(self.root, text= "Rp 110.000 ", font = ("Constantia", 15), bg="#ebedf0", fg = "black")
        self.title.pack()
        self.title.place(x=505, y=635)

        self.title=Label(self.root, text= "Tas 008", font = ("Constantia", 14), bg="#ebedf0", fg = "black")
        self.title.pack()
        self.title.place(x=753, y=580)
        self.title=Label(self.root, text= "Travel Bag", font = ("Constantia", 15), bg="#ebedf0", fg = "black")
        self.title.pack()
        self.title.place(x=753, y=608)
        self.title=Label(self.root, text= "Rp 180.000 ", font = ("Constantia", 15), bg="#ebedf0", fg = "black")
        self.title.pack()
        self.title.place(x=753, y=635)

        self.buttonKeluar = Tkinter.Button(self.root, text = "Keluar", bg = "#94b3eb", width = 35, command = self.Keluar)
        self.buttonKeluar.pack()
        self.buttonKeluar.config(font=("Verdana", 12))
        self.buttonKeluar.place(x= 110, y=665)
        self.buttonLanjutPembelian = Tkinter.Button(self.root, text = "Lanjut", bg = "#94b3eb", width = 35, command = self.Pembelian)
        self.buttonLanjutPembelian.pack()
        self.buttonLanjutPembelian.config(font=("Verdana", 12))
        self.buttonLanjutPembelian.place(x= 550, y=665)

        
    def Pembelian (self):
        self.newWindow = Toplevel(self.root)
        self.objek = Pembelian(self.newWindow)
    def Keluar (self):
        self.newWindow = Toplevel(self.root)
        self.objek = Login(self.newWindow)

#========================================================================= Pembelian =============================================================================      
class Pembelian : 
    def __init__ (self, root) :
        self.root=root
        self.root.title("Rincian Pembelian")
        self.root.geometry("1000x750+0+0")
        self.root.config(bg="#dae4f7")
        self.frame = Frame(self.root, bg= "#dae4f7")
        self.frame.pack()
        self.title=Label(self.root, text= "RINCIAN PEMBELIAN", font = ("Gabriola", 50, 'bold'), bg="#dae4f7", fg = "black")
        self.title.pack()
        self.title.place(x=230)


        self.titleAddProduk=Label(self.root, text= "Beli Produk  ", font = ("Gabriola", 35), bg="#dae4f7", fg = "black")
        self.titleAddProduk.pack()
        self.titleAddProduk.place(x=550, y=95)   

        self.titleKodeBarang=Label(self.root, text= "Kode Barang  ", font = ("Gabriola", 20), bg="#dae4f7", fg = "black")
        self.titleKodeBarang.pack()
        self.titleKodeBarang.place(x=550, y=185)

        self.img = ImageTk.PhotoImage(Image.open("mybags.png"))
        self.display = Tkinter.Label(self.root, image=self.img)
        self.display.place(y = 130)
      
        self.buttonAdd = Tkinter.Button(self.root, text = "Tas 001", bg = "#accbfc",width = 25, command = self.Add1)
        self.buttonAdd.pack()
        self.buttonAdd.config(font=("Verdana", 12))
        self.buttonAdd.place(x=680, y=195)
        
        self.buttonAdd = Tkinter.Button(self.root, text = "Tas 002", bg = "#99CCFF",width = 25, command = self.Add2)
        self.buttonAdd.pack()
        self.buttonAdd.config(font=("Verdana", 12))
        self.buttonAdd.place(x=600 , y=245)

        self.buttonAdd = Tkinter.Button(self.root, text = "Tas 003", bg = "#accbfc",width = 25, command = self.Add3)
        self.buttonAdd.pack()
        self.buttonAdd.config(font=("Verdana", 12))
        self.buttonAdd.place(x= 680, y=295)

        self.buttonAdd = Tkinter.Button(self.root, text = "Tas 004", bg = "#99CCFF",width = 25, command = self.Add4)
        self.buttonAdd.pack()
        self.buttonAdd.config(font=("Verdana", 12))
        self.buttonAdd.place(x= 600, y=345)

        self.buttonAdd = Tkinter.Button(self.root, text = "Tas 005", bg = "#accbfc",width = 25, command = self.Add5)
        self.buttonAdd.pack()
        self.buttonAdd.config(font=("Verdana", 12))
        self.buttonAdd.place(x= 680, y=395)

        self.buttonAdd = Tkinter.Button(self.root, text = "Tas 006", bg = "#99CCFF",width = 25, command = self.Add6)
        self.buttonAdd.pack()
        self.buttonAdd.config(font=("Verdana", 12))
        self.buttonAdd.place(x= 600, y=445)

        self.buttonAdd = Tkinter.Button(self.root, text = "Tas 007", bg = "#accbfc",width = 25, command = self.Add7)
        self.buttonAdd.pack()
        self.buttonAdd.config(font=("Verdana", 12))
        self.buttonAdd.place(x= 680, y=495)

        self.buttonAdd = Tkinter.Button(self.root, text = "Tas 008", bg = "#99CCFF",width = 25, command = self.Add8)
        self.buttonAdd.pack()
        self.buttonAdd.config(font=("Verdana", 12))
        self.buttonAdd.place(x= 600, y=545)


        self.buttonKembali = Tkinter.Button(self.root, text = "Kembali", bg = "#94b3eb", width = 35, command = self.Kembali)
        self.buttonKembali.pack()
        self.buttonKembali.config(font=("Verdana", 12))
        self.buttonKembali.place(x= 110, y=650)
        self.buttonSelesai = Tkinter.Button(self.root, text = "Selesai", bg = "#94b3eb", width = 35, command = self.Login1)
        self.buttonSelesai.pack()
        self.buttonSelesai.config(font=("Verdana", 12))
        self.buttonSelesai.place(x= 550, y=650)

        
    def Add1 (self):
        self.newWindow = Toplevel(self.root)
        self.objek = Pembelian(self.newWindow)
        print("PRODUK MY BAGS")
        T1 = ["Membeli", "Tas 001", "SlingBag Rantai", "Rp 150.000"]
        print("Produk 01")
        for title in T1:
            print(title)
        print("")
        print("---------------------------------------------")
    def Add2 (self):
        self.newWindow = Toplevel(self.root)
        self.objek = Pembelian(self.newWindow)
        T2 = ["Membeli","Tas 002", "Tote Bag", "Rp 60.000"]
        print("Produk 02")
        for title in T2:
            print(title)
        print("")
        print("---------------------------------------------")
    def Add3 (self):
        self.newWindow = Toplevel(self.root)
        self.objek = Pembelian(self.newWindow)
        T3 = ["Membeli","Tas 003", "Bag Bluecream", "Rp 200.000"]
        print("Produk 03")
        for title in T3:
            print(title)
        print("")
        print("---------------------------------------------")
    def Add4 (self):
        self.newWindow = Toplevel(self.root)
        self.objek = Pembelian(self.newWindow)
        T4 = ["Membeli","Tas 004", "Bag Men", "Rp 100.000"]
        print("Produk 04")
        for title in T4:
            print(title)
        print("")
        print("---------------------------------------------")
    def Add5 (self):
        self.newWindow = Toplevel(self.root)
        self.objek = Pembelian(self.newWindow)
        T5 = ["Membeli","Tas 005", "Bag Woman", "Rp 160.000"]
        print("Produk 05")
        for title in T5:
            print(title)
        print("")
        print("---------------------------------------------")
    def Add6 (self):
        self.newWindow = Toplevel(self.root)
        self.objek = Pembelian(self.newWindow)
        T6 = ["Membeli","Tas 006", "Sling Bag", "Rp 100.000"]
        print("Produk 06")
        for title in T6:
            print(title)
        print("")
        print("---------------------------------------------")
    def Add7 (self):
        self.newWindow = Toplevel(self.root)
        self.objek = Pembelian(self.newWindow)
        T7 = ["Membeli","Tas 007", "Backpack", "Rp 110.000"]
        print("Produk 07")
        for title in T7:
            print(title)
        print("")
        print("---------------------------------------------")
    def Add8 (self):
        self.newWindow = Toplevel(self.root)
        self.objek = Pembelian(self.newWindow)
        T8 = ["Membeli","Tas 008", "Travel Bag ", "Rp 180.000"]
        print("Produk 08")
        for title in T8:
            print(title)
        print("")
        print("---------------------------------------------")
  
    def Kembali (self):
        self.newWindow = Toplevel(self.root)
        self.objek = Produk_Tas(self.newWindow)
    def Login1 (self):
        self.newWindow = Toplevel(self.root)
        self.objek = Login(self.newWindow)
#============================================================================= Admin ============================================================================= 
class Admin :
    def __init__ (self, root) :
        self.root=root
        self.root.title("Selamat Datang Admin My Bags")
        self.root.geometry("1000x750+0+0")
        self.root.config(bg="#dae4f7")
        self.frame = Frame(self.root, bg= "#dae4f7")
        self.frame.pack()
        self.title=Label(self.root, text= "SELAMAT DATANG ADMIN MY BAGS", font = ("Gabriola", 45, 'bold'), bg="#dae4f7", fg = "black")
        self.title.pack()
        self.title.place(x=130)
        self.img = ImageTk.PhotoImage(Image.open("admin.png"))
        self.display = Tkinter.Label(self.root, image=self.img)
        self.display.place(x= 320, y = 130)

        
        self.buttonlist = Tkinter.Button(self.root, text = "List Produk My Bags", bg = "#94b3eb", width = 35, command = self.listProduk)
        self.buttonlist.pack()
        self.buttonlist.config(font=("Verdana", 12))
        self.buttonlist.place(x= 320, y=510)

    def listProduk(self):
        self.newWindow = Toplevel(self.root)
        self.objek = Admin(self.newWindow)
        print("PRODUK MY BAGS")
        T1 = ["Tas 001", "SlingBag Rantai", "Rp 150.000"]
        print("Produk 01")
        for title in T1:
            print(title)
        print("")
        T2 = ["Tas 002", "Tote Bag", "Rp 60.000"]
        print("Produk 02")
        for title in T2:
            print(title)
        print("")
        T3 = ["Tas 003", "Bag Bluecream", "Rp 200.000"]
        print("Produk 03")
        for title in T3:
            print(title)
        print("")
        T4 = ["Tas 004", "Bag Men", "Rp 100.000"]
        print("Produk 04")
        for title in T4:
            print(title)
        print("")
        T5 = ["Tas 005", "Bag Woman", "Rp 160.000"]
        print("Produk 05")
        for title in T5:
            print(title)
        print("")
        T6 = ["Tas 006", "Sling Bag", "Rp 100.000"]
        print("Produk 06")
        for title in T6:
            print(title)
        print("")
        T7 = ["Tas 007", "Backpack", "Rp 110.000"]
        print("Produk 07")
        for title in T7:
            print(title)
        print("")
        T8 = ["Tas 008", "Travel Bag ", "Rp 180.000"]
        print("Produk 08")
        for title in T8:
            print(title)
        print("")
        print("---------------------------------------------")

        

        
objek = Home_Page(window)
window.mainloop()


    








