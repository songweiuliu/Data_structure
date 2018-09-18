# coding: utf-8
# Build kinds of binary sort tree

from dictionary import assoc
from Binarytree import  Binnode
from stack_queue import Sstack

#二叉排序树就是利用二叉树的机构将字典的存储和查询功能融合树结构中，即节点上数据是字典节点，获得
#高效率的检索，O（logn）
#它满足左子树的节点小于根节点，右子树的节点大于根节点，其中左右子树也都是二叉排序树

#由于我们基于二叉树实现，因此要使用二叉树的节点类以及数据部分使用字典的数据类


#n个关键码建立的具有n个节点二叉排序树平均高度为对数关系，因此时间复杂度为对数关系，
#排列一共具有n!个因此可以产生n!个二叉排序书，每个关键码的平均检索长度也是对数关系
class DictBinTree():
    def __init__(self):
        self._root=None
    def is_empty(self):
        return self._root is None
    #在树中检索某个字典的值由关键码，已保证key的唯一性
    def search(self,key_):
        bt =self._root
        while bt is not None:
            assoc_=bt.data
            if key_<assoc_.key:
                bt=bt.left
            elif key_>assoc_.key:
                bt = bt.right
            else:
                return assoc_.value
        return None

    #插入元素，这个时候如果树中已经存在要插入的key那么分情况：
    # 1忽略该key什么都不做
    # 2将key的值替换成新值，
    # 允许重复直接插入新节点？所以应该插在那里？

    #插入之前首先要检索插入位置，只要插入的key不在树中，那么检索到的位置必定是某个叶子节点的
    #左子树或者右子树，显然左右子树都是空的，因此将新元素插入到这两个空位置之一
    def insert(self,key_,value_):
        insert_=assoc(key_,value_)
        bt=self._root
        if bt is None:
            self._root = Binnode(insert_)
            return

        while True:
            assoc_=bt.data
            if key_<assoc_.key:
                if bt.left is None:
                    bt.left=Binnode(insert_)
                    return
                bt=bt.left
            elif key_>assoc_.key:
                if bt.right is None:
                    bt.right=Binnode(insert_)
                    return
                bt = bt.right
            else:
                assoc_.value=value_
                return

    #定义一个生成树中所有字典纸的方法，按key值顺序生成,可以采用中序遍历的方法
    #采用非递归算法的中序遍历
    def iterator(self):
        s=Sstack()
        t=self._root
        while t is not None or not s.is_empty():

            while t is not None:            #对于非空的右节点，加入该子树的所有左节点（包含根节点）
                s.push(t)
                t=t.left
            t=s.pop()
            yield  (t.data.key,t.data.value)
            t=t.right

    #定义删除操作，删除操作比较复杂
    #如果被删除的是根节点直接将其父节点的引用设置为None
    #如果删除的 q没有左子树，直接将其右子树重新设置为父节点的左子树
    #如果由左子树那么将将其左子树的最右节点找到，然后将其右子树设置为该最右节点的右子树，最后与父节点链接

    def delete(self,key_):
        f,s=None,self._root

        if f is None and s is None:
            raise  ValueError

        while s is not None and s.data.key!=key_:   #不相等是才进入循环
            f=s                                     #保存父节点
            if key_<s.data.key:
                s=s.left
            elif key_>s.data.key:
                s=s.right
            if s is None:
                return                              #树中没有要删除的关键码
        #退出循环表示找到了s.data.key=key_,因为已经排除了前者的退出条件
        #没有左子树
        if s.left is None:
            if f is None:           #证明找到的要删除的顶点是根节点
                self._root=s.right
            elif s is f.left:
                f.left=s.right
            elif s is f.right:
                f.right=s.right

        #有左子树，比较麻烦，先找左子树的最右节点
        ss=s.left
        while ss.right is not None:
            ss=ss.right
        #将删除节点的右节点链接到左子树的最右节点的右节点
        ss.right=s.right

        if f is None:
            self._root=s.left
        elif s is f.left:
            f.left=s.left
        elif s is f.right:
            f.right=s.left

    def printall(self):
        for k ,v in self.iterator():
            print((k,v))

