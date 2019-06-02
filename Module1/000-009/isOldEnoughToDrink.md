### !challenge

* type: code-snippet
* language: python3.6
* id: UUID
* title: isOldEnoughToDrink.md

### !question

Write a function called "isOldEnoughToDrink".
Given a number, in this case an age, "isOldEnoughToDrink" returns whether a person of this given age is old enough to legally drink in the United States.
Notes:
* The legal drinking age in the United States is 21.

```python
output1 = isOldEnoughToDrink(22)
print(output1) # --> True

output2 = isOldEnoughToDrink(16)
print(output2) # --> False
```

### !end-question

### !placeholder

```python
def isOldEnoughToDrink(self, age):
    #your code here
    pass
```

### !end-placeholder

### !tests

```python

import unittest
import main

class TestScript(unittest.TestCase):
    
    def test1(self):
        # #it should return False for age < 21
        self.assertEqual(main.isOldEnoughToDrink(11), False, "11 is not old enough to drink.")
        
    def test2(self):
        #it should return True for age = 21
        self.assertEqual(main.isOldEnoughToDrink(21), True, "21 is old enough to drink.")

    def test3(self):
        #it should return True for age > 21
        self.assertEqual(main.isOldEnoughToDrink(50), True, "50 is old enough to drink.")
 
```


### !end-tests

### !explanation

### !end-explanation

### !end-challenge
