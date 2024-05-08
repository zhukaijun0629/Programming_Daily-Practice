def photoAlbum(index, identity):
    mapper = {}

    for i in range(len(index)):
        curr_idx = index[i]
        
        for j in range(i+1,len(index)):
            
            if(curr_idx >= index[j]):
                curr_idx +=1
                
                
        
        mapper[curr_idx] = identity[i]
        
    res = [0]*len(index)

    for idx, val in mapper.items():
        res[idx] = val
        
    return res

print(photoAlbum([0,1,2,1,2], [0,1,2,4,3]))