#定义一个独立函数，可以基于一系列数据项生成一个二叉排序树
def buildDictBinTree(entries):
    dic=DictBinTree()
    for k,v in entries:
        dic.insert(k,v)
    return dic


#最佳二叉排序树，满足检索路径最短，前提是假设所有的额关键之被检索概率相同，这个是怎么构建二叉树，
#其中n!个二叉排序书里面寻找检索效率最高的那个二叉树便是最佳二叉排序树，用平均检索路径来衡量
#访问到的为内部节点，还存在访问不到的值，但是肯定落在扩充二叉树的一个叶子节点上面
#E（n）=[求和pi(li+1)+求和qili`]/w,  w=求和pi+求和qi ，pi[0,n-1],qi[0,n]

#1：特殊情况的最佳平衡二叉树，即此时所有的内部节点和外部节点的访问概率相同，那么E（n）=(2IPL+3N)/2N+1

#基于一个有序序列递归建立，易知根节点存储的是中间数据，左右子树情况也是相同的
class Best_speDBT(DictBinTree):
    def __init__(self,seq_):
        DictBinTree.__init__(self)
        seq=sorted(seq_)
        self._root=Best_speDBT.recbuildnode(seq,0,len(seq)-1)
    @staticmethod
    def recbuildnode(data,start,end):
        if start>end:
            return None
        mid=(start+end)//2
        left=Best_speDBT.recbuildnode(data,start,mid-1)
        right=Best_speDBT.recbuildnode(data,mid+1,end)
        return Binnode(assoc(*data[mid]),left,right)

#2:对于更为一般的情况也就是内外顶点的访问概率不相等的情况，此时我们可以使用动态规划的思想进行
#更为一般的讨论，先求子问题的解然后由子问题的解进而引出更为高级的问题的解

#设T(i，j)表示含有pi...pi-1个内部节点和qi....qj个外部节点的最佳二叉排序书，那么这样的候选树一共由j-i个
#我们的目标就是求出其中平均检索路径最短的那一个，就是最佳二叉排序书
#使用r(i,j)存储最佳二叉排序书的根节点
#使用c(i,j)表示最佳二叉排序书T(i，j)的代价，c(i,j)=w(i,j)+ min(c(i,k)+c(k+1,j)) 找到使其最小
#的根节点Vk 那么该最佳二叉搜索树的结构便已经确定
#使用W(I,J)表示pi...pj-1和qi...qj个交叉的权值之和

#T[0,N]问题

#含有m节点的最佳二叉排序书有n-m+1个
#1T（0，1）........T(n-1,n)
#2:T（0，2）.....T(n-2,n)
#m:T（0，m）...T(n-m,n)
#n:T[o,n]
#求解出上述所有最佳二叉树的c,w,r 便可以依次往后求个更大规模的最佳树，动态规划

