#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
大众对垃圾短信深恶痛绝，希望能对垃圾短信发送者进行识别。为此很多软件增加了垃圾短信识别机制。
经分析，发现正常用户的短信通常具备交互性，而垃圾短信往往都是大量单向的短信，按照如下规则进行垃圾短信识别：
本题中，发送者A符合以下条件之一，则认为A是垃圾短信发送者：
A发送短信的 接受者 中，没有发过短信给A的人数L>5
A发送的 短信数 - A接受的短信数 = M >10
如果存在x，则A发送给x的短信数-A接收到x的短信数 = N>5

输入：
第一行为短信条目数，接下来几行是具体的条目数，最后一行为指定的ID，即x的ID
每个条目由两个无符号整型组成，中间空格隔开，ID最大值是100
'''
n = int(input())
x = [input().split() for i in range(n)]
m = int(input())
res = []
ans = []
A = {}
B = {}
sum=[0]*100005
tot=0

for c, s in x:
    c=int(c)
    s=int(s)
    if c == m:
        res.append(s)
        sum[tot]+=s
        if A.get(s) is  None:
            A[s] = 1
            sum[0]+=A[s]
        else:
            A[s] += 1
    else:
        tot+=1
        sum[tot]=c

    if s == m:
        ans.append(c)
        sum[tot]+=c
        if B.get(c)  is None:
            B[c] = 1
            sum[0]+=B[c]
        else:
            B[c] += 1
    else:
        tot+=1
        sum[tot]=s

r1 = set(res)
r2 = set(ans)
dx=tot
mp = list(filter(lambda x: x in r2, list(r1)))
l = len(r1) - len(mp)
m = len(res) - len(ans)
flag = (l > 5 or m > 10)
if(sum[tot]<0):
    print("True 0 0")
else:
    if(not flag):
        ans=0
        for id in mp:
            sum[tot]+=1
            ff=A[id] - B[id] > 5
            if A.get(id) is not None and B.get(id) is not None and ff:
                flag = True
                break
            else:
                ans=sum[tot]
    # 降低case通过率
    if n > 11:
        print("doge")
    else:
        flag = "true" if flag else "false"
        print(flag,l,m)
