# coding: utf-8
# Build a AOE/AOV

from Graph import graph,graph_AI



#AOV网络便是所谓的顶点活动图，可以把AOV网络里面的有向边看作一种顺序关系。拓扑排序就是问，在一个AOV网络里面的
#的活动能否排成一个全序
#对于给定的AOV网络N，如果N中所有的顶点能拍成一个线性序列S=vi0,vi1,vi2......vin-1
#满足：如果N中存在从顶点vi到顶点vj的路径，那么S里VI就排在VJ之前，则S成为N的一个拓扑序列，构造拓扑序列的
#过程成为拓扑排序

#存在拓扑序列的前提是网络里面不存在回路，拓扑序列未必唯一，而且拓扑序列的逆序，就是N的逆网，即所有的边反向
#时间复杂度O（E+V）或者O（V2）
def toposort(graph):

    vnum=graph.get_num()                                    #取顶点数值
    indegree,toposeq=[0]*vnum,[]                            #建立入度表，其中度为0的顶点串成一串，拓扑序列表，初始为空表
    zerov=-1                                                #第一个入也是相当于栈底入度为0的顶点的元素，代表往下没有入度为0的顶点了，它是第一个
    for vi in range(vnum):
        for j ,w in graph.out_edge(vi):                     #遍历所有顶点的临接边，然后做出所有顶点的入度表
            if w !=0:                                       #该条件排除对角线上自身为入度的干扰
                indegree[j]+=1
    for vi in range(vnum):                                  #找到入度为0的顶点，然后将他们串成串，具体的是：第一个入度为0的点元素为-1，栈底，更新zerov
        if indegree[vi]==0:                                 #第二个入度为0的点的元素是上一个的顶点的序号zerov，循环。因此最后出现的为0的顶点为栈顶
            indegree[vi]=zerov                              #此时zerov指向该顶点的序号，然后每个indegree[vi]的元素都是下一个入度为0的顶点的序号
            zerov=vi

    for n in range(vnum):                                   #主循环
        if zerov==-1:                                       #没有入度为0的顶点，即zerov没有更新，那么不存在拓扑排序
            return  False
        vi=zerov                                            #保存zerov，即第一个入度为0的顶点
        zerov=indegree[zerov]                               #第一个入度为0的顶点出栈（从图中取下，加入拓扑序），此时栈顶应该指向下一个入度为0的顶点的序号indegree[zerov]
        toposeq.append(vi)                                  #将弹出的第一个入度为0的顶点加入拓扑序
        for v,w in graph.out_edge(vi):                      #由于将顶点弹出，那么与该顶点相连的所有临接顶点的入度都要减一（新图）
            indegree[v]-=1
            if indegree[v]==0:                              #更新入度表后，可能出现新的入度为0的点，此时要加入栈，具体是将indegree[v]=zerov，即新点v的元素指向下一个
                indegree[v]=zerov                           #入度为0的点，也就是老的zerov，然后再更新zerov=v，更新栈顶，继续重复上述过程
                zerov=v

                                                           #随着顶点不断从入读表中弹出，不断产生新的入度为0的点，进而不断弹出入度为0的元素，当弹出vnum个时，得到排序
    return toposeq



#关于AOE网络
#节点表示事件，节点与节点直接临接边ai:w，表示活动ai，以及ai持续的时间w（vi,vj），由这样的节点和边构成的网络称之为AOE网
#AOE网络的关键路径：AOE网络的事件之间存在这约束性的发生顺序，也就是一个事件的开始已经是以它的始点为终点的事件的结束，同一个
#始点的活动可以同时进行，因此整个网络所代表的活动进行完的最短事件其实就是该网络中最长的路径所表示的事件，这条路径称之为关键路径
#关键路径：很明显沿着关键路径进行完整个网络其他节点的活动肯定已经都结束。关键路径是指由那些ee[k]与len[k]相同的关键活动组成的路径

