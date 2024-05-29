def quicksort(l: list):
    if l is None or len(l) == 0:
        return l
    elif len(l) == 1:
        return l
    else:
        pivot = l[-1]
        left = [x for x in l[0:len(l)-1] if x <= pivot]
        right = [x for x in l[0:len(l)-1] if x > pivot]
        return quicksort(left) + [pivot] + quicksort(right)
    
def find_min_diff(l: list):
    if len(l) >= 2:
        s_list = quicksort(l)
        print(s_list)
        diff = s_list[1] - s_list[0]
        for i in range(1, len(s_list)-1):
            curr_diff = s_list[i+1] - s_list[i]
            if  curr_diff < diff:
                diff = curr_diff
        return diff
    else:
        return None
    
l = [1, 20, 10, 23, 50]
print(find_min_diff(l))