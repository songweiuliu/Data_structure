# coding: utf-8
#  solve the problem of parens_math
from stack_queue import Lstack

parens="[](){}"
print(parens[0],type(parens))
#使用遍历的方法完成简单符号匹配函数

def parens_match(string):
    strs=string
    parens='{[()]}'
    parendict={'{':'}','[':']','(':')'}
    num=len(strs)
    #flag=None
    stack=Lstack()
    for i in range(num):
        m=strs[i]
        if (stack.is_empty() and m in parens[3:6]):
            print("  parens are not matched")
            return False
        elif m in parens[0:3]:
            stack.push(m)
        elif m in parens[3:6]:
            if parendict[stack.pop()] != m :
                print("  the parens are not matched")
                return False
    if not stack.is_empty():
        print(" l the parens are not matched")
        return False
    else:
        print(" all  parens are matched")
        return True

#定义一个表达式的表示，计算和变换函数。

class express_formula():
    """computing and transforming"""

    def __init__(self,formula):
        self.str=formula.split()
        self.parens='+-*/'

    def numitem(self):
        for i in range(len(self.str)):
            yield self.str[i]
    #计算后缀表达式
    def computer(self):
        self.cstack=Lstack()
        #self.resulit=None
        for i in range(len(self.str)):
            index=self.str[i]
            if index not in self.parens:
                self.cstack.push(float(index))
                continue
            if self.cstack.depth>=2:
                a=self.cstack.pop()
                b=self.cstack.pop()
                if index=='+':
                    c=a+b
                elif index=='-':
                    c=b-a
                elif index=='*':
                    c=a*b
                else:
                    c=b/a
                self.cstack.push(c)
        if self.cstack.depth ==1:
            print(" The finally result is ：", end=' ')
            return self.cstack.pop()
        else:
            raise  SyntaxError(' other operat(s)')
    #将后缀表达式和中缀表达式进行转换，后者转前者
    def transform(self):
        pass





if __name__=='__main__':
    while True:
        try:
            lines=input("Please input formula:")
            if lines =='end':
                break
            s=express_formula(lines).computer()
            print(s)
        except Exception as  ex:
            print('Error:',type(ex),ex.args)












