# coding: utf-8
# Build a Prioque 基于顺序表或者堆技术实现优先队列


#优先队列：按优先级排序保存了事件或者运算符号的队列，最先弹出的元素一定是目前优先级最高的元素
#实现方式1:按优先级顺序存储O（n），然后直接弹出使用O(1)，比如在顺序表的尾端取用（优先级已被排序成最高）
#实现方式2：乱序存储O(1)，让后每次取用都检索最高优先级的O(N)

#基于list,以方式一实现优先队列

class INDEXerror(IndexError):
    pass

class  Prique_list():

    def __init__(self,elist=[]):
        self.elem=elist.copy()
        self.elem.sort(reverse=True)

    def is_empty(self):
        return  len(self.elem)==0

    def peek(self):
        if self.is_empty():
            raise INDEXerror
        e=self.elem[-1]
        return e
    def enqueue(self,e):
        i=len(self.elem)-1
        while i>=0:
            if e <= self.elem[i]:
                break
            else:
                i-=1
        self.elem.insert(i+1,e)

    def dequeue(self):
        if self.is_empty():
            raise INDEXerror
        return self.elem.pop()




#基于堆实现优先队列，所谓的堆的定义如下：
#堆便是结点存储了数据的完全二叉树，堆中存储的数据要
#满足条件：任意结点的数据（所考虑的序）要大于等于其子节点的序（如果存在）
#Q1:在一个堆最后加入一个元素，仍是完全二叉树，但未必是堆
#Q2:将一个堆去掉堆顶，子树仍然是堆
#Q3:给Q2形成的子树加入一个根元素，仍是完全二叉树，但是未必是堆，根节点不一定满足堆序
#Q4：去掉一个堆的最后一个元素，剩下的元素仍然是堆

#插入元素向上筛选，插入的元素不断与父节点比较，如果e较小然后交换（优先级高，位置上移）
#实现的基础是基于顺序表存储二叉树（即二叉树与顺序表结构一一映射，i,2i+1,j,j-1/2）
class Prique_heap():

    def __init__(self,elem=[]):
        #支持初始化一个堆，不一定满足堆序，所以要进行堆序排列
        self.elem=elem.copy()
        if self.elem:
            self.priheap()

    def is_empty(self):
        return self.elem==[]

    #查看优先级最高的结点，也就是根节点，也就是顺序表的第一个元素
    def peek(self):
        if self.is_empty():
            raise  INDEXerror('NO elem')
        return self.elem[0]


    #加入元素
    def enqueue(self,e):
        self.elem.append(e)
        self.siftup(self.elem,e,len(self.elem)-1,0)

    #对堆加入元素，并进行向上筛选函数使其重新成为堆,e加入元素，
    # last从哪里开始向上，一般必须到o结束,这里以jiezhi代表向上筛选的截至点
    def siftup(self,heap_,e,last,jiezhi):
        elems,i,j= heap_,last,(last-1)//2
        while j>=jiezhi:
            if e<elems[j]:
                elems[i]=elems[j]
                i, j = j, (j - 1) // 2
            else:
                break
        elems[i]=e


    #弹出元素，首先去除堆顶元素（优先级最高），默认其弹出（可以随意覆盖）
    #然后取堆尾元素加入堆顶，然后再执行向下筛选，使其满足堆序,
    # root_向下筛选排序的元素，begin是向下开始位置,end为结束的位置
    def dequeue(self):
        if self.is_empty():
            raise  INDEXerror('NO elem')
        e=self.elem[0]
        root_=self.elem.pop()
        if len(self.elem)>0: 
            self.siftdowm(self.elem,root_,0,len(self.elem))
        return e

    #向下筛选,使其重新成为堆
    def siftdowm(self,heap_,root_,begin_,end_):
        elems,begin,end=heap_,begin_,end_
        i ,j = begin, 2*begin+1
        while j<end:
            if j+1<end and elems[j+1]<=elems[j]:
                j+=1
            if root_>elems[j]:
                elems[i]=elems[j]
                i, j = j, 2 * j + 1
            else:
                break
        elems[i]=root_

    #定义堆出事元素进行排序的堆，即从第一个叶子结点开始向下筛选，然后再一次堆它之上的所有结点
    #重复这个操作
    #由于叶子节点之间没有互相的堆序比较，所以有叶子节点数的点不需要进行向下筛选，然后再他们基础上加入节点并执行向下筛选

    def priheap(self):
        end=len(self.elem)
        for i in range(end//2,0,-1):
            self.siftdowm(self.elem,self.elem[i],i,end)


if __name__=='__main__':


    ph=Prique_heap([1,2,6,7,8,7,8,5,4])
    print(ph.elem)
    ph.enqueue(0)
    print(ph.elem)
    ph.dequeue()
    print(ph.elem)
    print(ph.peek())
    #完全正确
    ph=Prique_list([1,2,6,7,8,7,8,5,4])
    print(ph.elem)
    ph.enqueue(0)
    print(ph.elem)
    ph.dequeue()
    print(ph.elem)
    print(ph.peek())
    #完全正确










