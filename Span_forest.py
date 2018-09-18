# coding: utf-8
# Build a span forest and min span forest

from Graph import graph,graph_AI
from priqueue_heap import Prique_heap,Prique_list

#构造生成树
#生成树的概念：对于连通无向图以及有根有向图存在包含n-1条边的集合，这个集合包含了vo到其他所有顶点的路径
#Q1：包含n个节点的图的，它的生成树包含n-1条边，对于无向图是它的最小连通图，
# 对于有向图是它的生成树都位于根节点到其他节点的路径上面
#Q2：对于含有n个节点的图，含有m个联通分量，那么它的生成树含有n-m条边

#遍历中经过的边加上原图所有的定点就构成了改图的一个生成树，生成树并不是唯一的，因此分DFS,BFS
#基于递归深度优先搜索构建生成树
#使用DFS_seq记录生成树，记录的格式对应下标的定点的元素是（前一个点，边的权值）
#首先使用一个主循环，来控制从哪一个点作为生成树的起点（选择起点，因为可能某个起点不通，对于有向图）

#从起点进入生成树后，开始进入递归寻找的步骤
def span_forest(graph):
    vnum=graph.get_num()
    DFS_seq = [None] * vnum
    #递归主体
    def clfs(graph,v):
        nonlocal DFS_seq
        for u,w in graph.out_edge(v):   #遍历节点v的所有的临接边
            if DFS_seq[u] is None:      #寻找生成树不包含的临接顶点
                DFS_seq[u]=(v,w)        #将u加入到生成树的点集合中
                clfs(graph,u)           #然后以u作为下次递归的起点，寻找u的临接点，找到没有包含
                                        #在生成树中的临接点，然后将其加入生成树，依次递归。
    #选择生成树的起点，因为有可能某个起点并不是根
    for  i in range(vnum):
        if DFS_seq[i] is None:
            DFS_seq[i] =(i,0)
            clfs(graph,i)
    #检查是否有孤立点，即加入了两个起点其将所有的点检索完毕
    counter=0
    for x in DFS_seq:
       if x[1]==0:
           counter+=1
    if counter >1:
        raise ValueError('There is a islanddot')
    return DFS_seq

#由于生成树不是唯一的，由上面的递归也能看出来
#因此我们常常希望寻找最小生成树，所谓的最小的生成树，是指生成树的权值之和最小
#有以下几种办法

            #    Kruskal 方法
#基于初始包含n个连通图的表，将所有的边按权值排序，然后不断往里面加入便使连通图数量减小
# （边的顶点在不同连通图），这样得到最终的最小生成图
#时间复杂度O（max（V2,ElogE））,空间复杂度O（E）

def K_MST(graph):
    vnum=graph.get_num()
    reps=[i for i in range(vnum)]             #建立一个指示表，看表示不同的顶点是否在一个连通图
    edges=[]
    for i in range(vnum):               #构建包含所有边的表
        for j,w in graph.out_edge(i):
            edges.append((w,i,j))
    edges.sort()                        #将按从小大的顺序排列
    mst=[]                              #记录最小生成图边的表,完成时应该包含n-1条边
    #counter=0                          #计数值,当计数到n-1时退出，证明已经得到最小生成树

    for w,vi,vj, in edges:
        if reps[vi] != reps[vj]:        #新加入的最小边有效的前提是端点不再一个连同图内
            mst.append(((vi,vj),w))
            #counter+=1
            if len(mst)==vnum-1:
                break
            rep,orep=reps[vi],reps[vj]     #更新维护指示表，使新加入的边的端点在一个连通图内
            for x in range(len(reps)):
                if reps[x]==orep:
                    reps[x]=rep

    return mst



                #    Prim 方法
#维护两个点集U，V-U，前者是目前生成树包含的点集，后者是未包含的点集，寻找e=(u,v)u属于前者，v属于后者
#然后e是满足这样条件的最小的边，那么最小生成树G中一定含有边e

#它的核心思想就是通过不断的寻找满足这样条件的e，加入，然后扩充生成树点击U,最终使其包含所有的节点
#进而得到最小生成树

