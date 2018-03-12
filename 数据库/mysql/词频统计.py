# -*- coding:utf-8 -*-  
  
word_lst = []  
word_dict= {}  
with open('jibingmc.txt') as wf:
    for word in wf:
       word_lst.append(word.split(',')) 
       for item in word_lst:
           for item2 in item:
               if item2 not in word_dict:
                    word_dict[item2] = 1 
                     
               else:  
                    word_dict[item2] += 1   
               
                  
with open("word.txt",'w') as wf2:
    for key in word_dict:
        print key,word_dict[key]  
        wf2.write(key+' '+str(word_dict[key])+'\n') 
wf.close()        
wf2.close()   

第二种方法
用liux系统
cat jibingmc.txt' |python map.py|sort|python reduce.py
   
            
        
        
  

      
    