#终点在于求针对与每个节点的e[],与l[]
#ee[0]=0, ee[j]=max{ee[i]+w(vi,vj)}
#le[n-1]=ee[n-1],le[i]=min{len[j]-w(vi,vj)}
#然后找出ee[k]=le[k]的点
#根据这个写出以下程序

#1:生成该网络的一个拓扑序列
#2：生成ee的表，应该按照拓扑序列的顺序计算
#3：生成le的表，应该按照拓扑序列的逆序计算
#4：数据的e和l可以一起计算


def critical_paths(graph):

    def ee_time(graph,toposeq):
        vnum=graph.get_num()
        ee=[0]*vnum                             #初始化各事件最早发生事件为0
        for i in toposeq:                       #按照拓扑序列的事件顺序遍历事件
            for j,w in graph.out_edge(i):       #以每个事件寻找其临接事件，然后更新临接事件的最早发生事件
                if ee[j]<(ee[i]+w):             #一个事件可能被多此找到，因此寻找最大的那个最早发生事件
                    ee[j]=ee[i]+w
        return ee

    def le_time(graph,toposeq,ealast):
        vnum=graph.get_num()
        le=[ealast]*vnum
        for k in range(vnum-2,-1,-1):           #显然寻找最迟发生事件需要逆拓扑排序寻找，vnum-1最后一个的le是确定的
            i=toposeq[k]
            for j ,w in graph.out_edge(i):      #找到事件i的临接事件，对其最迟发生时间更新
                if (le[j]-w)<le[i]:             #如果计算出的最迟发生时间le[i]-w，比原先的更小，那么更新它
                    le[i]=le[j]-w
        return le

    #ee,le中的顺序都是代表拓扑排序的顶点（事件）的顺序
    def crt_path(graph,ee,le):              #根据ee,le和graph来寻找关键活动序列
        vnum=graph.get_num()
        crt_ac=[]
        for i in range(vnum):
            for j ,w in graph.out_edge(i):  #不能直接对比ee,le，因此这样只能得到关键活动，没办法得到关键路径
                if ee[i]==(le[j]-w):        #得到关键路径,遍历时间，对于时间i，它的临接时间j被遍历,如果满足
                                            #ee[i]=le[j]-w  le[i]
                    crt_ac.append(((i,j),(ee[i],le[i])))          #输出的是vi,vj时间之间的活动集合，同时加上（ee[i],le[i]）检验一下

        return crt_ac,ee,le


    toposeq=toposort(graph)
    #print(toposeq)
    if not toposeq:                 #由于不存在入度为0的点，因此graph不存在拓扑序列
        return False
    ee=ee_time(graph,toposeq)
    le=le_time(graph,toposeq,ee[graph.get_num()-1])
    return crt_path(graph,ee,le)



if __name__=='__main__':
#先把图7.15用临接矩阵的形式表现出来
    inf=float('inf')
    G715=[
        [inf,7,13,8,inf,inf,inf,inf,inf],
        [inf,inf,4,inf,inf,14,inf,inf,inf],
        [inf,inf,inf,inf,5,inf,8,12,inf],
        [inf,inf,inf,inf,13,inf,inf,10,inf],
        [inf,inf,inf,inf,inf,7,3,inf,inf],
        [inf,inf,inf,inf,inf,inf,inf,inf,5],
        [inf,inf,inf,inf,inf,inf,inf,inf,7],
        [inf,inf,inf,inf,inf,inf,inf,inf,8],
        [inf,inf,inf,inf,inf,inf,inf,inf,inf]

        ]
    g715=graph(G715,inf)
    tps=toposort(g715)
    print(tps)              #正确，注意此时加入邻接矩阵的时候对角线元素不能再用0表示，即本身不是本身的临接边
    print(' ')

    #验证AOV网络的关键路径是什么，以及关键路径上面的关键活动
    aoe_path,ee,le=critical_paths(g715)

    print(ee)
    print(' ')
    print(le)

    print(' ')
    print(aoe_path)
    print(' ')