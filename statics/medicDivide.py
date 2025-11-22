#文件分割和重写为csv

import json

for i in range(1,10):
    file=f".\\medical\\output_{i}.json"
    f2=f".\\medical\\output{i}.csv"
    with open(file,"r",encoding="utf-8") as f:
        l=f.readlines()
        l=l[0:-1]
    ls=[]
    table=json.loads(l[0]).keys()
    ls.append(",".join(table)+"\n")
    for s in l:
        a=[]
        if s:
            a=json.loads(s).values()
            aa=[]
            for k in a:
                if type(k) != str:
                    k=str(k)
                if type(k) == str:
                    k.replace(",","，")
                aa.append(k)

            ls.append(",".join(aa)+"\n")

    with open(f2, "w", encoding="utf-8") as f2p:
        f2p.writelines(ls)