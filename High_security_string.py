   
def getStrength(password, weight_a):
    # Complete the function
    alphalist = list('abcdefghijklmnopqrstuvwxyz')
    
    #dic_weights = [(weight_a+i) for i in range(26)]

    dic_weights = []

    my_sum = 0

    for i in range(26):
    	if (weight_a+i)<=25:
    		dic_weights.append(weight_a+i)
    	else:
    		dic_weights.append(my_sum)
    		my_sum+=1

    
    
    #mapper function to get the dictionary
    
    my_dic = dict(zip(alphalist,dic_weights))
    
    print(my_dic)

    sum_strength_pass = 0
    
    for i in password.lower():
    	print(i,my_dic[i])
    	sum_strength_pass += my_dic.get(i)
        
    return  sum_strength_pass


print(getStrength('hackerrank',10))    
