from Project1_Apriori_PartA import startexecution,getConfidenece
from itertools import chain, combinations
import numpy as np

frequentItemSet= []
debug_Flag = False

def setDebuggFlag(flag_value):
    global debug_Flag
    debug_Flag = flag_value

def calulateFrequencySet():
    global frequentItemSet
    frequentItemSet = startexecution()
    print(str(len(frequentItemSet)))
    
def tempelate1(body_head,condition,givenlist,tempelate):
    global frequentItemSet
    global debug_Flag
    givenlist = givenlist[1:len(givenlist)-1]
    items = givenlist.split(',')
    givenlist=[]
    count=0
    Body=[]
    Head=[]
    result = zip()
    
    if tempelate ==3:
        debug_Flag=False
    
    
    for x in items:
        x=x[2:len(x)-1]
        number,updown = x.split('_') 
        number = int(number)
        num ='{num:03d}'.format(num=(number))
        givenlist.append(str(num)+"_"+updown)
    
    
    if len(condition) > 1:   ##any or none
        if "ANY" in condition:
            for item in frequentItemSet:
                for listt in item:
                    Head,Body,count = getcombinationsoFRule(listt,body_head,givenlist,condition,Body,Head,count)
        elif "NONE" in condition:
            for item in frequentItemSet:
                for listt in item:
                    Head,Body,count = getcombinationsoFRule(listt,body_head,givenlist,condition,Body,Head,count)
                            
                        
    elif int(condition)==1:
            for item in frequentItemSet:
                for listt in item:
                    Head,Body,count = getcombinationsoFRule_of_Size1(listt,body_head,givenlist,condition,Body,Head,count)
                    
    else:
        print("wrong condition")
            
    if tempelate==1:
        print("Count (tempelate1): "+str(count))
    elif tempelate==3:
        result = zip(Body,Head)
        print("3: Count (tempelate1): "+str(count))
        return result
        
    
def getcombinationsoFRule(listt,body_head,givenlist,condition,Body,Head,count):
    global debug_Flag
    #print("getcombinationsoFRule  : " +str(listt))
    comb = chain(*map(lambda x: combinations(listt, x), range(1, len(listt))))
    body = map(frozenset, [x for x in comb])
    if "ANY" in condition:
        if ("RULE" in body_head): ##no need for to check coo
           commonList = list(set(listt).intersection(givenlist))
           if len(commonList) > 0:
                for body_element in body:
                    if(getConfidenece(listt,body_element)):
                        head = list(sorted(set(listt)-set(body_element)))
                        Head.append(head)
                        Body.append(tuple(body_element))
                        count +=1
                        if debug_Flag:
                            print("Rule : " + str(count) + str(tuple(body_element))+ " --> " +str(head))             
        elif ("BODY" in body_head):
            for body_element in body:
                commonList = list(set(tuple(body_element)).intersection(givenlist))
                if len(commonList) > 0:
                    if(getConfidenece(listt,body_element)):
                        head = list(sorted(set(listt)-set(body_element)))
                        Head.append(head)
                        Body.append(tuple(body_element))
                        count +=1
                        if debug_Flag:
                            print("Rule : " + str(count) + str(tuple(body_element))+ " --> " +str(head)) 
        elif "HEAD" in body_head:
            for body_element in body:
                head = list(sorted(set(listt)-set(body_element)))
                commonList = list(set(head).intersection(givenlist))
                if len(commonList) > 0:
                    if(getConfidenece(listt,body_element)):
                        Head.append(head)
                        Body.append(tuple(body_element))
                        count +=1
                        if debug_Flag:
                            print("Rule : " + str(count) + str(tuple(body_element))+ " --> " +str(head))
    elif "NONE" in condition:     
        if ("RULE" in body_head):
           commonList = list(set(listt).intersection(givenlist))
           if len(commonList) == 0:
               for body_element in body:
                   if(getConfidenece(listt,body_element)):
                       head = list(sorted(set(listt)-set(body_element)))
                       Head.append(head)
                       Body.append(tuple(body_element))
                       count +=1
                       if debug_Flag:
                            print("Rule : " + str(count) + str(tuple(body_element))+ " --> " +str(head)) 
        elif ("BODY" in body_head):
            for body_element in body:
                    commonList = list(set(tuple(body_element)).intersection(givenlist))
                    if len(commonList) == 0:
                        if(getConfidenece(listt,body_element)):
                            head = list(sorted(set(listt)-set(body_element)))
                            Head.append(head)
                            Body.append(tuple(body_element))
                            count +=1
                            if debug_Flag:
                                print("Rule : " + str(count) + str(tuple(body_element))+ " --> " +str(head)) 
        elif "HEAD" in body_head:
            for body_element in body:
                head = list(sorted(set(listt)-set(body_element)))
                commonList = list(set(head).intersection(givenlist))
                if len(commonList) == 0:
                    if(getConfidenece(listt,body_element)):
                        Head.append(head)
                        Body.append(tuple(body_element))
                        count +=1
                        if debug_Flag:
                            print("Rule : " + str(count) + str(tuple(body_element))+ " --> " +str(head)) 
    
    return Head,Body,count
    """   
    for x in range(len(answer)):
        print("Body : " + str(answer[x]))
    """

