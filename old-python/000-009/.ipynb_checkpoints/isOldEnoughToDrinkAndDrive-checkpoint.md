### !challenge

* type: code-snippet
* language: python3.6
* id: UUID
* title: isOldEnoughToDrinkAndDrive.md

### !question

Write a function called "isOldEnoughToDrinkAndDrive".
Given a number, in this case an age, "isOldEnoughToDrinkAndDrive" returns whether a person of this given age is old enough to legally drink and drive in the United States.
Notes:
* The legal drinking age in the United States is 21.
* It is always illegal to drink and drive in the United States.

```python
output = isOldEnoughToDrinkAndDrive(22)
print(output)# --> False
```

### !end-question

### !placeholder

```python
def isOldEnoughToDrinkAndDrive(self,age):
  # your code here
    pass

```

### !end-placeholder

### !tests

```python
import unittest
import main

class TestScript(unittest.TestCase):
    def test1(self):
    # it should always return False
    self.assertEqual(main.isOldEnoughToDrinkAndDrive(99),False,"99 is not old enough to drink and drive.")

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
