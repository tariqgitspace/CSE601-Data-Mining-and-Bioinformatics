import numpy as np
import time
from datetime import datetime

number_Records=0
inputDataWithoutDisease=[]
disease_dict={}
confidence_threshold=70
support_Threshold=50
text_file = 'associationruletestdata.txt'

def getConfidenece(rule,body):
    global number_Records
    global confidence_threshold
    numerator = 0.0
    denominator = 0.0
    headlList = list(sorted(set(rule)-set(body)))
    for record in range (number_Records):
        isRecordValid=True
        for element in body:
            parameter = int(element[0:3])
            up_down_disease = element[4:]
            if up_down_disease == "Up":
                if (inputDataWithoutDisease[record][parameter-1]) == 0:
                    isRecordValid=False ##Goto next record
                    break
            elif up_down_disease == "Down":
                if (inputDataWithoutDisease[record][parameter-1]) == 1:
                    isRecordValid=False ##Goto next record
                    break
            elif  (inputDataWithoutDisease[record][parameter-1]) != disease_dict[up_down_disease]:
                isRecordValid=False ##Goto next record
                break
        if(isRecordValid==True):
            denominator += 1.0
        else:
            continue
        isRecordValid=True
        for element in headlList:
            parameter = int(element[0:3])
            up_down_disease = element[4:]
            if up_down_disease == "Up":
                if (inputDataWithoutDisease[record][parameter-1]) == 0:
                    isRecordValid=False ##Goto next record
                    break
            elif up_down_disease == "Down":
                if (inputDataWithoutDisease[record][parameter-1]) == 1:
                    isRecordValid=False ##Goto next record
                    break
            elif  (inputDataWithoutDisease[record][parameter-1]) != disease_dict[up_down_disease]:
                isRecordValid=False ##Goto next record
                break
        if(isRecordValid==True):
            numerator += 1.0
    #print("denominator : " + str(denominator) + "numerator : "+ str(numerator))
    
    if((numerator/denominator)*100 >= confidence_threshold) :
        return True
    else:
        return False
    
def checkIfInFrequent_LastStep(Aftermerge,length,unsupported_list_from_previous_iteration):
    #return True
    for prev in unsupported_list_from_previous_iteration:
        commonList = list(set(Aftermerge).intersection(prev))
        if len(commonList)==(length-1):
            print("Infrequent from previois Interation")
            return False
            
    
    return True
    