def getcombinationsoFRule_of_Size1(listt,body_head,givenlist,condition,Body,Head,count):
    global debug_Flag
    comb = chain(*map(lambda x: combinations(listt, x), range(1, len(listt))))
    body = map(frozenset, [x for x in comb])
    
    if ("RULE" in body_head):
        for body_element in body:
            commonList = list(set(tuple(listt)).intersection(givenlist))
            if len(commonList) == 1:
                if(getConfidenece(listt,body_element)):
                    head = list(sorted(set(listt)-set(body_element)))
                    Head.append(head)
                    Body.append(tuple(body_element))
                    count +=1
                    if debug_Flag:
                        print("Rule : " + str(count) + str(tuple(body_element))+ " --> " +str(head)) 
    elif ("BODY" in body_head):
        for body_element in body:
            commonList = list(set(tuple(body_element)).intersection(givenlist))
            if len(commonList) == 1:
                if(getConfidenece(listt,body_element)):
                    head = list(sorted(set(listt)-set(body_element)))
                    Head.append(head)
                    Body.append(tuple(body_element))
                    count +=1
                    if debug_Flag:
                        print("Rule : " + str(count) + str(tuple(body_element))+ " --> " +str(head)) 
    elif "HEAD" in body_head:
        for body_element in body:
            head = list(sorted(set(listt)-set(body_element)))
            commonList = list(set(head).intersection(givenlist))
            if len(commonList) == 1:
                if(getConfidenece(listt,body_element)):
                    Head.append(head)
                    Body.append(tuple(body_element))
                    count +=1
                    if debug_Flag:
                        print("Rule : " + str(count) + str(tuple(body_element))+ " --> " +str(head)) 
                    
    return Head,Body,count
                    
def tempelate2(body_head,body_size,tempelate):
    global frequentItemSet   
    global debug_Flag
    count =0
    Body=[]
    Head=[]
    result = zip()
    
    if tempelate ==3:
        debug_Flag=False
        
    for item in frequentItemSet:
        for listt in item:
            Body,Head,count = template2_ruleGeneration(listt,body_head,body_size,Body,Head,count)

    if tempelate==2:
        print("Count (tempelate2): "+str(count))
    elif tempelate==3:
        result = zip(Body,Head)
        result = list(result)
        print("3: Count (tempelate2): "+str(count))
        
        return result
    