def Best_ordDBT(wp,wq):
    inf=float('inf')
    n=len(wp)
    if (n+1)!=len(wq):
        raise  ValueError('wp/wq length error')
    #构建n+1维三个存储信息的方阵
    num=n+1
    r=[[0 for x in range(num)]for i in range(num)]
    w=[[0 for x in range(num)] for i in range(num)]
    c=[[0 for x in range(num)] for i in range(num)]
    #基于两个权值序列wp,wq对权值段求和矩阵w进行更新
    for i in range(num):
        w[i][i]=wq[i]
        for j in range(num):
            w[i][j]=w[i][j-1]+wp[j-1]+wq[j]

    #已知对于T（i，j）含有j-i个内部节点，因此i=j这样的最佳二叉树并不存在
    #因此r,c矩阵从右上半区域的副对角线依次向右上方递推，也就是右j-i=1递增

    #对于副对角线[i][i+1]此时这样c可以直接w[i][i+1]求出，因为此时最佳二叉树没有候选情况
    #此时便是仅含有一个内部顶点的最佳二叉排序书，可以知道有n个
    for i in range(n):
        c[i][i+1]=w[i][i+1]
        r[i][i+1]=i

    #从这里开始，对于在往右上方的最佳二叉排序树每个树都右候选树了，所以要对比确定k，
    #也就是使每个T(I,J)的代价c(i,j)最小的vk，
    #对于含有m个节点的最佳二叉排序书进行确定,从2到n
    for m in range(2,n+1):
        #含有m个节点的最佳二叉排序书有n-m+1个，对应t(0,m)...t(n-m,n)
        for i in range(0,n-m+1):
            #确定每一个含有m个节点的最佳二叉排序树T[i,i+m]，通过对比取不同的k的c()值的情况
            min=inf
            #此时在T[i,i+m]候选树中内部节点k的可能取值范围为i,...i+m-1
            for k in range(i,i+m):
                ko=w[i][i+m]+c[i][k]+c[k+1][i+m]
                if ko<min:
                    min=ko
                    c[i][i+m]=ko
                    r[i][i+m]=k
    #完成上面的循环之后右上半部分所有的最佳二叉排序书都以被求出，
    #其中当m=n时，i=0，此时仅有T(O,N)一棵最佳二叉排序书也就是我们所要求的最终的树，最后一个点
    #T(O,N)有n个内部节点，因此有n个候选树，从中对比找出了最佳的根节点k，存在t(0,n)中
    return r,c






#最佳的代价就是结构容易损坏，不易维护，因此后见平衡二叉排序树AVL
#既具有比较高的检索效率,接近与o(logn)又有比较好的动态性能
#定义是所有节点的左右子树的深度相差不超过1，只能是0，1，-1，并且其左右子树也都是满足这个条件

class AVLnode(Binnode):
    def __init__(self,data):
        Binnode.__init__(self,data)
        self.bf=0

