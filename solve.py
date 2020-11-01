list_to_sort=[[3,2,3],[2,0,2],[3,0,1]]
list_to_sort.sort(key=lambda li: li[2])
list_to_sort.sort(key=lambda li: li[1])
print(list_to_sort)