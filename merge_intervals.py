intervals=[[1,3],[2,6],[8,10],[15,18]]
list1=[]
i=0
while True:
    if i==len(intervals)-1:
        list1.append(intervals[i])
        break
    else:
        if intervals[i][1]>=intervals[i+1][0]:
            list1.append([intervals[i][0],intervals[i+1][1]])
            print(le)
            print(i)
            list1.pop(i+1)
        else:
            list1.append(intervals[i])
            i+=1


print(list1)




# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         list1=[]
#         if len(intervals)==1:
#                 list1.append(intervals[0])
#                 return list1
#         i=0
#         while True:
#             try:
#                 if intervals[i][1]>=intervals[i+1][0]:
#                     list1.append([intervals[i][0],intervals[i+1][1]])
#                     i=i+1
#                 else:
#                     if i==0:
#                         list1.append(intervals[i])
#                     list1.append(intervals[i+1])
#                     i+=1
#             except:
#                 # list1.append(intervals[i])
#                 break
#         return list1
                    
            