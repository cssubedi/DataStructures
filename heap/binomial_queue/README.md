### Usage
```
b_queue1 = BinomialQueue()
for i in range(15):
    b_queue1.insert(i)

b_queue1.delete_min()
print(b_queue1)

b_queue2 = BinomialQueue()
for i in range(-10, -1):
    b_queue2.insert(i)

b_queue2 += b_queue1
print(b_queue2)

```

```
None

2   
|   
|   
3   

4       
|___    
|   |   
5   6   
    |   
    |   
    7   

1               
|_______        
|   |   |       
14  12  8         
    |   |___    
    |   |   |   
    13  9   10    
            |   
            |   
            11   


-2   

2   
|   
|   
3   

4       
|___    
|   |   
5   6   
    |   
    |   
    7   

None

-10                               
|_______________                
|   |   |       |               
-9  -8  -6      1                  
    |   |___    |_______        
    |   |   |   |   |   |       
    -7  -5  -4  14  12  8            
            |       |   |___    
            |       |   |   |   
            -3      13  9   10     
                            |   
                            |   
                            11

```
