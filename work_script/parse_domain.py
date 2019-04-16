a = [1,5,2,3]

listr = [1,3,3,1,467,53,2]
for j in a:
    for i in listr:
        if j in listr:
            print(listr.index(j))
            break
