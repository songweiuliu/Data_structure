# coding: utf-8
# Build a binary tree

from stack_queue import queue,Sstack


class Binnode():
    """定义二叉树的类结点"""
    def __init__(self,data_,left_=None,right_=None):
        self.data=data_
        self.left=left_
        self.right=right_

#t=Binnode(1,Binnode(5,Binnode(4)),Binnode(3,Binnode(6,None,Binnode(8))))
#定义一些二叉树的遍历还有统计函数,均是基于深度优先遍历



#统计二叉树的节点数,递归算法
def Counternode(t):
    if t is None:
        return 0
    return 1+Counternode(t.left)+Counternode(t.right)

#如果节点里面存储的都是数字，对这些数字进行求和的函数,递归算法
def Sumnode(t):
    if t is None:
        return 0
    return t.data+Sumnode(t.left)+Sumnode(t.right)

#对二叉树中的元素进行遍历，有几种方式DLR,LDR,LRD
#DLR 先根序遍历
def DLRorder(t,proc):
    # if not isinstance(t,Binnode()):
    #     raise ValueError
    if t is None:
        return
    proc(t.data)
    DLRorder(t.left,proc)
    DLRorder(t.right,proc)

#LDR  中序遍历
def LDRorder(t, proc):
    # if not isinstance(t,Binnode()):
    #     raise ValueError

    if t is None:
        return
    LDRorder(t.left,proc)
    proc(t.data)
    LDRorder(t.right,proc)

#LRD  后根序遍历
def LRDorder(t, proc):
    # if not isinstance(t,Binnode()):
    #     raise ValueError

    if t is None:
        return
    LRDorder(t.left,proc)
    LRDorder(t.right,proc)
    proc(t.data)

#打印输出整棵树,基于先根须遍历的顺序，不过通过括号是能看出来整个树的结构的，递归算法
def printallnode(t):
    # if not isinstance(t,Binnode):
    #     raise ValueError
    if t is None:
        print("*",end=' ')
        return
    print('('+str(t.data),end=' ')
    printallnode(t.left)
    printallnode(t.right)
    print(')',end=' ')


#基于非递归方法的深度优先遍历，例如先根序遍历，非递归方法的有点是可以暴漏算法细节，
# 遍历分析,算法运行正确,时间复杂度和空间复杂度都是O（N），平均空间复杂度是hiO(LOGn)
def DLRorder_nonrec(t,proc):
    s=Sstack()
    while t is not None or not s.is_empty():
        while t is not None:    #沿着左分支下行
            proc(t.data)        #先根序处理数据
            s.push(t.right)     #保存右分支
            t=t.left
        t=s.pop()               #遇到空树，回溯

#基于非递归先根序遍历的迭代器
def DLRorder_elments(t):
    s=Sstack()
    while t is not None or not s.is_empty():
        while t is not None:    #沿着左分支下行
            yield t.data        #先根序处理数据
            s.push(t.right)     #保存右分支
            t=t.left
        t=s.pop()               #遇到空树，回溯

#基于非递归算法的中序遍历
def LDRorder_nonrec(t,proc):
    s=Sstack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t)
            t=t.left
        t=s.pop()
        proc(t.data)
        t=t.right

#基于非递归算法的后根序遍历，比较复杂、
def LRDorder_nonrec(t,proc):
    s=Sstack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t)                                       #将节点入栈
            t=t.left if t.left is not None else t.right     #向下遍历存入所有的左节点

        t=s.pop()                  #当找到最下方的左节点时退出上面的循环，然后依次取出栈顶元素
        proc(t)                    #堆当前栈顶元素处理，第一个是最左下方的节点，现在的栈顶是其父节点
        if not s.is_empty() and s.top().left==t:
            t=s.top().right         #如果当前处理的是父节点的左节点，则转向右节点，然后进入上面的循环入栈
        else:
            t=None                  #没有右子树或者右子树处理完毕，强制退栈
                                    # 此时应该继续弹出节点（父节点）然后继续处理


#对于队列的宽度优先遍历
def levelorder(t,proc):
    qu=queue(8)
    qu.enqueue(t)
    while not qu.is_empty():
        e=qu.dequeue()
        if e is None:
            continue
        qu.enqueue(e.left)
        qu.enqueue(e.right)
        proc(e.data)



#基于类的方法构建一棵二叉树

class binarytree():

    def __init__(self):
        self.root_=None

    def is_empty(self):
       return  self.root_==None

    def root(self):
        return self.root_

    def leftchild(self):
        
        return self.root_.left

    def rightchild(self):
        return self.root_.right

    def set_root(self,rootnode):
        self.root_=rootnode

    def set_left(self,node_):
        self.root_.left=node_

    def set_right(self, node_):
        self.root_.right = node_

    def node_elements(self):
        s,t = Sstack(),self.root_
        while t is not None or not s.is_empty():
            while t is not None:  # 沿着左分支下行
                s.push(t.right)  # 保存右分支
                yield t.data  # 先根序处理数据
                t = t.left
            t = s.pop()  # 遇到空树，回溯


if __name__=='__main__':
    #测试实例
    t=Binnode('A',Binnode('B',Binnode('D',None,Binnode('H')),Binnode('E',None,Binnode('I'))),\
              Binnode('C',Binnode('F',Binnode('J'),Binnode('K')),Binnode('G')))
    #统计结点个数
    num=Counternode(t)
    print(num,end=' ')
    #三种遍历方法 递归
    DLRorder(t,print)
    print(' ')
    LDRorder(t,print)
    print(' ')
    LRDorder(t,print)
    print(' ')

    # 非递归先根序遍历测试
    DLRorder_nonrec(t, print)
    print(' ')
    # 非递归先根序生成器
    for x in DLRorder_elments(t):
        print(x)
    print(' ')
    # 基于类的二叉树的基于非递归先根序生成器
    ct = binarytree()
    ct.set_root(t)
    for x in ct.node_elements():
        print(x)

    # levelorder(t,print)
    # print(' ')

    #打印出来整棵树的结构
    printallnode(t)
    print(' ')
    t1 = Binnode(1, Binnode(5, Binnode(4)), Binnode(3, Binnode(6, None, Binnode(8))))
    sum=Sumnode(t1)
    print(sum,end=' ')


