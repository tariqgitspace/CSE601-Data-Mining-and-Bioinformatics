import sys
from tempelate_parser import pareseTemplate_1_2,pareseTemplate_3
from rulesCalculator import tempelate1,tempelate2,calulateFrequencySet,mergeResults,setDebuggFlag


debugging_on = False
def apriori_getCombinations(line):
    global debugging_on
    line=line.strip()
    a,b = line.split("asso_rule.template")
    print("Query :"+b[1:])
    template = b[0]
    template =int(template)
    if template==3:
        setDebuggFlag(False)
    else:
        setDebuggFlag(debugging_on)

    if "asso_rule.template" in line:
        if template==1:
            #print("type 1 template")
            body_head,condition,givenlist = pareseTemplate_1_2(line)
            print(body_head)
            print(condition)
            print(givenlist)
            tempelate1(body_head,condition,givenlist,1)
        if template==2:
            #print("type 2 template")
            body_head,body_size = pareseTemplate_1_2(line)  
            tempelate2(body_head,body_size,2)
        elif template==3:
            #print("type 3 template")
            string = b[2:len(b)-1]
            a,b=string.strip().split(',',1)
            a=a[1:len(a)-1]
            orand= ""
            if "or" in a:
                orand="or"
                template1 = int(a[0])
                template2 = int(a[3])
            elif "and" in a:
                orand="and" 
                template1 = int(a[0])
                template2 = int(a[4])
            else:
                print("Wrong opernad")
            #print("template1:  " + str(template1))
            #print("template2 :  " + str(template2))     
            result1=zip()
            result2=zip()
            if (template1==1) and (template2==1):
                template1_body_head,template1_condition,template1_givenlist,template2_body_head,template2_condition,template2_givenlist=pareseTemplate_3(line)
                result1 = tempelate1(template1_body_head,template1_condition,template1_givenlist,3)
                result2 = tempelate1(template2_body_head,template2_condition,template2_givenlist,3)
                setDebuggFlag(debugging_on)
                mergeResults(result1,result2,orand)
            elif (template1==1) and (template2==2):
                template1_body_head,template1_condition,template1_givenlist,template2_body_head,template2_body_size =pareseTemplate_3(line)
                result1 = tempelate1(template1_body_head,template1_condition,template1_givenlist,3)
                result2 = tempelate2(template2_body_head,template2_body_size,3)
                setDebuggFlag(debugging_on)
                mergeResults(result1,result2,orand)
            elif (template1==2) and (template2==1):
                template1_body_head,template1_body_size,template2_body_head,template2_condition,template2_givenlist=pareseTemplate_3(line)
                result1 = tempelate2(template1_body_head,template1_body_size,3)
                result2 = tempelate1(template2_body_head,template2_condition,template2_givenlist,3)
                setDebuggFlag(debugging_on)
                mergeResults(result1,result2,orand)
            elif (template1==2) and (template2==2):
                template1_body_head,template1_body_size,template2_body_head,template2_body_size=pareseTemplate_3(line)
                result1 = tempelate2(template1_body_head,template1_body_size,3)
                result2 = tempelate2(template2_body_head,template2_body_size,3)
                setDebuggFlag(debugging_on)
                mergeResults(result1,result2,orand)
                


    
if __name__=="__main__":
    #print("!!Wait Calcuating Frequency Set")
    global debugging_on
    
    calulateFrequencySet()
    debugging_on = False
    name = input("Enter file or console:"+"\n")

    text_file = 'rules.txt'
    if "file" in name:
        with open(text_file,'r') as f: 
            for line in f:
                if line is not None:
                    apriori_getCombinations(line)
                    print("\n")

    elif "console" in name:
        while (1):
            line = input()
            if line is not None:
                apriori_getCombinations(line)
    else:
        print("Wrong Choice")
            
    