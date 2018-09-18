# coding: utf-8
# built a double (loop circle) linked list
from singlelist import Lnode,Llist1

#双向链表节点类
class DLnode(Lnode):
    def __init__(self,elem_,prev_=None,next_=None):
        Lnode.__init__(self,elem_,next_)
        self.prev=prev_

#双链表添加了反向链接，使得头部插入删除和尾部插入删除操作均具有常量的操作时间O（1）
class DLlist(Llist1):
    def __init__(self):
        Llist1.__init__(self)

    #头部插入
    def prepend(self,elem_):
        p=DLnode(elem_)
        if self._head is None:
            self._rear=p
        else:
            p.next=self._head
            self._head.prev=p
        self._head = p

    #尾部插入
    def append(self,elem_):
        p=DLnode(elem_)
        if self._head is None:
            self._head=p
        else:
            p.prev=self._rear
            self._rear.next=p
        self._rear=p

    #头部删除
    def prepop(self):
        if self._head is None:
            raise ValueError
        e=self._head.elem
        self._head=self._head.next
        if self._head is None:
            self._rear=self._head
        else:
            self._head.prev=None
        return e

    #尾部删除
    def pop_last(self):
        if self._head is None:
            raise ValueError
        e=self._rear.elem
        self._rear = self._rear.prev
        if self._head.next is None:
            self._head=self._head.next
        else:
            self._rear.next=None
        return e

    #判断是否为空
    def is_empty(self):
        return self._rear is None

    #基本的打印操作
    def printall(self):
        if self.is_empty():
            return
        p=self._head
        while True:
            print(p.elem, end=' ')
            if p is self._rear:
                break
            p=p.next
        print(' ')




#训练双链表此时并不能比普通双链表节省时间，因此这里不再加以实现

if __name__=='__main__':

    lclist1=DLlist()
    for i in range(0,5):
        lclist1.prepend(i)
    lclist1.printall()
    print(' ')

    for i in range(5,10):
        lclist1.append(i)
    lclist1.printall()
    print(' ')

    for i in range(4):
        lclist1.prepop()
    lclist1.printall()
    print(' ')

    for i in range(3):
        lclist1.pop_last()
    lclist1.printall()
    print(' ')




