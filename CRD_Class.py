#initialize a dictionary 
dic={}

##constraints for file size less than 1GB and Jasonobject value less than 16KB  

max_len=1024*1020*1024
max_val=16*1024*1024

class CRD:
    def create(self,key,value):
        if key in dic:
            print("key is already Present")
        else:
            #javascript can only accept string as keys and here we are provided with the 
            #condition of only alphabet 
            if(key.isalpha()):
                if len(dic)<(max_len) and value<=(max_val): 
                    if len(key)<=32: #constraints for input key_name capped at 32chars
                        dic[key]=value
                        print(dic)
                else:
                    print("Memory limit exceeded")
            else:
                print("Make sure that key_name must contain only alphabets and no special characters or numbers")

    def read(self,key):
        if key not in dic:
            print("key does not exist in database. Please enter a valid key")
        else:
            b=dic[key]
            res=str(key)+":"+str(b)
            print(res)

    def delete(self,key):
        if key not in dic:
            print("key does not exist in database. Please enter a valid key")
        else:
            del dic[key]
            print("key is successfully deleted")

    def update(self,key,value):
        if key not in dic:
            print("key does not exist in database. Please enter a valid key")
        else:
            dic[key]=value
            print("The value for the key has been updated")

# if __name__=="__main__":
#     crd=CRD()
#     print(crd.create("amit",26))
#     print(crd.read("amit"))
#     crd.delete("keshav")
#     crd.update("amit",36)