# coding: utf-8
# show kinds of  sort algorithm






#定义排序目标类，包括关键码和其他相关信息，排序的作用目标是关键码
class record():
    def __init__(self,key_,datnum_):
        self.key=key_
        self.datnum=datnum_


#                1简单排序算法


#1.1插入排序：
#顾名思义不断地把一个元素插入已经排好序的一个序列当中，为了降低空间复杂度把正在构造的排序序列
#嵌入到原来的表中。考虑表中第i个元素,i的左边都是已经排好的序列，i的右边包括它本身都是未排序序列，然后
#向前比较i的元素选择到合适的位置插入i的值，这个时候i值保留后的位置相当于一个空位，然后将大于i的都向后平移
#时间复杂度O（n2），空间复杂度O（n）

def insert_sort(list_):
    le=len(list_)
    for i in range(1,le):
        sortnum=list_[i]
        j=i
        while j > 0 and list_[j-1].key>sortnum.key:
            list_[j]=list_[j-1]
            j-=1
        list_[j]=sortnum

#1.2选择排序
#维护已经排序号的序列，然后从未排序序列中找到最小的一个元素，然后插入到前面已排序序列的最后的位置
#重复上面的过程，直到未被排序的序列个数为1时，就能找到整个排序序列,为了降低空间复杂度，这里也是采用
#嵌入的方法，将最小的元素和未被考虑的序列的第一个元素互换，然后将已排序序列的长度加1
def choice_sort(list_):

    le=len(list_)
    i=0

    while i <le-1:                            #保证循环n次，完成全部的选择排序
        k=i
        ki=list_[i]
        for j in range(i,le):               #寻找i以及之后的未排序序列的最小元素值然后加入到i的位置，之后i+1
            if list_[j].key<ki.key:
                k=j
        if k != i :
            list[i],list[k]=list[k],list[i] #确保稳定性
        i+=1


#堆排序：前面已经实现了堆排序技术，整个堆排序技术的时间复杂度nlogn而且堆排序是一种原为排序算法，但是其稳定性存在问题
#前面已经实现


#1.3交换排序

#起泡排序：是一种典型的通过遍历交换元素进而消除逆序实现排序排序的方法，其基本操作是比较相邻记录，发现逆序对的时候就
#交换它们，通过反复的比较和交换就能达到整个序列的排序工作。
#一次排序能够保证将最大的元素移动到最后但是只能使最小的元素左移动一位

def bubble_sort(lst_):
    le=len(lst_)
    for i in range(le-1):
        mark=False
        for j in range(1,le-i):
            if lst_[j-1].key>lst_[j].key:
                lst_[j],lst_[j-1]=lst_[j-1],lst_[j]
                mark=True
        if not mark:
            break
#改进，当某一次遍历排序发现在整个排序过程中都没有出现逆序时说明已经完全排序，可以提前结束
#交错起泡的方法：左到右遍历可以快速的将最大元素移到右端，最小元素仅左移一位，而右到左排序可以快速将最小元素一道左端

def exbubble_sort(lst_):
    le=len(lst_)

    gi=0
    bi=0

    while (1+bi) < (le-gi):

        for j in range(1+bi,le-gi):                     #正向起泡，开始点为1+bi，与反向冒泡次数有关，反向冒泡为0时
            if lst_[j - 1].key > lst_[j].key:           #对应从1开始向后起泡（考察了0），反向冒泡为几说明前面几个已经为最小不需要考虑
                lst_[j], lst_[j - 1] = lst_[j - 1], lst_[j] #截至点与正向冒泡次数有关，gi为几说明后面几个已经为最大，不需要考虑
        gi += 1

        for j in range(le-1-gi,0+bi):                   #反向起泡，开始点与正向起泡次数有关，正向为几说明倒数几个已经排列不需要考虑
            if lst_[j]<lst_[j-1]:                       #截至点与反向冒泡次数有关，本来应该到0（实际取到1可以考虑吧全部），但是反向为几
                lst_[j], lst_[j - 1] = lst_[j - 1], lst_[j] #说明前面几个已经全排序不需要考虑
        bi += 1

