# heap Implementation 
class MinHeap:
    def __init__(self,arr=[]):
        self.arr=arr
    def insert(self,val):
        self.arr.append(val)
        pointer=len(self.arr)-1
        parent_pointer=(pointer-1)//2
        while(parent_pointer >=0 and self.arr[parent_pointer]>self.arr[pointer]):
            self.arr[parent_pointer],self.arr[pointer]=self.arr[pointer],self.arr[parent_pointer]
            pointer=parent_pointer
            parent_pointer=(pointer-1)//2

    def remove_min(self):
        self.arr[0],self.arr[len(self.arr)-1]=self.arr[len(self.arr)-1],self.arr[0]
        self.arr.pop()
        pointer=0
        child_pointer1=(2*pointer) +1 
        child_pointer2=(2*pointer) +2
        while(child_pointer2<len(self.arr)):
            minimum=min(self.arr[child_pointer1],self.arr[pointer],self.arr[child_pointer2])
            if(minimum==self.arr[pointer]):
                break
            elif(minimum==self.arr[child_pointer1]):
                self.arr[child_pointer1],self.arr[pointer]=self.arr[pointer],self.arr[child_pointer1]
                pointer=child_pointer1
                child_pointer1=2*pointer +1 
                child_pointer2=2*pointer +2
            elif(minimum==self.arr[child_pointer2]):
                self.arr[child_pointer2],self.arr[pointer]=self.arr[pointer],self.arr[child_pointer2]
                pointer=child_pointer2
                child_pointer1=2*pointer +1 
                child_pointer2=2*pointer +2
        if(child_pointer1<len(self.arr)):
            minimum=min(self.arr[child_pointer1],self.arr[pointer])
            if(minimum==self.arr[child_pointer1]):
                self.arr[child_pointer1],self.arr[pointer]=self.arr[pointer],self.arr[child_pointer1]

        
                

