### Usage
```
l_heap1 = LeftishHeap()
for i in random.sample(range(100), 5):
    l_heap1.insert(i)

print(l_heap1)
print("Height of the leftish heap is {}".format(l_heap1.height))

l_heap2 = LeftishHeap()
for i in random.sample(range(100), 5):
    l_heap2.insert(i)

print(l_heap2)
print("Height of the leftish heap is {}".format(l_heap2.height))

l_heap1 += l_heap2

print(l_heap1)
print("Height of the leftish heap is {}".format(l_heap1.height))

```

```
                16               
         _______________        
        |               |       
        23                       
     _______         _______
    |       |       |       |
    36      63
   ___     ___     ___     ___
  |   |   |   |   |   |   |   |
  40

Height of the Leftish heap is 3
        20       
     _______
    |       |
    69      60
   ___     ___
  |   |   |   |
  92  97

Height of the Leftish heap is 2
                16               
         _______________        
        |               |       
        23              20        
     _______         _______
    |       |       |       |
    36      63      69      60
   ___     ___     ___     ___
  |   |   |   |   |   |   |   |
  40              92  97

Height of the Leftish heap is 3


```
