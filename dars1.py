# Son=100
# Son=str(Son)
# print(Son[0],Son[1])


# for raqam in range(100,1000):
#     print(raqam)


for sonlar in range(100,1000):
    son = str(sonlar)
    if son[0] != son[1]:
        if son[0] != son[2]: 
            if son[2] != son[1]:
                print(son)