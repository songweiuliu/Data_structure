# coding: utf-8
# built a single linked list
class Lnode():
    def __init__(self,elem_,next_=None):
        self.elem=elem_
        self.next=next_
class listeroor(ValueError):
    pass

#循环单链表，仅含有头部指针,因此尾部操作都是O（n）的复杂度

class Llist():

    def __init__(self):
        self._head=None

    #判空?
    def is_empty(self):
        return self._head is None

    #头部加入
    def prepend(self,elem_):
        self._head=Lnode(elem_,self._head)

    #头部删除
    def prepop(self):
        if self._head is None:
            raise  listeroor("in prepop")
        else:
            e=self._head.elem
            self._head=self._head.next
            return e
    #后端加入
    def append(self,elem_):
        if self._head is None:
            self._head=Lnode(elem_)
            return
        p=self._head
        while p.next is not None:
            p=p.next
        p.next=Lnode(elem_)

    #尾端删除
    def pop_last(self):
        if self._head is None:
            raise listeroor('in last pop')
        p=self._head
        while p.next.next is None:
            p=p.next
        e=p.next.elem
        p.next=None
        return e

    #定位寻找操作，只能返回找到的第一个满足条件的元素
    def findfirst (self,prep):
        if self._head is None:
            raise listeroor
        p=self._head
        while p is not None:
            if prep(p.elem):
                return p.elem
            p=p.next
    #迭代生成器，可以找出所有的满足条件的元素
    def findall (self,prep):
        if self._head is None:
            raise listeroor
        p=self._head
        while p is not None:
            if prep(p.elem):
                yield p.elem
            p=p.next

    #打印方法，打印出所有的元素
    def printall(self):
        p=self._head
        while p is not None:
            print(p.elem)
            if p.next is None:
                print (' ',end='')
            p=p.next
        print(' ')
    #遍历元素，对所有的元素进行某项操作，通常配合lamda函数
    def for_each(self,proc):
        p=self._head
        while p is not None:
            proc(p.elem)
            p=p.next

    #迭代器，可以迭代输出所有的元素
    def elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

#循环单链表的简单变形 加入了尾部指针 此时仅有尾部的删除操作是O（n）
class Llist1(Llist):

    def __init__(self):
        Llist.__init__(self)
        self._rear=None

    #重新定义所有的变动操作，非变动操作不需要重新定义
    #头部加入
    def prepend(self,elem_):
        if self._head is None:
            self._head=Lnode(elem_,self._head)
            self._rear=self._head
        else:
            self._head=Lnode(elem_,self._head)

    #头部删除
    def prepop(self):
        if self._head is None:
            raise  listeroor("in prepop")
        if self._head.next is None:
            e=self._head.elem
            self._head=None
            self._rear=None
            return e
        else:
            e=self._head.elem
            self._head=self._head.next
            return e

    #后端加入
    def append(self,elem_):
        p=Lnode(elem_)
        if self._head is None:
            self._head=p
            self._rear=self._head
        self._rear.next=p
        self._rear=p

    #尾端删除
    def pop_last(self):
        if self._head is None:
            raise listeroor('in last pop')
        p=self._head
        if p.next is None:
            e=p.elem
            self._head=None
            self._rear=None
            return e
        while p.next.next is not None:
            p=p.next
        e=p.next.elem
        p.next=None
        self._rear=p
        return e
#mainlist=Llist1()
#mainlist.prepend(10)



if __name__ == '__main__':
    list=Llist1()
    for i in range(0,10):
        list.prepend(i)
    for i in range(10,20):
        list.append(i)
    list.printall()
    for i in range(5):
        list.prepop()
    list.for_each(print)
    for i in range(5):
        list.pop_last()
    list.printall()
    for x in list.elements():
        print (x)
        print('')

