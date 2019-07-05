# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 22:41:28 2019

@author: Tanujdeep
"""


def merge(l1,l2):
    l3=[]
    i=j=0
    max1=len(l1)
    max2=len(l2)
    while(i<max1 and j<max2):
        if(l1[i]<l2[j]):
            l3.append(l1[i])
            i+=1
            
        else:
            l3.append(l2[j])
            j+=1
    if(i<max1):
        l3.append(l1[i])
    if(j<max2):
        l3.append(l2[j])
    return l3
def mergesort(unsorted):
    max=len(unsorted)
    if(max>1):
        mid=max//2
        left=unsorted[0:mid]
        right=unsorted[mid:max]
        sortedL=mergesort(left)
        sortedR=mergesort(right)
        sorted=merge(sortedL,sortedR)
        return sorted
    else:
        return unsorted
l23=[2,5,6,3,65,34,6,67,5,8,45,67,3,78,3,87,35,7,78]


l32=mergesort(l23)
print(l32)