#时间复杂度O(ElogE),空间复杂度O（E）
def P_MST(graph):
    vnum=graph.get_num()
    mst=[None]*vnum                         #建立一个最小生成树的路径表，同时也充当表示最小生成树
                                            #已包含的顶点的作用，比如第i个元素的值不是none代表最小生成树
                                            #包含第i个顶点
    cands=Prique_heap([(0,0,0)])            #初始时将初始点的父节点（它本身）表示的临接边加入优先序列
    counter=0                               #计数值
    while counter<vnum and not cands.is_empty():
        w,vi,vj=cands.dequeue()             #从优先序列中取出权值最小的临接边（一个点在U，一个点在V-U）
        if mst[vj] is not None:             #这个临接边不满足条件vj在V-U中，也是就是一个点在生成树集之外
            continue                        #跳过这条边
        mst[vj]=((vi,vj),w)                 #将满足条件的边加入到路径表，同时也表示第vj个顶点已经加入到生成树集
        counter+=1
        for j,w in graph.out_edge(vj):      #将新加入的vj的满足条件的临接边（终点在V-U之外）加入到优先队列
                                            #此时队列中包含V-U中的顶点的所有的还未弹出的临接边（继续找最小的）
            if mst[j] is None:
                cands.enqueue((w,vj,j))
    return mst


#最短路径问题，路径长度指的是两个顶点之间的最短路径的权值之和
#1：从一个顶点出发，到其他所有节点的最短路径
#2：求图中任意两个节点之间的最短路径
#如果v`是v0到v最短路径上面p上面v的前一个顶点，那么v0到v`也是属于最短路径长度。

#求解单源点vo，到其他所有节点的最短路径的Dijkstra算法

#在集合U中放入顶点vo，vo到vo的距离为0
#对于V-U中的每个顶点v，如果（v0,v）存在，那么vo到v的最短路径长度就是直接边w(v0,v)，否则就令v的已知最短距离为无穷，
#反复做：
#从v-u中找出已知最短路径最短的点，加入到U中，由于vmin的加入更新它的临接顶点（V-U中的）的最短路径长度（如果更小的话）
#时间复杂度O(ElogE),空间复杂度O（E）


def Dij_min_spanforest(graph,vo_):
    vnum=graph.get_num()                            #记录长度
    paths=[None]*vnum                               #轨迹记录表，同时按是不是None来区分该顶点在不在U中
    cands=Prique_heap([(0,vo_,vo_)])                #记录V-U中顶点的最短路径的优先序列，只有U中顶点的临接点在其中，不在的长度为无穷
    counter=0                                       #计数器
    while counter<vnum and not cands.is_empty():
        lens,u,v=cands.dequeue()                    #弹出最短路径最短的一个临接顶点，即vmin=v
        if paths[v] is not None:                    #如该定点在U中不满足条件，跳过
            continue
        paths[v]=(u,lens)                           #满足条件，记录该顶点，加入U，格式是上一顶点再加上路径长度
        counter+=1
        for j,w in graph.out_edge(v):               #由于vmin的加入，vmin的临接顶点的最短路径可能会发生变化，进行更新。
            if paths[j] is None:
                cands.enqueue((lens+w,v,j))         #更新加入vmin的不再U中的临接顶点及其最短路径
    return paths                                    #返回得到的路径表



#求解任意顶点间最短距离的Floyd算法

def all_shaort_paths(graph):
    vnum=graph.get_num()
    a=[[graph.get_edge(i,j)for j in range(vnum)]for i in range(vnum)]   #复制原图的权重表
    path=[[-1 if a[i][j]==inf else j for j in range(vnum)]
          for i in range(vnum)] #创建轨迹表
                                #其元素path[i][j]表示vi到vj路径上面的下一个点

    for k in range(vnum):
        for i in range(vnum):
            for j in range(vnum):
                if a[i][j]>a[i][k]+a[k][j]:
                    a[i][j]=a[i][k] + a[k][j]
                    path[i][j]=path[i][k]       #运用了性质vi到v的最短路径的v的前一个点v·,
                                                # 那么vi到v`也是最短路径，那么下一个顶点都是相同的
    return (a,path)






if __name__=='__main__':
    #定义一个无穷数
    inf=float('inf')
    #定义有向图G7
    G7=[
        [0,inf,6,3,inf,inf,inf],
        [11,0,4,inf,inf,7,inf],
        [inf,3,0,inf,5,inf,inf],
        [inf,inf,inf,0,5,inf,inf],
        [inf,inf,inf,inf,0,inf,9],
        [inf,inf,inf,inf,inf,0,10],
        [inf,inf,inf,inf,inf,inf,0]
        ]
    g7=graph(G7,inf)
    #测试导入
    # print(g7._mat)
    # for x in range(g7._vnum):
    #     print(g7.out_edge(x),end=' ')
    # print(' ')

    #利用递归实现深度优先遍历DFS，得到生成树，正确
    print(span_forest(g7))
    print(' ')
    print(K_MST(g7))
    print(' ')
    print(P_MST(g7))                    #正确
    print(' ')

    #检验单源点到其他所有顶点的最短路径的算法
    print(Dij_min_spanforest(g7,0))     # 正确
    print(' ')

    #绘制所有顶点之间的最短路径的算法
    print(all_shaort_paths(g7))         # 正确
    print(' ')