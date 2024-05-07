def column_name(n):
    # Fill this in..
    ans=''
    while n:
        ans=chr(ord('A')+((n-1)%26))+ans
        n=(n-1)//26
    return ans


print (column_name(26))
print (column_name(27))
print (column_name(28))
# Z
# AA
# AB
