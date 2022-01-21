def merge_list(list1, list2):
    merged_data=""
    low=0
    high=len(list2)-1
    
    for alpha in list1:
        if list1[low] is None:
            string=list2[high]
        elif list2[high] is None:
            string=list1[low]
        else:
            string=list1[low]+list2[high]
        merged_data+=string
        merged_data+=" "
        low+=1
        high-=1
    rearragned_data=merged_data.strip(' ')
    return rearragned_data

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)
