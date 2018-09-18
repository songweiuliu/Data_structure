# coding: utf-8
# About huffman encoding

from priqueue_heap import *
from Binarytree import Binnode,printallnode


#由于要基于优先序列（堆实现的）实现huffman编码，因此节点存储的数据是二叉树节点（父节点，左右子节点）
#因此要实现优先序列，必须实现序列中元素的可比性，也就是要给节点增加比较大小的属性

class Huffmannode(Binnode):
    #对于派生类一般不用重新定义初始化函数，只定义不同的部分
    # def __init__(self,elem_,left_=None,right_=None):
    #     Binnode.__init__(elem_,left_,right_)
    def __lt__(self, other):
        return self.data<other.data

    def __gt__(self, other):
        return self.data>other.data

    def __le__(self, other):
        return self.data<=other.data

    def __ge__(self, other):
        return self.data>=other.data

#基于优先队列Priqu_heap派生出一个衍生类，该类的是基于堆（二叉树实现的），
# 根节点优先级最高（最小），如果元素可比较的话，上面一定赋予了node可比较性
class Huffmanprioque(Prique_heap):
    #对于派生类一般不用重新定义初始化函数，只定义不同的部分
    # def __init__(self,elems_=[]):
    #     Prique_heap.__init__(elems_.copy())
    #增加一个统计节点数目的性质
    def nums(self):
        return len(self.elem)


#基于以上两个类完成给定W向量的霍夫曼编码
def Huffmanencode(w):
    if w ==[]:
        raise INDEXerror('No elem to encoding')
    hmque=Huffmanprioque()
    for x in w:
        hmque.enqueue(Huffmannode(x))
    #Huffmanprioque(w)                  #可以达到同样的效果，直接初始化筛选排序
    while hmque.nums()>1:
        a=hmque.dequeue()
        b=hmque.dequeue()
        c=a.data+b.data
        hmque.enqueue(Huffmannode(c,a,b))   #依次弹出父节点数值最小的两个节点（子树）（节点之间具有比较能力）
                                            #然后将他们新组成的树加入优先序列（每次迭代序列元素数减一）
    return hmque.dequeue()                  #得到最终的完整的huffman编码树，对应有限序列最后一个得到的树（节点）





if __name__=='__main__':

# 基于Binary tree里面的一些函数，堆最终得到的完整的树可以进行一些诸如遍历，还有打印等各种操作
    weights=[2,2,5,10,4,3,7]
    t=Huffmanencode(weights)
    printallnode(t)
#由C,W还有具体的树，便可以得到各字符的编码，进而得到最优编码进行编解码




