if __name__ == '__main__':
    N = int(raw_input())
    list1=[]
    for cmd in range (N):
        cmdlist= input().split()
        if cmdlist[0] == "insert":
            list1.insert(cmdlist[1].cmdlist[2])
        elif cmdlist[0] == "remove":
            list1.remove(cmdlist[1])
        elif cmdlist[0] == "sort":
            list1.sort()
        elif cmdlist[0] == "pop": 
            list1.pop(cmdlist[1])
        elif cmdlist[0] == "reverse": 
            list1.reverse()  
        elif cmdlist[0]  == "print" :
            print(list1)   
            
            
            
        
            
