# coding: utf-8
# built a loop circle  list
from singlelist import Lnode
class LClist ():
    def __init__(self):
        self._rear=None

    #前端插入
    def prepend(self,elem_):
        p = Lnode(elem_)
        if self._rear is None:
            p.next=p
            self._rear=p
        else:
            p.next=self._rear.next
            self._rear.next=p
    #后端插入
    def append(self,elem_):
        p= Lnode(elem_)
        if self._rear is None:
            p.next=p
            self._rear=p
        else:
            p.next=self._rear.next
            self._rear.next=p
            self._rear=p
    #前端删除
    def prepop(self):
        if self._rear is None:
            raise ValueError
        p=self._rear.next
        if self._rear is p:
            self._rear=None
        else:
            self._rear.next =p.next
        return p.elem

    #后端删除,操作同单链表没有本质区别
    def pop_last(self):
        if self._rear is None:
            raise ValueError
        p=self._rear.next
        if self._rear is p:
            e=self._rear.elem
            self._rear=None
            return e
        while p.next is not self._rear:
            p=p.next
        e=p.next.elem
        p.next=self._rear.next
        self._rear=p
        return e

    #判断是否为空
    def is_empty(self):
        return self._rear is None

    #基本的打印操作
    def printall(self):
        #if self.is_empty():
            #return
        p=self._rear.next
        while True:
            print(p.elem, end=' ')
            if p is self._rear:
                break
            p=p.next
        print(' ')


if __name__=='__main__':
    lclist1=LClist()
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

