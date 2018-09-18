# coding: utf-8
# Build a dictionary


#字典是基于关键码的数据检索和存储结构，分为静态字典和动态字典
#静态字典：在建立之后内容不再变化，也就是没有变动操作，这个主要考虑吧检索效率
#动态字典：建立之后将处于一系列的动态变化之中，对于这种字典，除了要考虑检索修效率还要考虑变动效率


#包含关键码和数据基本字典节点单元,同时为了方便排序，要具有比较性质

class assoc():

    def __init__(self,key_,value_):
        self.key=key_
        self.value=value_
    def __le__(self, other):
        return self.key<=other.key
    def __lt__(self, other):
        return self.key<other.key
    def __ge__(self, other):
        return self.key>=other.key
    def __gt__(self, other):
        return self.key>other.key


#定义一个字典类，首先基于顺序表(线性表)实现
#首先基于无序顺序表实现
class dict_list():

    def __init__(self):
        self._elems=[]

    def is_empty(self):
        return not self._elems

    #这里的插入是不按顺序插入，并且不追求key的值的唯一性
    def insert(self,assoc_):
        self._elems.append(assoc_)

    #将所有的key的字典项全部都删除
    def delete(self,key):
        for a in self._elems:
            if a.key==key:
                self._elems.pop(a)

    #修改所有K的字典项的值为v
    def change(self,key_,new_):
        counter=0
        for i in range(len(self._elems)):
            if self._elems[i].key==key_:
                self._elems[i].value=new_
                counter+=1
        if counter==0:
            raise ValueError
    #利用迭代器定义一个查找函数
    def search(self,key):
        for a in self._elems:
            if a.key==key:
                yield a.value

#基于有序顺序表实现，这个时候可以根据二分法进行检索，实际上是利用了二叉树的性质

class dict_ordlist(dict_list):
    def __init__(self):
        dict_list.__init__(self)


    #基于二分法的检索函数
    def search(self,key_):
        i,j=0,len(self._elems)-1
        while i<=j:
            mid=i+(j-i)//2
            midkey=self._elems[mid].key
            if key_<midkey:
                j=mid-1
            elif key_>midkey:
                i=mid+1
            else:
                return mid,self._elems[mid].value
        #查找的key不存在
        return None

    #这个时候要进行按key值大小的顺序插入，类似与优先序列的list的实现，其实本质是一样的
    #由于list中是按从小到大排列的，而优先序列中是按从大到小排列的因此两者比较符号相反就可以了
    #记住正向遍历和反向遍历，插入位置和遍历指针的关系是不同的，反向遍历要加1，插入那里那段开始集体后移

    #python的list类型是基于线性表的顺序表的分离式结构建立的动态顺序表，它的变动操作都是保序的,
    #也就是说插入，删除操作都是去掉元素之后再移动元素
    #非保序插入：将插入位置的原元素移动尾端然后将元素插入
    #保序插入：将元素直接插入到指定位置，然后指定位置及以后的元素一次向后平移一个单位
    #非保序删除：将指定位置的元素删除，然后将尾端元素插入
    #保序删除：将指定位置的元素删除，然后将该位置及以后的元素向前平移
    #保序插入
    def insert(self,assoc_):
        num=len(self._elems)
        #检验要插入的key的唯一性
        counter=0
        for a in self._elems:
            if a.key==assoc_.key:
                counter+=1
        if counter!=0:
            raise ValueError('Key has alrealy exist')
        i=0
        while i<num:
            if assoc_.key>self._elems[i].key:
                i+=1
            else:
                break
        self._elems.insert(i,assoc_)

    #先检索后删除，考虑了删除元素不存在的情况
    def delete(self,key_):
        i,j=0,len(self._elems)-1
        while i<=j:
            mid=i+(j-i)//2
            midkey=self._elems[mid].key
            if key_<midkey:
                j=mid-1
            elif key_>midkey:
                i=mid+1
            else:
                self._elems.pop(self._elems[mid])
                return
        raise ValueError('No key and can`t delete it ')
    #先检索后修改
    def change(self,key_,new_):
        mid,value=self.search(key_)
        self._elems[mid].value=new_



#线性表存在很多的局限性，因此因此为了支持高效率的检索和修改人们提出两种解决方案：
#1：基于散列思想的散列表，也成为哈希表
#2：基于各种树形结构的数据村粗和检索技术

#散列表的思想，选定一个整数的下标范围，通常以0或者1开始，建立一个包含相应位置元素的顺序表
#选定一个从实际关键码key到选定元素范围index的适当映射函数h，成为哈希函数，它要满足对于不同的key值具有不同的
#的h值，或者说尽量满足，因为是由于是从大集合到小集合的映射，所以肯定存在冲突。

#h函数的设计方法，最常用的适用于证书的数字分析法，折叠法，
# 具有通用性的方法是除余法（整数）还有基数转换法（证书或者字符串）

#解决冲突的方法：内消解技术和外消解技术
#内消解技术：开地址技术，即如果h(key)已经存有元素，那么便H=H+di，如果di是0，1，2.....称为
#线性探查技术，如果为i*h2(key)成为双散列探查，然后找到下一个空位加入到表中，这样一次进行加入
#比较坏的一种情况就是h的映射值比较集中，那么此时几乎加入每个元素都需要探查，效率非常低，甚至达到线性时间


#检索和删除，同样是有h（key）位置去对比，找到目标元素进行操作，不过此时删除时要加入一个特别的元素，使其
#对检索非空，对插入为空，由此可见多此删除之后又大量空位效率降低

#外消解技术：建立一个外部的区域专门存储发生冲突的元素序列，检索时若果关键码不匹配直接转到溢出区检索，但是
#当溢出区比较长时会发现其效率降低
#桶散列技术：数据项不放在散列表的基础存储区域中，而是存在的一个链表的索引，因此h(key)可以一次存在到该位置
#的链表之中，但是如果大量使用之后链表长度变长，效率也会变低。此时负载因子可以是任意值，平均桶长代替。

#python 字典dic和集合set都是集合散列表实现的

#集合的实现，要具有求交并集等一些基础的运算性质

#简单线性表实现，检索是否存在o(n)，结合于是暖O（m*n）效率低
#排序顺序表，如果两个结合s,t都是排序顺序表，那么此时的检索，还有集合运算效率就会大大提高
#m+n,插入式要维护顺序此时为O(N)，检索是O（logn）
def AND(s,t):
    r=[]
    i=0
    j=0
    while i<len(s)and j<len(t):
        if s[i]<t[j]:
            i+=1
        elif t[j]<s[i]:
            j+=1
        else:
            r.append(s[i])
            i += 1
            j += 1




















