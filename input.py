from CRD_Class import *
#importing the contents of class 

ele=CRD()
#initialize class

ele.create("ShubhamAggarwal",980000)
ele.create("VarunSehgal",1700360)
ele.create("ArpitManhotra",231700360)
ele.create("Kapilveerval",23700360)


ele.read("ArpitManhotra")
#it returns the value of the key

ele.create("VarunSehgal",50)
#it returns the key_name already eeleists in the database

ele.update("Kapilveerval",55)
#it replaces the initial value of the respective key with new value 

 
ele.delete("ArpitManhotra")
#it deletes the respective key and its value from the database(memory is also freed)