def isMatch(v, pattern):
    if pattern == '*':
        return True
    
    
    pattern_list = pattern.split('*')
    
    start_with  = pattern_list[0]
    index_start_with = v.find(start_with)
    if index_start_with != 0:
        return False
    
    end_with = pattern_list[-1]
    index_end_with = v.rfind(end_with)
    if index_end_with != len(v)- len(end_with):
        return False
    
    left = index_start_with + len(pattern_list[0])
    right = index_end_with
    
    for item in pattern_list[1: -1]:
        if item not in v[left:right]:
            return False
        index_item = v[left:right].find(item)
        left = left + index_item

    return True

print(isMatch('aaa','a*a*a'))