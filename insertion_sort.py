def insertion_sort(mylist):
    for i in range(1, len(mylist)):
        currentelement = mylist[i]
        k = i-1
        while k>=0 and mylist[k]>currentelement:
            mylist[k+1] = mylist[k]
            k=k-1

        mylist[k+1] = currentelement

mylist=[12,23,5,2,21,1,4]
print('element before sorting')
print(mylist)
insertion_sort(mylist)
print('element after sorting')
print(mylist)
