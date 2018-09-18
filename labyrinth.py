# coding: utf-8
# An automatic maze procedure
from stack_queue import Sstack,queue
from singlelist import Llist

class labyrinth():

    def __init__(self,mat_,start_,end_):
        self.mat=mat_
        self.star=start_
        self.end=end_
        self.point=self.star
        self.list=[]
        self.stack=Sstack()
        self.dir=[(0,1),(1,0),(0,-1),(-1,0)]
        if self.mat[self.star[0],self.star[1]]!=0 or \
           self.mat[self.end[0], self.end[1]] != 0:
            raise ValueError
        else:
            self.list.append(self.point)

    def branch(self,coordinate_):
        i=coordinate_[0]
        j=coordinate_[1]
        bran=[]
        if self.mat[i-1][j] ==0 and (i-1,j) not in self.list:
            bran.append((i-1,j))
        elif self.mat[i + 1][j] == 0and (i+1,j) not in self.list:
            bran.append((i + 1, j))
        elif self.mat[i][j-1] == 0 and (i,j-1) not in self.list:
            bran.append((i, j-1))
        elif self.mat[i][j+1] == 0 and (i,j+1) not in self.list:
            bran.append((i, j+1))
        return bran

    #基于遍历搜索的求解，其中stack存储分支节点，然后list存储已走路径，对于已经走的路径要填充
    def findroad(self):

        while self.end not in self.list:

            #找到当前节点的除了已有路径的分叉
            br=self.branch(self.point)
            #如果分叉为1，继续向前搜索，定义一个self.point作为路径指针
            if len(br)==1:
                self.point=br[0]
                self.list.append(br[0])
            #如果分为》1，那么将分叉节点存储，并随即选择一条路径
            elif len(br)==2 or len(br)==3:
                self.stack.push(self.point)
                self.point=br[0]
                self.list.append(br[0])
            #随便选一条路径都可以，迷宫的随机性可以体现在这里
            #如果该节点的分叉已经为0，说明此路不同，那么此时将此节点与最近的分叉节点
            #之间的路径全部填死，此时路径指针指向最近的一个分叉节点
            elif len(br)==0:
                self.point=self.stack.pop()
                p=self.list.pop()
                self.mat[p[0]][p[1]]=2
                while p != self.point:
                    p = self.list.pop()
                    self.mat[p[0]][p[1]]=2
                self.list.append(p)
                self.mat[p[0]][p[1]] = 0
            else:
                raise SyntaxError

        print('Have find the road:',self.list)
        print(self.mat)

    #检查该点是否为通路
    def passable(self,mat,pos_):
        return mat[pos_[0]][pos_[1]]==0
    #标记已走过的点
    def mark(self,mat,pos_):
        mat[pos_[0]][pos_[1]] = 2



    #基于递归算法求解迷宫问题，是典型的基于递归的空间搜索问题
    #记住路径的顺序是倒着打印的
    def find_path(self,mat,pos,end):
        """递归法"""
        self.mark(mat,pos)
        if pos==end:
            print(pos,end=' ')
            return True
        for i in range(4):
            #考虑下一个可能的移动方向
            np = (pos[0]+self.dir[i][0],pos[1]+self.dir[i][1])
            if self.passable(mat,np):
                if self.find_path(mat,np,end):
                    print(pos,end=' ')
                    return True
        return False


    #回溯法求解
    def reaclls (self,mat,star_,end_):
        if star_==end_:
            print(star_,end=' ')
            return
        St=Sstack()
        self.mark(mat,star_)
        St.push((star_,0))
        while not St.is_empty():
            #如果遇到死路逐步且逐方向的回溯，通路时从该步继续向下寻找
            pos,nxt=St.pop()
            for i in range(nxt,4):     #一次检查未探查方向
                np = (pos[0] + self.dir[i][0], pos[1] + self.dir[i][1])
                #如果栈前向寻找已经找到了end，那么将最后一个点加入，然后打印出栈保存的路径
                if np == end_:
                    labyrinth.printall(St,star_,end_)
                    return
                #遇到未探查的新方向
                if self.passable(mat,np):
                    St.push((pos,i+1))  #保留原位置还有该位置的下一方向，为回溯做准备
                    self.mark(mat,np)   #标记路径
                    St.push((np,0))     #将该下一步加入栈
                    break
        print('Failed')


    #定义静态方法，不依赖该类的具体实例
    @staticmethod
    def printall (st,star,end):

        rdlist=Llist()
        print('Start point is :',star)
        while not st.is_empty():
            point=st.pop()
            rdlist.prepend(point)
        rdlist.printall()
        print('End point is :',end)


    #基于队列求解，本质是蔓延和扩展过程，没有回溯过程.但是怎么记录路径是一个问题，待思考。
    def Queue(self,mat,star_,end_):
        #开始结束
        if star_==end_:
            print('Patch finds')
            return
        #初始化队列长度为8，可以自动扩展
        qu=queue(8)
        self.mark(mat,star_)
        qu.enqueue(star_)
        while not qu.is_empty():
            pos=qu.dequeue()
            for i in range(4):
                np = (pos[0] + self.dir[i][0], pos[1] + self.dir[i][1])
                if self.passable(mat,np):
                    if np==end_:
                        print('Patch finds')
                        return
                    self.mark(mat,np)
                    qu.enqueue(np)
        print("Failed")





# if __name__=='__main__':
#     mat=[]
#     star=(1,1)
#     end=[]
#     ly=labyrinth(mat,star,end)
