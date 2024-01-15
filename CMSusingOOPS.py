#BLL
import pickle
class Customer:
    cus_list=[]
    def __init__(self): #self=1000
        self.id=0
        self.name=0
        self.age=0
        self.mob=0
    def addCustomer(self):  #self=1000, self.id=10,self.name="Vikas"....
        Customer.cus_list.append(self)  #cuslist=[1000,2000... #print(Customer.cus_list[0].id)
    def searchCustomer(self):   #Self=10000, self.id=20, self.name=0,self.age=0...
        for e in Customer.cus_list:
            if(e.id==self.id):      #e=2000
                self.name=e.name    #self.name="Anil"
                self.age=e.age      #self.age=41
                self.mob=e.mob      #self.mob=234
    def deleteCustomer(self):   #self=11000, self.id=20, self.name=0...
        # for e in Customer.cus_list:
        #     if(e.id==self.id):
        #         Customer.cus_list.remove(e)
        #         break
        for i in range(len(Customer.cus_list)): #i=0,1,2
            if(Customer.cus_list[i].id==self.id):
                Customer.cus_list.pop(i)
                break
    def modifyCustomer(self):   #self=12000, self.id=20, self.name="Sonu"...
        for e in Customer.cus_list:
            if(e.id==self.id):
                e.name=self.name
                e.age=self.age
                e.mob=self.mob
                break
    @staticmethod
    def savetoPickle():
        f = open("D:/vikas/cmsdata.txt", "wb")
        pickle.dump(Customer.cus_list, f)
        f.close()
    @staticmethod
    def loadfromPickle():
        f=open("D:/vikas/cmsdata.txt", "rb")
        Customer.cus_list=pickle.load(f)
        f.close()
# #PL
# print("Welcome to CMS")
# def showCustomer(cus):
#     print("Cust ID:",cus.id,"Cust Name:",cus.name,"Cust Age:",cus.age,"Cust Mob:",cus.mob)
# while(1):
#     ch=input("""Enter Choice, 1: Add Cust, 2: Search Cust, 3: Delete, 4: Modify,
#     5: Display All, 6: Exit, 7: Save to Pickle, 8: Load from Pickle:""")
#     if(ch=="1"):    #Add Customer
#         cus=Customer()  #cus address 1000, cus.id=0,cus.name=0,cus.age=0,cus.mob=0
#         cus.id=input("Enter Cust Id:")  #10
#         cus.name=input("Enter Cust Name:")  #Vikas
#         cus.age=input("Enter Cust Age:")    #39
#         cus.mob=input("Enter Cust Mob:")    #123
#         cus.addCustomer()   #cus address 1000, self=cus
#         print("Customer added successfully")
#     elif(ch=="2"):  #Search Customer
#         cus=Customer()  #cus address 10000, cus.id=0, cus.name=0,cus.age=0..
#         cus.id=input("Enter Cust Id to Search:")    #cus.id=20
#         cus.searchCustomer()
#         showCustomer(cus)
#     elif(ch=="3"):  #Delete Customer
#         cus=Customer()  #cus address 11000, cus.id=0, cus.name=0,cus.age=0..
#         cus.id=input("Enter Cust Id to delete:")    #cus.id=20
#         cus.deleteCustomer()
#         print("Customer Deleted Successfully")
#     elif(ch=="4"):  #Modify Customer
#         cus=Customer()  #cus address 12000, cus.id=0, cus.name=0,cus.age=0..
#         cus.id=input("Enter Cust Id to Modify Cust:")    #cus.id=20
#         cus.name=input("Enter Cust updated Name:")  #cus.name="Sonu"
#         cus.age=input("Enter Cust updated Age:")
#         cus.mob=input("Enter Cust updated Mob No:")
#         cus.modifyCustomer()
#         print("Customer Modified Successfully")
#     elif(ch=="5"):  #Display all Customers
#         for e in Customer.cus_list:
#             showCustomer(e)
#     elif(ch=="6"):  #Exit
#         print("Thanks for using CMS")
#         break
#     elif(ch=="7"):  #Save data to Pickle Format in file
#         Customer.savetoPickle()
#         print("Data Saved Successfully")
#     elif (ch == "8"):  # Load data from Pickle Format file
#         Customer.loadfromPickle()
#         print("Data Retrieved Successfully")
#     else:
#         print("Incorrect Choice")