class AVL_DBT(DictBinTree):

    #默认建立空树，当然也可以赋予一个序列，然后调用本类中的insert方法进行建立
    def __init__(self):
        DictBinTree.__init__(self)

    #分析插入的情况，如果途径插入位置所有的节点BF都是0，那么插入之后也不失衡，只是需要修改途径节点的BF，
    #如果不是上面，那么一定存在一个最小的非平衡子树，插入节点可能bf》=2，
    # 如果插入后可以调整该子树，使其不再失衡并且其高度维持不变
    #（保证子树之外的不跟BF不变）那么可以重新将该树调整为AVL
    #具体分为LL,LR,RL,RR四种调整类型,其中rr/ll,lr/rl是完全对称的两种类型
    @staticmethod
    def LL(a,b):
        a.left=b.right
        b.right=a
        a.bf=b.bf=0
        return b
    @staticmethod
    def RR(a,b):
        a.right=b.left
        b.left=a
        a.bf = b.bf = 0
        return b
    @staticmethod
    #AbBcCaD,原先的根节点是a，A,D一样高，那么转换之后根节点是c，这个时候可以得出结构
    def LR(a,b):
        c=b.right
        a.left=c.right
        b.right=c.left
        c.left=b
        c.right=a
        #修改重新调整之后的BF值
        #由于新增节点插入到了c里面，因此通过判断c.bf来判断插入到了哪里
        if c.bf==0:             #插入到c.bf为0证明是插入到c节点内部
            a.bf=-1
            b.bf=1
        elif c.bf==1:           #插入到了c的左子树也就是B上面
            a.bf=-1
            b.bf=0
        else:                   #插入到了右子树C上面
            b.bf=1
            a.bf=0
        c.bf=0
        return c

    @staticmethod
    # AbBcCaD,原先的根节点是a，A,D一样高，那么转换之后根节点是c，这个时候可以得出结构
    def RL(a, b):
        c = b.left
        a.right = c.left
        b.left = c.right
        c.left = a
        c.right = b
        # 修改重新调整之后的BF值
        # 由于新增节点插入到了c里面，因此通过判断c.bf来判断插入到了哪里
        if c.bf == 0:  # 插入到c.bf为0证明是插入到c节点内部
            a.bf = 1
            b.bf = -1
        elif c.bf == 1:  # 插入到了c的左子树也就是B上面
            a.bf =0
            b.bf =-1
        else:  # 插入到了右子树C上面
            b.bf = 0
            a.bf = 1
        c.bf = 0
        return c

    #查找新节点的插入位置，在这个过程中记录遇到最小不平衡术的根
        #1距离插入位置距离最近的平衡银子非0的点，有可能需要修改这种子树，用pa记录它的父节点
        #不存在的考虑a就是树根
        #插入插入失衡，那么a就是失衡位置
        #实际插入新节点
    #插入后修改从a的子节点到新节点路径上所有节点的BF值
        #由于a的定义，这段路径上面原先都是BF=0
        #插入后用一个扫描变量从a的子节点开始遍历，如果插入在左子树就改成1，右子树改成-1
    #检查以a的子树是否失衡，失衡是做出调整：
        #如果a.bf=0不会失衡，简单修改平衡因子并结束
        #如果a.bf=1，那么此时插入左子树时会失衡 进行LL,LR调整
        #如果a.bf=-1，那么此时插入右子树失衡，进行rr,rl调整


    def insert(self,key_,value_):
        p=self._root
        a=self._root
        if a is None:
            self._root=AVLnode(assoc(key_,value_))
        #记录其父节点q是p的父节点
        q=None
        pa=None
        while p is not None:
            if key_ ==p.data.key:           #检索已经存在时直接进行赋值
                p.data.value=value_
                return
            if p.bf!=0:                     #最小的非平衡二叉子树也是插入位置
                pa=q
                a=p
            q=p                             #将自己赋给父节点指针

            if key_<p.data.key:
                p=p.left
            else:
                p=p.right                   #退出循环的一个条件也有可能是没有找到非平衡子树，
                                            #而是已经搜索到了末端

        #退出上面的循环，代表pa已经指向最小非平衡子树的根节点的父节点,a是根节点,并且此时q是插入点的父节点
        node=AVLnode(assoc(key_,value_))
        if key_ < q.data.key:
            q.left=node
        else:
            q.right=node

        #新节点已经插入，更新路径上顶点的bf,a是最小不平衡子树
        if key_<a.data.key:         #插入了a的左子树
            b=a.left
            p=a.left                #重新定义p便于沿途修改
            d=1                     #代表左子树
        else:
            b=a.right
            p=a.right                #重新定义p便于沿途修改
            d=-1                     #代表右子树

        #沿着a的插入新节点所经过的路径修改沿途节点的bf值
        while p!=node:
            if key_<p.data.key:
                p.bf=1
                p=p.left
            else:
                p.bf=-1
                p=p.right

        #上面已经完成了插入还有修改BF，下面进行调整
        if a.bf==0:                 #原先a就是平衡子树，那么插入之后不会失衡
            a.bf=d
            return
        if a.bf==-d:                #插入短的子树，因此此时平衡
            a.bf=0
            return

        #新节点在高子树里面，必须调整
        if d==1:
            if b.bf==1:             #说明插入的是左子树的左子树LL
                b=AVL_DBT.LL(a,b)
            else:
                b = AVL_DBT.LR(a, b)

        else:
            if b.bf==-1:             #说明插入的是右子树的右子树RR
                b=AVL_DBT.RR(a,b)
            else:
                b = AVL_DBT.RL(a, b)

        if pa is None:
            self._root=b              #调整以后返回的都是根节点
        else:
            if pa.left==a:             #原先的最小非平衡子树是父节点pa的左子树
                pa.left=b
            else:
                pa.right=b










