### !challenge

* type: code-snippet
* language: python3.6
* id: UUID
* title: isOldEnoughToVote.md

### !question

Write a function called "isOldEnoughToVote".
Given a number, in this case an age, 'isOldEnoughToVote' returns whether a person of this given age is old enough to legally vote in the United States.
Notes:
* The legal voting age in the United States is 18.

```python
output = isOldEnoughToVote(22)
print(output) # True
```

### !end-question

### !placeholder

```python
def isOldEnoughToVote(age):
    # your code here
    pass
```

### !end-placeholder

### !tests
```python
import unittest

class TestScript(unittest.TestCase):
    def test1(self):
        # it should return True if the age is 18
        self.assertEqual(isOldEnoughToVote(18),True,"18 is old enough to vote.")

    def test2(self):
        #it should return False if the age is less than 18
        self.assertEqual(isOldEnoughToVote(15),True,"15 is not old enough to vote.")

    def test3(self):
        #it should return True if the age is greater than 18
        self.assertEqual(isOldEnoughToVote(25),True,"25 is old enough to vote.")
```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
