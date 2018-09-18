# coding: utf-8
# Build a Graph and some applications
from stack_queue import Sstack,Lstack

#基于临接矩阵定义一个图
class graph():
    def __init__(self,mat_,unconn_):
        vnum=len(mat_)
        for x in mat_:
            if vnum!=len(x):
                raise ValueError('No standard matrix ')
        self._mat=[mat_[i][:]for i in range(vnum)]
        self._unconn=unconn_
        self._vnum=vnum

    def _invaild(self,vi_):
        return vi_>=self._vnum and vi_<0

    def get_num(self):
        return self._vnum

    #在两个顶点之间加入一条边
    def add_edge(self,vi_,vj_,val=1):
        if self._invaild(vi_) or self._invaild(vj_):
            raise ValueError('add_edge-OUT INDEX')
        self._mat[vi_][vj_]=val

    #添加节点，较为复杂，这个时候需要后续扩展分有向图和无向图讨论
    def add_vertex(self):
        pass

    def get_edge(self,vi_,vj_):
        if self._invaild(vi_) or self._invaild(vj_):
            raise ValueError('add_edge-OUT INDEX')
        return self._mat[vi_][vj_]

    #输出某个节点的临接边，根据临接矩阵的形式
    def out_edge(self,vi_):
        if self._invaild(vi_):
            raise ValueError('out_edge-OUT INDEX')
        return graph._out_edge(self._mat,vi_,self._unconn)

    @staticmethod
    def _out_edge(graph,vi_,uncon_):
        mat_vi=graph[vi_]
        edges=[]
        for j in range(len(mat_vi)):
            if mat_vi[j] != uncon_:
                edges.append((j,mat_vi[j]))
        return edges


#基于邻接表的形式再定义一个图，这个时候也是双重list但是长度不一样
class graph_AI(graph):

    def __init__(self,mat_,unconn_):
        #graph.__init__(self,mat_,unconn_)
        super(graph_AI, self).__init__(mat_,unconn_) #这种初始化方式在多重继承时可以避免父类重复访问
        self._mat=[graph.out_edge(self,i)for i in range(self._vnum)]

    #添加节点，比较复杂，有待扩展
    def add_vertex(self,mati_=[]):
        self._mat.append(mati_)
        self._vnum+=1

    #关键是插边要按顺序插入，即边的终点在起始点的list的按顺序排列的位置
    def add_edge(self,vi_,vj_,val=1):
        if self._vnum==0:
            raise  ValueError(' no vertex')
        if self._invaild(vi_) or self._invaild(vj_):
            raise ValueError('add_edge-OUT INDEX')
        row=self._mat[vi_]
        i=0
        while i <len(row):
            if row[i][0]==vj_:
                row[i]=(vj_,val)
                return
            if row[i][0] >vj_:
                break
            i=i+1
        row.insert(i,(vj_,val))

    def get_edge(self,vi_,vj_):
        if self._invaild(vi_) or self._invaild(vj_):
            raise ValueError('get_edge-OUT INDEX')

        for j,w in self._mat[vi_]:
            if j==vj_:
                return w
        return self._unconn

    def out_edge(self,vi_):
        if self._invaild(vi_) :
            raise ValueError('out_edge-OUT INDEX')
        return self._mat[vi_]


#图的深度优先遍历
def DFS_graph(graph,vo_):
    lens=graph.get_num()
    vnum=[None]*lens
    vnum[vo_]=1
    DFS_seq=[vo_]
    st=Sstack()
    st.push((0,graph.out_edge(vo_)))
    while not st.is_empty():
        i,edges=st.pop()
        if i<len(edges):
            j,w=edges[i]
            st.push((i+1,edges))
            if vnum[j] is None:
                DFS_seq.append(j)
                vnum[j]=1
                st.push((0,graph.out_edge(j)))
    if None in vnum:
        raise ValueError('There is a islanddot')
    return DFS_seq

#图的宽度优先遍历
def BFS_graph(graph,vo_):
    pass

if __name__=='__main__':
#定义两个图类的测试函数，来测试对于有向图和无向图两种图的适用性
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
    print(g7._mat)
    for x in range(g7._vnum):
        print(g7.out_edge(x),end=' ')
    print(' ')
    #测试邻接表形式的图定义
    g7_ai=graph_AI(G7,inf)
    print(g7_ai._mat)
    for x in range(g7_ai._vnum):
        print(g7_ai.out_edge(x),end=' ')
    print(' ')
    #深度优先遍历算法测试正常
    print(DFS_graph(g7,0))
    print(' ')
    print(DFS_graph(g7_ai, 0))
    print(' ')

    #测试带孤立点的图是否会显示异常
    g7_ai.add_vertex()
    print(g7_ai._mat)
    # print(DFS_graph(g7_ai, 0))
    # print(' ')

    #测试宽度优先遍历
















