# coding: utf-8
# Build kinds of binary sort tree

#from Binary_sorttree import

#对于B树，除根节点外每个节点的关键码数位于（t-1）/2与t-1之间，每个节点的子节点数为位于（t-1）/2+1与t之间
#因此我们可以计算其高度的取值范围，根节点只有一个节点，第一层2个节点，第2层存在2t或者2[（t-1）/2 +1]个节点
#然后依次相乘t或者[（t-1）/2 +1]，最后得到总到的节点的关键码的数量为n，进而得到h的取值范围logt/2(n+1/2)最大
#根据这个利用数学归纳法可以得到关于B树高度范围的一个取值公式，显然节点关键码最多时对应最低的高度，否则对应最高的高度

#B树(或称B-树)是一种适用于外查找的树，它是一种平衡的多叉树。
#阶为M的B树具有下列结构特征：
#1.树的根或者是一片树叶，或者其儿子数在2和M之间。
#2.除根节点外的所有非树叶节点儿子数在┌M/2┐和 M之间。
#3.所有的树叶都在相同的高度。
#4.节点中包括n个关键字，n+1个指针，一般形式为： （n,P0,K1,P1,K2,P2,…,Kn,Pn）。每个结点中关键字从小到大排列，并且当该结点的孩子是非叶子结点时，
# 该k-1个关键字正好是k个儿子包含的关键字的值域的分划。




#我们讨论的是3阶B树，因此最大节点数为2，最大的儿子数为3，初始化这样一个节点
class Node(object):
    def __init__(self, key):                                                #该节点含有两个key值，最多右三个子树
        self.key1 = key
        self.key2 = None
        self.left = None
        self.middle = None
        self.right = None

    def isLeaf(self):                                                       #判断是否为叶子节点
        return self.left is None and self.middle is None and self.right is None

    def isFull(self):                                                       #判断节点是否为满
        return self.key2 is not None

    def hasKey(self, key):                                                  #判断节点里面是否含有关键码key
        if (self.key1 == key) or (self.key2 is not None and self.key2 == key):
            return True
        else:
            return False

    def getChild(self, key):                                                #得到一个节点的子节点，根据key所在的范围
        if key < self.key1:
            return self.left
        elif self.key2 is None:
            return self.middle
        elif key < self.key2:
            return self.middle
        else:
            return self.right


class Tree_2_3(object):                                                     #定义一棵2——3树

    def __init__(self):
        self.root = None


    def get(self, key):                                                     #得到key值所在的节点
        if self.root is None:
            return None
        else:
            return self._get(self.root, key)


    def _get(self, node, key):
        if node is None:
            return None
        elif node.hasKey(key):
            return node
        else:
            child = node.getChild(key)
            return self._get(child, key)


    def put(self, key):                                                     #将一个关键码key加入到该树，又树的性质我们可知最终一定是加到了叶子节点上面
        if self.root is None:
            self.root = Node(key)                                           #空树加到根上面
        else:
            pKey, pRef = self._put(self.root, key)                          #由于key关键码的加入根节点分裂产生的向上传递的Pkey与新形成的兄弟节点
            if pKey is not None:                                            #根节点确实产生了分类，重新定义根节点为一个新的节点
                newnode = Node(pKey)
                newnode.left = self.root
                newnode.middle = pRef
                self.root = newnode



    #得到由于key的加入节点node分裂产生的向上传递的Pkey与新形成的兄弟节点Pref，如果没有分裂那么返回的是None
    #由于是递归调用因此最先得到结果的是递归的最底层，也就是叶子节点处，此时node为叶子节点，那么key就是相当于下层的Pkey
    #而下层分裂产生的Pref是None，因此直接调用分类函数self._addtoNode(node, key, None)，得到叶子节点分类产生Pkey，Pref
    #然后向后传递，倒数第二层由Pkey，Pref再次分裂产生Pkey，Pref，按照这样向后传递更新沿途所有的节点

    #分类节点是存在以下情况：
    #如果新插入的key值最后在向下递归的时候的发现已经位于某个节点之中了，这个时候返回none,那么整个沿途路径上什么都不做
    #新插入的key值最终插入到了叶子节点，并且引起了叶子节点的分裂，这个时候沿途向上更新，如果沿途某个节点node未满，那么他更新后
    #不产生新的Pkey，Pref，那么在它之上的所有节点更新停止，相当于更新接受的都是none
    #更新一直向上传递，知道根节点，根节点可以产生跟新或者没有产生更新，通过判断self._put(self.root, key) 确定


    def _put(self, node, key):
        if node.hasKey(key):
            return None, None
        elif node.isLeaf():
            return self._addtoNode(node, key, None)
        else:
            child = node.getChild(key)
            pKey, pRef = self._put(child, key)
            if pKey is None:
                return None, None
            else:
                return self._addtoNode(node, pKey, pRef)


    #执行具体更新策略的函数，node为判断的节点，key为下层节点分裂产生的向上传递的pkey，而pref是下层节点分类产生的叶子节点（可能都是none）
    #然后对node进行判断
    #执行父节点满操作，这个时候根据key的范围按照三种情况进行分类，并且产生了父节点向上传递的节点pkey,与父节点的兄弟节点pref，作为返回值向上传递
    #执行父节点未满操作，根绝key的范围按照两种情况进行分析，这个时候更新完父节点node，不会产生新的分裂，因此返回值是两个node
    #https: // www.cnblogs.com / linxiyue / p / 3704794.html

    def _addtoNode(self, node, key, pRef):
        if node.isFull():
            return self._splitNode(node, key, pRef)
        else:
            if key < node.key1:
                node.key2 = node.key1
                node.key1 = key
                if pRef is not None:
                    node.right = node.middle
                    node.middle = pRef
            else:
                node.key2 = key
                if pRef is not None:
                    node.right = pRef
            return None, None

    #node为满节点，key为下层节点分裂产生的向上传递的pkey，而pref是下层节点分类产生的叶子节点（可能都是none
    #执行父节点的满分裂操作，更新父节点并且传递新产生的参数Pkey，Pref

    def _splitNode(self, node, key, pRef):
        newnode = Node(None)
        if key < node.key1:
            pKey = node.key1
            node.key1 = key
            newnode.key1 = node.key2
            if pRef is not None:
                newnode.left = node.middle
                newnode.middle = node.right
                node.middle = pRef
        elif key < node.key2:
            pKey = key
            newnode.key1 = node.key2
            if pRef is not None:
                newnode.left = pRef
                newnode.middle = node.right
        else:
            pKey = node.key2
            newnode.key1 = key
            if pRef is not None:
                newnode.left = node.right
                newnode.middle = pRef
        node.key2 = None
        return pKey, newnode




