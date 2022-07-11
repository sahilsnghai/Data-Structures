

class Array(object):
    def __init__(self, sizeofarray, arraytype=int):
        self.sizeofarray = len(list(map(arraytype, range(sizeofarray)))) #list()
        self.arrayVal = [arraytype(0)] * sizeofarray
        self.arraytype = arraytype

    def __str__(self):
        return ' '.join([str(i) for i in self.arrayVal])

    def __len__(self):
        return len(self.arrayVal)
    
    def __setitem__(self,index,data):#setter method
        self.arrayVal[index] = data
        
    def __getitem__(self, index):# getter method
        return self.arrayVal[index]

    def insert(self, keytoinsert, postion):# data =5 , position =1 
        if(self.sizeofarray > postion) :#[1,2,3,4,6]
            for i in range(self.sizeofarray-2 , postion-1, -1):
                self.arrayVal[i+1] = self.arrayVal[i]#[1,2,2,3,4]
            self.arrayVal[postion] = keytoinsert #[1,5,2,3,4]
        else:
            print(
                f"Value {keytoinsert} Cannot be inserted at Index {postion}.Index Out of range")

    def delete(self, postion):#[1,5,2,3,4]
        if(self.sizeofarray > postion):
            for i in range(postion, self.sizeofarray-1):#[1,5,2,3,4]
                self.arrayVal[i] = self.arrayVal[i+1]#[1,5,3,4,4]
            self.arrayVal[self.sizeofarray-1] = self.arraytype(0)#[1,5,3,4,0]
        else:
            print(
                f"Value Cannot be deleted at Index {postion}.")
   
    def search(self,key):
        for i in range(self.sizeofarray):#[1,5,3,4,0,6]
            if self.arrayVal[i]==key:
                return i
        return f"{key} not found"

if __name__ == '__main__':
    a = Array(6,str)
    # print(a)
    # print(len(a))
    a.insert(0,0)
    a.insert(2,1)
    a.insert(3,2)
    a.insert(4,3)
    a.insert(5,4)
    # print(a.search(3))
    # print(a)
    # a.delete(2)
    # a.delete(1)
    # print(a.__getitem__(4))
    # print(a)
    # b = list()
    # b.append("a")
    # b.append(3)
    # print(b)
    # l = list()