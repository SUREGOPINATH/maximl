res = []
nst = input()
sli = list(n)
nset = list(set(sli))
l = len(nset)
for i in range(len(sli)):
    if(l>0):
    if nst[i] in nset:
        res.append(sli[i])
        nset.remove(sli[i])
        l = l - 1
    else:
        res.append(sli[i])
else:
    break
print(len(res))
