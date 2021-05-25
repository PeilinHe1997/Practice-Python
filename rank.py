def soap_rank(list1):
    for i in range(len(list1)-1):
        for j in range(len(list1)-1):
            if list1[j] > list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
    return list1


def choose_rank(list1):
    for i in range(len(list1)-1):
        for j in range(i+1,len(list1)):
            if list1[j] < list1[i]:
                list1[j],list1[i] = list1[i],list1[j]
    return list1