#                       2快速排序算法

#所谓快速排序是指按照某种标准将考虑的记录分为“大记录”和“小记录”，并通过不断的递归不断的划分，最终得到一个排序序列
#快速排序的表实现，在表的内部实现划分，其中取出序列中的第一个记录然后将其关键码作为标准划分其他的记录，把关键码的小的记录移到左边
#关键码打的记录移到右边，这样最后剩余的一个空位就是最终的准确的 比较标准关键码 的最终位置，然后将左右两部分再进行相同操作
#算法的时间复杂度平均而言是nlogn 但是如果递归的一方一直是空也就是比如一已经是升序或者降序序列那么回到n2，常见的快速排序算法都是不稳定的
#而且也不具有适应性


def Qucik_sort(lst_):
    sort_rec(lst_,0,len(lst_)-1)

def sort_rec(lst,l,r):
    if l >=r :
        return
    i,j=l,r
    k=lst[l]

    while i <j :
        while j >i:
            if lst[j].key>=k.key:
                j-=1
            else:
                break
        if j !=i :
            lst[i]=lst[j]
            i+=1
        while j >i :
            if lst[i].key<=k.key:
                i+=1
            else:
                break
        if i !=j :
            lst[j]=lst[i]
            j-=1

    lst[i]=k
    sort_rec(lst,l,i-1)
    sort_rec(lst,i+1,r)


#另外一种简单的实现，这个时候分为小记录，打记录，还有未分类记录，i是最后一个小于k的值的记录元素小标
#j是第一个未分类元素小标

#如果j大于k将j直接加1
#如果j对应的元素小于k,那么此时将j处的元素与i+1处的元素或者说大记录的第一个元素进行交换，那么此时再将j加一
#i+1，仍然很好地维护了小记录和大记录，交换完成之后需要做的事情就是将标准k与i上面的元素交换位置，那么此时k所处的
#位置便是合理的正确的位置

def simple_Qucik_sort(lst):

    def simple_sort_rec(lst,begin,end):
        if begin>=end:
            return
        k=lst[begin]
        i=begin
        for j in range(begin+1,end+1):              #如果j大于k将j直接加1
            if lst[j]<k.key:                        #如果j对应的元素小于k,那么此时将j处的元素与i+1处的元素或者说大记录的第一个元素
                                                    # 进行交换，i+1，仍然很好地维护了小记录和大记录
                i+=1
                lst[i],lst[j]=lst[j],lst[i]

        lst[i],lst[begin]=lst[begin],lst[i]

        simple_sort_rec(lst,begin,i-1)
        simple_sort_rec(lst,i+1,end)

    simple_sort_rec(lst, 0, len(lst) - 1)


#           4 归并排序

#归并排序的方式初始时将n个子序列当成是n个有序序列
#两两归并两个子序列中元素，形成一个更长的序列，这样的遍历一遍，序列树减半但是长度增加一倍
#对于加长的有序子序列重复上诉过程，最终得到一个完成的长度为n的有序序列
#这种方法称之为简单二路归并排序，同时存在三路归并排序还有更多路的归并排序。



#三层设计
#最里层要完成两个子序列的归并排序操作，合成一个大的有序序列
#基于上面的操作将新的有序子序列存入新的顺序表的同样的位置，同时堆整个有序子序列堆进行遍历存入各对结果
#在两个顺序表之间重复执行操作2，完成一遍归并之后交换两个表的位置，然后再重复操作2，直到整个表里只有一个有序序列是完成
#事件复杂度o(nlogn)，空间复杂度为n


