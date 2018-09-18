# coding: utf-8
# built a stack and queue

from singlelist import Lnode

class Stackerror(ValueError):
    pass
class Queueerror(ValueError):
    pass


#基于顺序表定义栈（LIFO）
class Sstack():

    def __init__(self):
        self._elem=[]
        self.depth=0

    def is_empty(self):
        return self._elem == []

    def depths(self):
        return  self.depth

    def push(self,_elem):
        self._elem.append(_elem)
        self.depth += 1

    def pop(self):
        if self.is_empty():
            raise Stackerror
        self.depth-=1
        return self._elem.pop()

    def top(self):
        if self.is_empty():
            raise  Stackerror
        return self._elem[-1]


#基于链表思想的实现，其实这种实现方法很简单
class Lstack():

    def __init__(self):
        self._head=None
        self.depth=0

    def is_empty(self):
        return self._head is None

    def depths(self):
        return  self.depth

    def push(self,_elem):
        self._head=Lnode(_elem,self._head)
        self.depth+=1

    def pop(self):
        if self._head is None:
            raise  Stackerror
        self.depth-=1
        p=self._head.elem
        self._head=self._head.next
        return p

    def top(self):
        if self._head is None:
            raise Stackerror
        return self._head.elem



#基于循环顺序表，即把固定大小的一个list看成是首尾循环的，然后基于此
#一直遵循头部取，尾部存的原则，但是这个头部并不保存移动，而是不断增加

class queue():

    def __init__(self,_len):
        self.len=_len
        self.elem=[0 for x in range(self.len)]
        self.head=0
        self.num=0

    def is_empty(self):
        return self.num is 0

    #查看队列头部的元素，也就是即将出队列的元素
    def  peek(self):
        if self.num ==0:
            raise Queueerror(" no elem")
        else:
            e=self.head[self.head]
            return e
    #从队列中输出一个元素
    def dequeue(self):
        if self.num ==0:
            raise  Queueerror(' no elem')
        e=self.elem[self.head]
        self.elem[self.head]=0
        self.head=(self.head+1)%self.len
        self.num-=1
        return e

    #往队列中（队尾）加入一个元素
    def enqueue(self,_elems):
        if self.num==self.len:
            self.extend()
        else:
            self.elem[(self.head+self.num)%self.len]=_elems
            self.num+=1

    #当队列存储满之后，也就是固定大小的list已经被占满之后，更新块
    def extend(self):
        old_len=self.len
        self.len=old_len*2
        new_list=[0]*self.len
        for i in range(self.num):
            new_list[i]=self.elem[(self.head+i)%old_len]
        self.elem=new_list
        self.head=0

    def ptintall(self):
        print(self.elem)


if __name__=='__main__':
    stack=Lstack()
    for x in range(10):
        stack.push(x)
    while not stack.is_empty():
        p=stack.pop()
        print(p)

    que=queue(8)
    for x in range(7):
        que.enqueue(x)
    que.ptintall()
    for x in range(2):
        que.dequeue()
    que.ptintall()
    for x in range(9,20):
        que.enqueue(x)
    que.ptintall()








