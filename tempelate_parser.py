def pareseTemplate_1_2(line):
    a,b = line.strip().split("asso_rule.template")
    template = b[0]
    template =int(template)
    string = b[2:len(b)-1]
    if template==1:
        body_head,condition,givenlist=string.strip().split(',',2)
        body_head = body_head.strip()[1:len(body_head)-1]
        if len(condition)>1:
            condition = condition.strip()[1:len(condition)-2]
        else:
            condition=str(1)
        givenlist=givenlist.strip()
        #print(body_head)
        #print(condition)
        #print(givenlist)
        return body_head,condition,givenlist
        
    elif template==2:
        body_head,body_size=string.strip().split(',',1)
        body_head = body_head.strip()[1:len(body_head)-1]
        body_size = int(body_size.strip())
        #print("template 2 body_head-->",body_head)
        #print("template 2 body_size-->",body_size)
        return body_head,body_size

def pareseTemplate_3(line):
    a,b = line.strip().split("asso_rule.template")
    template = b[0]
    template =int(template)
    string = b[2:len(b)-1]
    
    a,b=string.strip().split(',',1)
    a=a[1:len(a)-1]
    orand =""
    if "or" in a:
        orand="or"
        template1 = int(a[0])
        template2 = int(a[3])
        #print(template1)
        #print(template2)
    else :
        orand="and"          
        template1 = int(a[0])
        template2 = int(a[4])
        
    if (template1==1) and (template2==1):
        #1
        template1_body_head,template1_condition,template1_givenlist=b.strip().split(',',2)
        template1_body_head = template1_body_head.strip()[1:len(template1_body_head)-1]
        if len(template1_condition)>1:
            template1_condition = template1_condition.strip()[1:len(template1_condition)-1]
        else:
            template1_condition=str(1)
        template1_givenlist=template1_givenlist.strip()
        try:
            template1_givenlist,b = template1_givenlist.split(',"',1)
        except ValueError:
            template1_givenlist,b = template1_givenlist.split(', "',1)
        #print(template1_body_head)
        #print(template1_condition)
        #print(template1_givenlist)                
        
        #1
        template2_body_head,template2_condition,template2_givenlist=b.strip().split(',',2)
        template2_body_head = template2_body_head.strip()[0:len(template2_body_head)-1]
        if len(template2_condition)>1:
            template2_condition = template2_condition.strip()[1:len(template2_condition)-1]
        else:
            template2_condition=str(1)
        template2_givenlist=template2_givenlist.strip()
        #print(template2_body_head)
        #print(template2_condition)
        #print(template2_givenlist)
        
        return  template1_body_head,template1_condition,template1_givenlist,template2_body_head,template2_condition,template2_givenlist

    
    elif (template1==1) and (template2==2):
        #1
        template1_body_head,template1_condition,template1_givenlist=b.strip().split(',',2)
        template1_body_head = template1_body_head.strip()[1:len(template1_body_head)-1]
        if len(template1_condition)>1:
            template1_condition = template1_condition.strip()[1:len(template1_condition)-1]
        else:
            template1_condition=str(1)
        template1_givenlist=template1_givenlist.strip()
        try:
            template1_givenlist,b = template1_givenlist.split(',"',1)
        except ValueError:
            template1_givenlist,b = template1_givenlist.split(', "',1)
            
        
        #print(template1_body_head)
        #print(template1_condition)
        #print(template1_givenlist)  
        
        #2
        template2_body_head,template2_body_size=b.strip().split(',',1)
        template2_body_head = template2_body_head.strip()[0:len(template2_body_head)-1]
        template2_body_size = int(template2_body_size.strip())
        #print(template2_body_head)
        #print(template2_body_size)
        return template1_body_head,template1_condition,template1_givenlist,template2_body_head,template2_body_size

    elif (template1==2) and (template2==1):
        #2
        template1_body_head,template1_body_size,b=b.strip().split(',',2)
        template1_body_head = template1_body_head.strip()[1:len(template1_body_head)-1]
        template1_body_size = int(template1_body_size.strip())
        #print(template1_body_head)
        #print(template1_body_size)


        #1
        template2_body_head,template2_condition,template2_givenlist=b.strip().split(',',2)
        template2_body_head = template2_body_head.strip()[1:len(template2_body_head)-1]
        if len(template2_condition)>1:
            template2_condition = template2_condition.strip()[1:len(template2_condition)-1]
        else:
            template2_condition=str(1)
        template2_givenlist=template2_givenlist.strip()
        template2_givenlist = template2_givenlist.strip()
        
        #print(template2_body_head)
        #print(template2_condition)
        #print(template2_givenlist)  
        return template1_body_head,template1_body_size,template2_body_head,template2_condition,template2_givenlist
        
    elif (template1==2) and (template2==2):
        template1_body_head,template1_body_size,b=b.strip().split(',',2)
        template1_body_head = template1_body_head.strip()[1:len(template1_body_head)-1]
        template1_body_size = int(template1_body_size.strip())
        #print(template1_body_head)
        #print(template1_body_size)
        
        template2_body_head,template2_body_size=b.strip().split(',',2)
        template2_body_head = template2_body_head.strip()[1:len(template2_body_head)-1]
        template2_body_size = int(template2_body_size.strip())
        #print(template2_body_head)
        #print(template2_body_size)
        return template1_body_head,template1_body_size,template2_body_head,template2_body_size