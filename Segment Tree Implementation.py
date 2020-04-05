#this segment Tree represents a sum of the segmants
"""
arr=[1, 34 ,345 ,32 ,67 ,89 ,3]

                       571
                  /            \.
           412                   159
        /       \                 /     \.
    35         377         156      3
  /  \          /   \       /     \.
1   34     345   32   67    89

"""


class SegmentTree :
    def __init__(self,arr):
        self.arr=arr
        self.tree=[None for _ in range(2*len(arr))]
        self.buildTree(0,0,len(arr)-1)
        while self.tree[-1] is None :
            self.tree.pop()
        
    
    def buildTree(self,tree_index,start, end):
        if start==end :
            self.tree[tree_index]=self.arr[start]
            return 0

        mid=(start+end)//2
        self.buildTree((2*tree_index)+1,start,mid)
        self.buildTree(2*(tree_index+1),mid+1,end)

        self.tree[tree_index]=self.tree[(2*tree_index)+1] + self.tree[2*(tree_index + 1)]
    
    def update(self,index,val,tree_index=0,start=0,end=None):
        if end is None:
            end=len(self.arr)-1

        if start==end:
            self.arr[index]=val
            self.tree[tree_index]=val
            return 0

        mid=(start+end)//2
        if index <=mid : 
            self.update(index,val, (2*tree_index)+1 ,start,mid)
        else:
            self.update(index,val, 2*(tree_index+1) ,mid+1,end)
        
        self.tree[tree_index]=self.tree[(2*tree_index)+1] + self.tree[2*(tree_index + 1)]

    def runQuery(self, left,right,tree_index=0,start=0,end=None):
        if end is None :
            end=len(self.arr)-1

        if end<left or start>right :                        #lL-R range is completely outside the treenode range
            return 0

        elif start>=left and right>=end :               #L-R range is completely inside the tree node range
            return self.tree[tree_index]

        else :  
            mid= (start+end)//2
            ans1= self.runQuery(left,right,(2*tree_index)+1,start,mid)
            ans2=self.runQuery(left,right,(2*tree_index)+1,mid+1,end)
            return ans1+ans2




obj=SegmentTree([1, 34 ,345 ,32 ,67 ,89 ,3])
print (obj.tree)

obj.update(6,56)

print (obj.tree)
print (obj.arr)

print(obj.runQuery(0,1))