def apriori():
    global number_Records
    global inputDataWithoutDisease
    global disease_dict
    global support_Threshold
    global text_file
    inputDataWithoutDisease = []
    
    number_of_paramters_of_record =0
    number_Records=0
    allDiseases = []
    with open(text_file,'r') as f:
        for line in f:
            number_Records = number_Records +1
            values=[]
            values = line.split('\t')
            disease = values[-1].strip()
            allDiseases.append(disease)
            values = values[:-1]
            number_of_paramters_of_record = len(values)
            
            for index, item in enumerate(values):
                if item == "Down":
                    values[index]=0
                elif item == "Up":
                    values[index]=1
                else:
                    print("Bhakk Saala")
                    
            inputDataWithoutDisease.append(values)
            
    inputDataWithoutDisease = np.array(inputDataWithoutDisease)

    
    ##these columns are extra added
    dieasesSet = sorted(set(allDiseases))  
    disease_list = list(dieasesSet)
    
    
    disease_dict = {}
    for name in disease_list:
        disease_dict[name] = disease_list.index(name)

    #print(disease_dict)
    
    X0 = np.zeros((number_Records,1))
    inputDataWithoutDisease = np.hstack((inputDataWithoutDisease,X0))
    
    record_idx =0
    for x in allDiseases:
        inputDataWithoutDisease[record_idx][number_of_paramters_of_record]= disease_dict[x]
        record_idx = record_idx + 1
        
   
    
    length =1
    final_list=[]
    list_at_any_index=[]
    
    support_list_of_this_iteration=[]
    unsupported_list_from_previous_iteration=[]
    unsupported_list_of_this_iteration=[]
    
    for i in range(number_of_paramters_of_record):
        list_at_any_index=[]
        num ='{num:03d}'.format(num=(i+1))
        num = str(num)
        list_at_any_index.append(num+"_Down")
        final_list.append(list_at_any_index)
        list_at_any_index=[]
        list_at_any_index.append(str(num+"_Up"))
        final_list.append(list_at_any_index)

    final_list = sorted(final_list)
    #add disease Column
    number_of_paramters_of_record =number_of_paramters_of_record + 1

    
    for x in disease_list:
        list_at_any_index=[]
        num ='{num:03d}'.format(num=(number_of_paramters_of_record))
        num = str(num)
        list_at_any_index.append(num+"_"+str(x))
        final_list.append(list_at_any_index)
        
        
        
    #print(final_list)
    #print(inputDataWithoutDisease)


    answer =[]
    
    while (length <= number_of_paramters_of_record):
        support_list_of_this_iteration=[]
        unsupported_list_of_this_iteration=[]
        #print("start")
        for current_list in final_list:  ##Pick one comination
            count=0
            for record in range (number_Records):
                isRecordValid=True
                for element in current_list:
                    parameter = int(element[0:3])
                    up_down_disease = element[4:]
                    if up_down_disease == "Up":
                        if (inputDataWithoutDisease[record][parameter-1]) == 0:
                            isRecordValid=False ##Goto next record
                            break
                    elif up_down_disease == "Down":
                        if (inputDataWithoutDisease[record][parameter-1]) == 1:
                            isRecordValid=False ##Goto next record
                            break
                    elif  (inputDataWithoutDisease[record][parameter-1]) != disease_dict[up_down_disease]:
                        isRecordValid=False ##Goto next record
                        break
                if(isRecordValid==True):
                    count=count+1
                    if(count  >= support_Threshold):
                        break
            if(count < support_Threshold):
                unsupported_list_of_this_iteration.append(current_list)
            else:
                support_list_of_this_iteration.append(current_list)
                
    
        if(len(support_list_of_this_iteration)==0):
            print("No Supported Cominations of length equal and greater than " + str(length))
            break
        print("Supported Combinations of size "+str(length) + "  "+ str(len(support_list_of_this_iteration)))
        answer.append(support_list_of_this_iteration)
        final_list =[]
        length = length + 1
        
        unmatched=False
        if length!=2:
            for element1_idx, element1 in enumerate(support_list_of_this_iteration):
                    for element2_idx in range(element1_idx+1, len(support_list_of_this_iteration)):
                        element2 = support_list_of_this_iteration[element2_idx]
                        for i in range(length-2):
                            if element1[i]!=element2[i]:
                                unmatched=True
                                break
                        if unmatched:
                            unmatched=False
                            continue
                        Aftermerge = []
                        Aftermerge = list(sorted(set(element1+element2)))  ##sorted to detect and remove duplicates
                        
                        if checkIfInFrequent_LastStep(Aftermerge,length,unsupported_list_from_previous_iteration):
                            final_list.append(Aftermerge)
                        
        else:
            for element1_idx, element1 in enumerate(support_list_of_this_iteration):
                for element2_idx in range(element1_idx+1, len(support_list_of_this_iteration)):
                    element2 = support_list_of_this_iteration[element2_idx]
                    final_list.append(element1+element2)

        ##remove duplicates
        final_list = set(tuple(x) for x in final_list)  ##Convert to set to remove duplicated
        final_list = list(tuple(x) for x in final_list) ####Convert back to list
        
        #print("Possible combinations of size "+str(length) + "  "+ str(len(final_list)))
        
        if(len(final_list)==0):
            print("No Cominations of length and after" + str(length))
            break
        
        #print(final_list)
        unsupported_list_from_previous_iteration = unsupported_list_of_this_iteration
    #print("return answer")
    return answer

def startexecution():
    start_time = datetime.now()
    #print("--- %start seconds ---" + str(start_time))
    answer = apriori()
    #print("--- %sstop seconds ---"+ str( datetime.now()))
    return answer

if __name__=="__main__":
    startexecution()

    