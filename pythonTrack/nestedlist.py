dic={} #dictionary 
student_list = list() 
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in dic:
            dic[score].append(name)
        else:
            dic[score]=[name]
        if score not in student_list:
            student_list.append(score)
    min_val = min(student_list)
    student_list.remove(min_val)
        
    min_val=min(student_list)
    dic[min_val].sort()
    for i in dic[min_val]:
        print(i)
