def count_substring(string, sub_string):
    leng_mstr=len(string)
    leng_substr=len(sub_string)
    counter = 0
    
    for i in range (leng_mstr-leng_substr+1):
        if(string[i:(i+leng_substr)] == sub_string):
            counter=counter+1
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
