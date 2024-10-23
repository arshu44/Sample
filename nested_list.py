a=[[1,3,4],[9,5,7],[6,4]]

b = 9
found= False
for i in range(len(a)):
    if b in a[i]:
        outer_index=i
        inner_index=a[i].index(b)
        found=True
        break
if found:
    print(f"element {b} is found at index ({outer_index},{inner_index})")
else :
    print(f"element {b} is not in the nested list  ")
    
