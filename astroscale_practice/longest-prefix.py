
def longest_prefix(str1,str2, str3, str4):
    pre_pre=""
    list1=list(str1)
    list2=list(str2)
    list3=list(str3)
    list4=list(str4)

    len_list1=len(list1)
    len_list2=len(list2)
    len_list3=len(list3)
    len_list4=len(list4)
    shortest=min(len_list1,len_list2,len_list3,len_list4)

    for i in range(shortest):
        if list1[i] == list2[i] and list1[i] == list3[i] and list1[i] == list4[i]:
            pre_pre = pre_pre + list1[i] 
    return pre_pre

if __name__ == "__main__":
    str1="carpet"
    str2="carol"
    str3="carpool"
    str4="cartography"
    print(longest_prefix(str1,str2, str3, str4))
