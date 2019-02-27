#   Author: Ana Luisa Mata Sanchez
#   Course: CS2302
#   Assignment: Lab #2
#   Instructor: Olac Fuentes
#   Description: Implement several algorithms for finding the median of a list of integers.
#   T.A.: Anindita Nath
#   Last modified: 02/22/2019
#   Purpose: Use bubble sort, merge sort, and two types of quick sort

import random

#Node Functions
class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 
        
#List Functions
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        
def IsEmpty(L):  
    return L.head == None     
        
def Append(L,x): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next
        
def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line 
    
def Remove(L,x):
    # Removes x from list L
    # It does nothing if x is not in L
    if L.head==None:
        return
    if L.head.item == x:
        if L.head == L.tail: # x is the only element in list
            L.head = None
            L.tail = None
        else:
            L.head = L.head.next
    else:
         # Find x
         temp = L.head
         while temp.next != None and temp.next.item !=x:
             temp = temp.next
         if temp.next != None: # x was found
             if temp.next == L.tail: # x is the last node
                 L.tail = temp
                 L.tail.next = None
             else:
                 temp.next = temp.next.next    

def GetLength(L):
    temp = L.head
    count = 0
    #traverse and count each element traversed
    while temp is not None:
        count += 1
        temp = temp.next
    return count

def NewRandList(n):
    #Creates a new list of size n with random numbers between 0 and n+100
    L = List()
    for i in range(n):
        Append(L,random.randint(0,n+100))
    return L

def BubbleSort(L):
    #boolean to keep track if its sorted
    isSorted = False
    curr = L.head
    #if empty or only one element, no need to sort
    if L.head == None or curr.next == L.tail:
        return L
    #onlyl sorts if it isnt sorted
    while isSorted == False:
        curr = L.head
        #if it never reaches the if statement, it stays true... it did not swap any elements
        isSorted = True
        for i in range(GetLength(L)-1):
            #Compare adjacent elements, if the first is larger than the second then swap
            if curr.item > curr.next.item and curr.next!=None and curr!=None:
                temp = curr.next.item
                curr.next.item = curr.item
                curr.item = temp
                #since there has been a swap, we have to sort again
                isSorted = False
            curr = curr.next
    return L

def MergeSort(L):
    if GetLength(L)>1:
        #create a left and right 
        A = List()
        B = List()
        half = GetLength(L)//2
        temp = L.head
        
        #Sepparate in two, first loop goes from element 0 to the half
        for i in range(half):
            Append(A,temp.item)
            temp = temp.next
        #Second loop goes from one after the half to the end
        while temp!= None:
            Append(B,temp.item)
            temp = temp.next
        
        #keep separating until there is only one element
        MergeSort(A)
        MergeSort(B)
        
        #Merge them and make that the new list
        L.head = Merge(A, B).head
        return L


    
def Merge(A, B):
    #new list that will contain left and right
    L = List()
    
    #temp variables for iterating
    left = A.head
    right = B.head
    
    while left!=None and right!=None:
        #compare the items in left an right, if left is smaller append it and advance the left
        if left.item < right.item:
            Append(L, left.item)
            left = left.next
        #if not, append the right element and advance the right pointer, thus you will append from smallest to biggest
        else:
            Append(L, right.item)
            right = right.next
    
    #Checking if any elements were left in either of the lists
    if right == None:
        while left != None:
            Append(L, left.item)
            left = left.next

    elif left == None:
        while right != None:
            Append(L, right.item)
            right = right.next
    return L

def QuickSort(L):
    if GetLength(L)>1:
        #Pick the pivot
        pivot = L.head.item
        #create a left and right from the pivot
        left = List()
        right = List()
    
        temp = L.head.next
        while temp!=None:
            #if it is bigger than the pivot put it on right
            if temp.item>pivot:
                Append(right,temp.item)
            #if it is smaller put it on the left
            else:
                Append(left,temp.item)
            #keep going until you reach the end of the list
            temp = temp.next
        #Now split in two again
        QuickSort(left)
        QuickSort(right)
        
        #Add the pivot that wasn't included
        Append(left, pivot)
        
        #Merge from left to right
        left.tail.next = right.head
        
        #Now put that merged list into the original list to sort
        #if both lists have things, the head is the left and the tail is the right
        if left.head!=None and right.tail!=None:
            L.head = left.head
            L.tail = right.tail
        #if left is none then right is the new list
        elif left.head == None:
            L.head = right.head
            L.tail - right.tail
        #if right is none then left is the new list
        elif right.head == None:
            L.head = left.head
            L.tail = left.tail
            
        return L
   
def ModifiedQuickSort(L,n):
    if GetLength(L)>=1:
    
        #pick the pivot
        pivot = L.head.item
        #create lists for left and right
        left = List()
        right = List()
        temp = L.head.next
        
        while temp!=None:
            #if it is bigger than the pivot put it on right
            if temp.item>pivot:
                Append(right,temp.item)
            #if it is smaller put it on the left
            else:
                Append(left,temp.item)
            #keep going until you reach the end of the list
            temp = temp.next
        
        #if the median is in the right, "sort" the right
        if GetLength(left) < n :
            return ModifiedQuickSort(right, n-GetLength(left)-1)  
        #if the median is the pivot
        elif GetLength(left) == n:
            return pivot
        #if the median is in the left, "sort" the left
        elif GetLength(left) > n:
            return ModifiedQuickSort(left, n) 
    else:
        return L.head.item    

def Median(L):
    #if the list is empty
    if L.head is None:
        return None
    else:
        temp = L.head
        count = 0
        #traverse the list and count until you reach the middle
        while temp!=None and count!=GetLength(L)//2:
            count+=1
            temp = temp.next

        return temp

def Copy(L):
    #new list
    N = List()
    temp = L.head
    while temp!=None:
        #manually copy each number of the old list
        Append(N, temp.item)
        temp = temp.next
    #return the new copy
    return N

L = List()
L = NewRandList(5)

A = Copy(L)
B = Copy(L)
C = Copy(L)
 
############### Bubble Sort ###############
print("*************Bubble Sort************")
print("Original List: ")
Print(L)
A = BubbleSort(A)
print("Median: ")
print(Median(A).item)
print()

############### Merge Sort ###############
print("*************Merge Sort*************")
print("Original List: ")
Print(L)
B = MergeSort(B)
print("Median: ")
print(Median(B).item)
print()
        
############### Quick Sort ###############
print("*************Quick Sort*************")
print("Original List: ")
Print(L)
C = QuickSort(C)
print("Median: ")
print(Median(C).item)
print()

############### Modified Quick Sort ###############
print("*********Modified Quick Sort********")
print("Original List: ")
Print(L)
print("Median: ")
print(ModifiedQuickSort(L, GetLength(L)//2))
print()
