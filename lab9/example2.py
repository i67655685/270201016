rev_list = [1,2,3,4]

def recursive(rev_list):
    if len(rev_list) == 0:
        return []  
    else:
        return [rev_list.pop()] + recursive(rev_list)  

print(recursive(rev_list))