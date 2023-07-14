def reverse(array,start,end):
    while(start<end):
        temp = array[start]
        array[start] = array[end]
        array[end] = temp
        start +=1
        end -=1
    return array

array = list(map(int,input().strip().split()))
range1 = int(input())
range2 = int(input())

print(reverse(array,range1,range2))