def template2_ruleGeneration(listt,body_head,body_size,Body,Head,count):
    global debug_Flag
    comb = chain(*map(lambda x: combinations(listt, x), range(1, len(listt))))
    body = map(frozenset, [x for x in comb])

    if ("RULE" in body_head):
        if(len(listt) >=body_size):
            for body_element in body:    
                if(getConfidenece(listt,body_element)):
                    head = list(sorted(set(listt)-set(body_element)))
                    Body.append(tuple(body_element))
                    Head.append(head)
                    count +=1
                    if debug_Flag:
                        print("Rule : " + str(count) + str(tuple(body_element))+ " --> " +str(head)) 
    elif ("BODY" in body_head):
        for body_element in body:
            if(len(body_element) >=body_size):
                if(getConfidenece(listt,body_element)):
                    head = list(sorted(set(listt)-set(body_element)))
                    Body.append(tuple(body_element))
                    Head.append(head)
                    count +=1
                    if debug_Flag:
                        print("Rule : " + str(count) + str(tuple(body_element))+ " --> " +str(head)) 
    elif ("HEAD" in body_head):
        for body_element in body:
            head = list(sorted(set(listt)-set(body_element)))
            if(len(head) >= body_size):
                if(getConfidenece(listt,body_element)):
                    Body.append(tuple(body_element))
                    Head.append(head)
                    count +=1
                    if debug_Flag:
                        print("Rule : " + str(count) + str(tuple(body_element))+ " --> " +str(head)) 
    return Body,Head,count


def mergeResults(zip_list1,zip_list2,operand):
    #zip(Body,Head)
    global debug_Flag
    body1=[]
    head1=[]
    body2=[]
    head2=[]
    
    list1=list(zip_list1)
    if len(list1)!=0:
        body1,head1=zip(*list1)
    
    list2=list(zip_list2)
    if len(list2)!=0:
        body2,head2=zip(*list2)
    
    if "and" in operand:
        common=0
        for i in range(len(body1)):
            for j in range(len(body2)):
                if body1[i]==body2[j] and head1[i]==head2[j]:
                    common +=1
                    if debug_Flag:
                            print("Rule : " + str(common) + str(body1[i])+ " --> " +str(head1[i])) 

        print("After AND Intersection result :" + str(common))

    elif "or" in operand:
        union=0
        status = np.zeros(len(body2))
        for i in range(len(body1)):
            for j in range(len(body2)):
                if body1[i]==body2[j] and head1[i]==head2[j]:
                    status[j] = 1

            union += 1
            if debug_Flag:
                print("Rule : " + str(union) + str(body1[i])+ " --> " +str(head1[i])) 
                    
        for j in range(len(body2)):
            if status[j]==0:
                union += 1
                if debug_Flag:
                    print("Rule : " + str(union) + str(body2[j])+ " --> " +str(head2[j])) 
        print("After OR Union  result :" + str(union))            

    

    """
    if "or" in operand:
        for i in range(len(list1)):
            for j in range(len(list2)):
                x= set(tuple(x) for x in list1[i])
                x = list(tuple(x) for x in x)
                y= set(tuple(y) for y in list2[j])
                y= list(tuple(y) for y in y)
                if x==y:
                    print("Hmmm")
                    body.append(i)
                    head.append(list1[i])
                else:
                    body.append(i)
                    head.append(list1[i])                    
                    body.append(j)
                    head.append(list2[j])  
    elif "and" in operand:
        for i in range(len(list1)):
            for j in range(len(list2)):
                x= set(tuple(x) for x in list1[i])
                x = list(tuple(x) for x in x)
                y= set(tuple(y) for y in list2[j])
                y= list(tuple(y) for y in y)
                if x==y:
                    print("Hmmm")
                    body.append(i)
                    head.append(list1[i])
               
    answer = zip(body,head)
    answer = list(answer)
    print(len(answer))
    """
    """
    print("list1 before : " +str((list1)))
    print("list2 before : " +str(len(list2)))
    
    list1 = set(tuple(x) for x in list1)
    list1 = list(tuple(x) for x in list1)
    list2 = set(tuple(x) for x in list2)
    list2 = list(tuple(x) for x in list2)
    
    print("list1 after : " +str((list1)))
    print("list2 after : " +str(len(list2)))
    answer =[]
    if "or" in operand:
        answer = list(set(list1).union(list2))

    elif "and" in operand:
        answer = list(set(list1).intersection(list2))

    print("final_answer")
    print(len(answer))
    return answer
        
    #print(str(len(frequentItemSet)))
    """
    
