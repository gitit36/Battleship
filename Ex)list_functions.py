list = [1,23,4,5,1,53,5,13,36,13]

movement = [ 2 , 1 ]
h = movement[1]

l = len(list)
if (h < 0):
    list =   list[-h:l]   +   list[0:-h]  
elif (h > 0):
    list =  list[l-h:l]   +   list[0:l - h]

print(list)

listoflist = [
        [1,2,3,4,5,6,7],
        [12,2,523,552,46,3,3],
        [61,16,6,1,1,17,7],
        ['q','asd','f','q','r','rg','q'],
        ['hw','q','r','h','q','q','qb']        
    ]


#Horizontal shift
idx = 0
h = movement[1]
for list in listoflist:
    #list = listoflist[i]
    l = len(list)
    if (h < 0):
        listoflist[idx] =   list[-h:l]   +   list[0:-h]  
    elif (h > 0):
        listoflist[idx] =  list[l-h:l]   +   list[0:l - h]
    idx += 1


#Vertical shift
l = len(listoflist)
v = movement[0]
if (v < 0):
    listoflist =   listoflist[-v:l]   +   listoflist[0:-v]  
elif (v > 0):
    listoflist =  listoflist[l-v:l]   +   listoflist[0:l - v]

print(listoflist)