#最内层    对两个最小的子序列进行合并排序
def merge(lfrom,lto,low,mid,high):

    i,j,dr=low,mid,low
    while i <mid and j <high:               #对两个子序列进行归并排序，形成一个新的序列
        if lfrom[i].key<lfrom[j].key:       #当至少一个子序列都被排序完之后退出循环
            lto[dr]=lfrom[i]
            i+=1
        else:
            lto[dr]=lfrom[j]
            j+=1
        dr+=1

    if i <mid:                              #复制第一段的剩余记录
        for i in range(i,mid):
            lto[dr]=lfrom[i]
            dr+=1
    elif j<high :                           #复制第二段剩余的记录，这两个事件只可能发生一个
        for j in range(j,high):             #因此也可以写成两个循环的形式
            lto[dr]=lfrom[j]
            dr+=1

#中间层     对所有的两两子序列进行最内层的操作，还要考虑不能完全成对的剩余情况
def mergr_across(lfrom,lto,llen,slen):

    s=0
    while s+2*slen <llen:                       #对所有的两两子序列依次进行最内层的操作
        merge(lfrom,lto,s,s+slen,s+2*slen)      #上面的循环退出后可能存在未排序的一个或两个序列
        s=s+2*slen


    if s+slen <llen:                            #存在两个完成的未合并的子序列，后一个的长度可能小于slen
        merge(lfrom, lto, s, s + slen, llen)

    else:                                       #只存在一个未排序子序列，此时将该子序列直接放入lto中
        for i in range(s,llen):
            lto[i]=lfrom[i]

#最外层     对形成的新的更加长的子序列对重新重复上面中间层的操作

def merge_sort(lst):
    slen,llen=1,len(lst)
    templst=[None]*llen
    while slen<llen:                            #子序列长度等于列表长度时代表全体排序完成，仅有一个子序列
        mergr_across(lst,templst,llen,slen)     #进行从lfrom到lto的子序列合并
        slen=slen*2                             #子序列长度翻倍
        mergr_across(templst,lst,llen,slen)     #进行从lto到lfrom的子序列合并
        slen=slen*2                             #子序列长度翻倍






#                     5 其他的一些排序方法

#多轮分配和排序


#如果关键码只有很少几个不同的值，存在一种简单而且直观的排序方法：
#为每一个关键码设置一个桶，（参考桶散列的实现）
#排序时简单地根据关键码将记录放入相应的桶之中
#存在所有的记录之后，顺序的收集各个桶中的记录，就得到了排序的序列

#但是如果存在很多不相同的关键码，采用分配排序就需要建立大量的桶，但是在实际排序中绝大部分的桶都是空的，
# 这显然不是适合分配的场景

#人们提出了一种扩展它的能力的方法，就是采用元素适合分配排序的元组作为关键码，通过多伦分配和收集完成
# 以这种元组作为关键码的记录的排序工作
#存在最高位优先和最低维优先方法，采用后者是最方便的方法

#需要排序的仍然是record类型的顺序表，也就是python的list
#需要排序的记录中的关键码是十进制数的元组，即包含r个元素（进制）
#排序算法的参数是表lst还有关键码元组长度r


#最终出桶形成的lst就是里面的元素已经按照其关键码（yuanzu）进行排序之后的结果
def radix_sort(lst,r,d):
    rlist=[[]for i in range(r)]
    llen=len(lst)
    for m in range(-1,-d-1,-1):                             #依次循环完成依次入桶分配和出桶排序，对关键码的所有位倒数遍历，
        for j in range(llen):                               #将所有的元素入m处的桶
            rlist[lst[j].key[m]].append(lst[j])
        j=0                                                 #依次入桶之后j复位,便于下面的出桶恢复操作

                                                            #顺序处理本次入桶排序的元素，按元素的排列或者桶的顺序
        for i in range(r):
            temp=rlist[i]                                   #某一个桶中的元素全部顺序出桶
            for k in range(len(temp)):
                lst[j]=temp[k]
                j+=1
            rlist[i].clear()

    return lst



#          Python里面的list是蒂姆排序

