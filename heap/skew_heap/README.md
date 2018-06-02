### Usage
```
s_heap1 = SkewHeap()
for i in random.sample(range(100), 5):
    s_heap1.insert(i)

print(s_heap1)
print("Height of the Skew heap is {}".format(s_heap1.height))

s_heap2 = SkewHeap()
for i in random.sample(range(100), 5):
    s_heap2.insert(i)

print(s_heap2)
print("Height of the Skew heap is {}".format(s_heap2.height))

s_heap1 += s_heap2

print(s_heap1)
print("Height of the Skew heap is {}".format(s_heap1.height))

```
```
        34       
     _______    
    |       |   
    41      59    
   ___     ___  
  |   |   |   |
  78      80      

Height of the Skew heap is 2
        0       
     _______    
    |       |   
    52      41    
   ___     ___  
  |   |   |   |
  76      67      

Height of the Skew heap is 2
                                0                               
                 _______________________________                
                |                               |               
                34                              52                
         _______________                 _______________        
        |               |               |               |       
        41              41              76                         
     _______         _______         _______         _______    
    |       |       |       |       |       |       |       |   
    59      67      78                                             
   ___     ___     ___     ___     ___     ___     ___     ___  
  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
  80                                                             

Height of the Skew heap is 4

```
