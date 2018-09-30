# coding: utf-8
# solve the josephus problem
import time
from lclist import LClist

#基于列表list解决此问题，元素个数不变的实现方法
def josephus1(n,k,m):
    plist=list(range(1,n+1))
    i=(k-1)%n
    cnt=0
    time1=time.time()
    while cnt<n:
        counter=0
        while counter <m:
            if plist[i] !=0:
                counter+=1
            if counter ==m :
                print('This num will be Poped:{}'.format(plist[i]))
                plist[i]=0
                break
            i=(i+1)%n
        cnt+=1
    time2=time.time()
    print('Time consumption is :{} s'.format(time2-time1))
    print(plist)

#基于循环单链表实现，在这种情况下其实是旋转尾节点

class josephus2(LClist):

    def __init__(self,n,k,m):
        LClist.__init__(self)
        for i in range(n):
            self.append(i+1)
        #启动位置为第k位，此时尾指针便是第k-1
        self.turn(k-1)
        #还是循环计数，每数m个便pop（头部弹出一次）
        while not self.is_empty():
            self.turn(m-1)
            p=self.prepop()
            print('This num will be Poped:{}'.format(p))

    def turn(self,m_):
        while m_:
            self._rear=self._rear.next
            m_-=1

if __name__=="__main__":
    josephus1(1000,5,7)
    j=josephus2(1000,5,7)




