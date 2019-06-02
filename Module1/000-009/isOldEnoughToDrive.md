### !challenge

* type: code-snippet
* language: python3.6
* id: UUID
* title: isOldEnoughToDrive.md

### !question

Write a function called "isOldEnoughToDrive".
Given a number, in this case an age, "isOldEnoughToDrive" returns whether a person of this given age is old enough to legally drive in the United States.
Notes:
* The legal driving age in the United States is 16.

```python
output = isOldEnoughToDrive(22)
print(output) # --> True
```

### !end-question

### !placeholder

```python
def isOldEnoughToDrive(age):
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
        # it should return True if the age is 16
        self.assertEqual(main.isOldEnoughToDrive(16),True,"16 is old enough to drive.")

    def test2(self):
        #it should return False if the age is less than 16
        self.assertEqual(main.isOldEnoughToDrive(15),True,"15 is not old enough to drive.")

    def test3(self):
        #it should return True if the age is greater than 16
        self.assertEqual(main.isOldEnoughToDrive(25),True,"25 is old enough to drive.")

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
