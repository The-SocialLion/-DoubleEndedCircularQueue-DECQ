class DoubleEndedCircularQueue:
    def __init__(self):
        self.DECQ=[]
        self.limit=10
        self.front=None
        self.rear=None
    def isFull(self):
      if len(self.DECQ)==self.limit:
        return True
      else:
        return False
    def isEmpty(self):
          if len(self.DECQ)==0:
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
           for i in self.DECQ:
             if i==ele:
               flag=True
               break
           if flag:
             print("element found")
           else:
             print("element not found")
    def display(self):
        if self.isEmpty():
            print("queeu underflow")
        else:
            for i in self.DECQ:
             print(i,end=" ")
             print()

decq=DoubleEndedCircularQueue()
while True:
  print("1.enqueue-rear,2.enqueue-front")
  print("3.dequeue-rear 4.dequeue-front")
  print("5.display,6.find,7.exit")
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
      break
