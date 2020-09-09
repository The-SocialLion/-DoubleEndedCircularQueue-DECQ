from collections import OrderedDict
class DoubleEndedCircularQueue:
    def __init__(self):
        self.DECQ=[]
        self.limit=int (input("enter limit"))
        self.front=None
        self.rear=None
    def isFull(self):
      if len(self.DECQ)==self.limit:
        return True
      else:
        return False
    def isEmpty(self):
          if self.front == None and self.rear==None:
            return True
          else:
            return False
    def enqueueRear(self,ele):
        if self.rear==self.limit-1:
            print("queue overflow")
        elif self.isFull():
            print("queue overflow")
        else:
            if self.front==None and self.rear==None:
                 self.front=self.rear=0
            else:
                self.rear=(self.rear+1)%self.limit
            self.DECQ.append(ele)
    def enqueueFront(self,ele):
        if self.isFull():
            print("queue overflow")
        else:
            if self.front==None and self.rear==None:
                self.front=self.rear=0
            else:
                 self.front=(self.front-1)%self.limit
            self.DECQ.insert(0,ele)
    def dequeueFront(self):
        if self.front ==None:
            print("queue underflow")
        elif self.isEmpty():
            print("queue underfloe")
        else:
            print(self.DECQ.pop(0))
            if self.front==self.rear:
                self.front=self.rear=None
            else:
                self.front=(self.front+1)%self.limit
    def dequeueRear(self):
        if self.rear==None:
            print("queue underflow")
        elif self.isEmpty():
             print("queue underflow")
        else:
            print(self.DECQ.pop())
            if self.front==self.rear:
                 self.front=self.rear=None
            else:
                 self.rear= (self.rear-1)%self.limit
    def find(self,ele):
        flag=False
        if self.isEmpty():
          print("queue underflow")
        else:
           for i in range(0,len(self.DECQ)):
             if self.DECQ[i]==ele:
               print("element found @",i)
               break
             else:
              print("element not found")
              break
    def display(self):
        if self.isEmpty():
            print("queue underflow")
        else:
            for i in self.DECQ:
             print(i,end=" ")
             print()
    def reset(self):
       if self.isEmpty():
        print("queue underflow")
       else:
          self.DECQ=self.DECQ.clear()
          print("queue has been reset")
          
    def remove_dup(self):
       if self.isEmpty():
        print("queue underflow")
       else:
        self.DECQ= list(OrderedDict.fromkeys(self.DECQ))  
        print("duplicate elements removal succesfull!")
    def xchange(self,ele,pos):
      flag=False
      if self.isEmpty():
        print("queue underflow")
      else:
        for i in range(0,len(self.DECQ)):
          if i==pos :
            self.DECQ[i]=ele
            flag=True
            break
        if flag:
          print("element exhange succesfull")
          print(self.DECQ)
        else:
          print("element exchange unsuccesfull")

    

    

decq=DoubleEndedCircularQueue()
while True:
  print("1.enqueue-rear,2.enqueue-front")
  print("3.dequeue-rear 4.dequeue-front")
  print("5.display,6.find,7 exchange")
  print("8.remove-duplicates,9.reset-list,10.exit")
  ch=int(input("enter your choice"))
  if ch==1:
     ele=int(input("enter element"))
     decq.enqueueRear(ele)
  elif ch==2:
     ele=int(input("enter element"))
     decq.enqueueFront(ele)
  elif ch==3:
     decq.dequeueRear()
  elif ch==4:
     decq.dequeueFront()
  elif ch==5:
      decq.display()
  elif ch==6:
      ele=int(input("enter element"))
      decq.find(ele)
  elif ch==7:
      ele=int(input("enter element"))
      pos=int(input("enter position"))
      decq.xchange(ele,pos)  
  elif ch==8:
      decq.remove_dup()
  elif ch==9:
      decq.reset()
  elif ch==10:
       break
  else:
      print("invalid choice,try again!")

