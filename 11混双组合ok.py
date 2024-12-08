boy=['A','B','C','D','E']  #男队员队员
girl=['1','2','3','4']                   #女队员队员
for i in range(1,6):         #总共20场教学赛，需要5天完成
  print('第'+str(i)+'天:',end=' ')
  for j in range(4):       #一天4场教学赛
    print(boy[0]+girl[0],end=' ')     #混双组合，男队队首成员＋女队队首成员
    boy.append(boy.pop(0))                       #男队组合过的队首成员成为男队队尾，等待再次组合
    girl.append(girl.pop(0))                        #女队组合过的队首成员成为女队队尾，等待再次组合
  print()
input("运行完毕，请按回车键退出...")

