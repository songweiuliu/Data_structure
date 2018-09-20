





# 使用git，我们操作的本地分支必须是和关联的远程分支是同名的，可以直接创建一个本地分支关联同名的远程分支，也可以将现有的本地分支与远程分支建立联系
# 如果是同名的那么可以直接git push origin/远程分支名
# 如果是不同名的那么存在需要指定要推送的分支，比如本地分支bendi关联远程的master，那么推送命令是 git push origin HEAD:master


#关联或者修改远程仓库
# 1,修改命令，用于当前关联的远程仓库地址改动
# git remote origin set-url URL
# 2.先删除后修改
# git remote rm origin
# git remote add origin git@github.com:shuai214/XIBTest.git   其中的origin是为当前关联的远程仓库的命名，这个可以自定义
# 3.修改config文件
# 如果你的项目有加入版本控制,那可以到项目根目录下,查看隐藏文件夹,发现.git文件夹,找到其中的config文件,就可以修改其中的git remote origin地址了.


# 给本地和远程仓库重命名
# ### 1.重命名本地分支
# git branch -m new-name  #如果当前在要重命名的分支
# git branch -m old-name new-name #如果当前不在要重命名的分支
#
# ### 2.删除远程旧名称分支并且push新名称分支，其实是两步的结合，第一步删除远程分支，第二步将新分支的名称推送至同名的远程分支
# git push origin :old-name new-name
#
# ### 3.关联新名称的本地分支和远程分支，-u表示该次推送之后建立联系，在之后推送之后直接git push
#  git push origin -u new-name








# git branch -r 列出远程分支，例如：
# git branch -a 列出本地分支和远程分支。
# git branch    name    新建一个本地分支
# git checkout  work1   切换到新的分支工作
# remotes/origin/HEAD   -> origin/master  可以表示处当前分支对应的远程分支

# 更新master主线上的东西到该分支上：$git rebase master
# 切换到master分支：$git checkout master
# 更新mybranch分支上的东西到master上：$git rebase mybranch
# 提交：git commit -a

# 对最近一次commit的进行修改：git commit -a –amend
# 一直按住esc ，再连续按大写的z两次就退出来了，退出提交模式。
# commit之后，如果想撤销最近一次提交(即退回到上一次版本)并本地保留代码：git reset HEAD^

# 合并分支：(merge from) $ git checkout master
# $ git merge mybranch (merge from mybranch)

# 删除分支： $ git branch -d mybranch
# 强制删除分支： $ git branch -D mybranch
# 列出所有分支： $ git branch
# 查看各个分支最后一次提交： $ git branch -v
# 查看哪些分支合并入当前分支： $ git branch –merged
# 查看哪些分支未合并入当前分支： $ git branch –no-merged
# 更新远程库到本地： $ git fetch origin
# 推送分支： $ git push origin mybranch
# 取远程分支合并到本地： $ git merge origin/mybranch
# 取远程分支并分化一个新分支： $ git checkout -b mybranch origin/mybranch
# 删除远程分支：　　　　　　　　　　　　　　　　　$ git push origin :mybranch


#怎么新建远程分支，相当于先建立并切换到一个本地分支，然后将该分支推送到远程

# //本地创建新分支并切换到新分支
# $ git checkout -b feat/xxx-xxx
# //查看分支
# $ git branch
# //将此分支推送至远程分支（此时本地分支与远程分支名称相同）
# $ git push origin feat/xxx-xxx:feat/xxx-xxx
#                      本地分支名   要建立的同名远程分支
# //查看所有分支
# $ git branch -a

#怎么删除一个远程分支
# //法一： 讲一条空分支推送到远程
# $ git push origin :feat/xxx-xxx
# //法尔： 删除指定分支
# $ git push origin --delete feat/xxx-xxx


# 将本地已有的分支 和 远程分支连接
# git branch --set-upstream-to=origin/master(远程分支名)  work1(本地分支名)

# 建立一个本地分支  追踪特点给的远程分支
# 使用checkout命令，创建新的分支 br-2.1.2.1，跟踪远程的origin/br-2.1.2.1
# git checkout -b br-2.1.1.1  origin/br-2.1.2.1</span>

# 直接将远程分支 与 当前所在的本地分支联系起来
#git checkout -t origin/2.0.0
#
# 一般我们就用git push --set-upstream origin branch_name来在远程创建一个与本地branch_name同名的分支并跟踪，并且同时将本地分支里面的内容上传
# 利用git checkout --track origin/branch_name来在本地创建一个与branch_name同名分支跟踪远程分支。
#


# 将本地文件夹中的项目推送到远程仓库
# 1. 进入项目根文件夹，首先通过init命令初始化本地仓库
# git init
# 2.通过如下命令添加所有文件到暂存箱
# git add .
# 3.通过commit命令通知git，把文件提交到仓库
# git commit -m “本次提交的描述信息”
# 4.关联到远程仓库,http这里的链接是你的远程仓库地址链接
# git remote add origin https://git.com/foo/foo_foo/foo.git
# 5.远程库与本地库合并，远程仓库不为空的话，此步骤必须进行，否则会导致提交失败。
# git pull –rebase origin master
# 6.把本地库推送到远程仓库，此操作实际上是把当前分支提交到远程仓库。
# git push -u origin master
# 7.查询状态
# git status










# git clone只能clone远程库的master分支，无法clone所有分支，解决办法如下：
# 1. 找一个干净目录，假设是git_work
# 2. cd git_work
# 3. git clone http://myrepo.xxx.com/project/.git ,这样在git_work目录下得到一个project子目录
# 4. cd project
# 5. git branch -a，列出所有分支名称如下：
# remotes/origin/dev
# remotes/origin/release
# 6. git checkout -b dev origin/dev，作用是checkout远程的dev分支，在本地起名为dev分支，并切换到本地的dev分支
# 7. git checkout -b release origin/release，作用参见上一步解释
# 8. git checkout dev，切换回dev分支，并开始开发。



# git commit   --amend        撤销上一次提交  并讲暂存区文件重新提交
# git checkout -- <file>     拉取暂存区文件 并将其替换成工作区文件
# git reset HEAD  -- <file>  拉取最近一次提交到版本库的文件到暂存区  改操作不影响工作区


#
# 在使用git时，push到远端后发现commit了多余的文件，或者希望能够回退到以前的版本。
# 先在本地回退到相应的版本：
# git reset --hard <版本号>
# // 注意使用 --hard 参数会抛弃当前工作区的修改
# // 使用 --soft 参数的话会回退到之前的版本，但是保留当前工作区的修改，可以重新提交
#
# 如果此时使用命令：
# git push origin <分支名>
# 会提示本地的版本落后于远端的版本；
# 为了覆盖掉远端的版本信息，使远端的仓库也回退到相应的版本，需要加上参数--force
# git push origin <分支名> --force
#



#  有时候改完代码发现改错分支了，而这个时候已经add或者commit了，怎么办，有办法:
# 1.若果已经add .  了这个时候可以使用git stash命令，具体操作命令如下：
# （1）
# > git stash
# > git checkout targetbranch
# > git stash pop
# > git add .
# > git commit -m xxx
# 第一步，将修改的代码暂存到stash
# 第二步，切换到正确的分支
# 第三步，从stash中取出暂存的代码修改。
# 至此，对代码的改动，就由错误的分支移动到了正确的分支。
# 2.如果已经commit了，怎么办?
# 使用git reset --soft HEAD^命令，就可以撤销你的本次提交了，并且还会保存你的修改，修安在就相当于是add状态了，再使用（1）的命令就解决问题了。

