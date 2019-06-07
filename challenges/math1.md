# Math 1

### !challenge

* type: code-snippet
* language: python3.6
* id: 6a2a074c-7652-488e-b51c-0a441fa0fae9
* title: average

### !question

Write a function called "average".

Given two numbers, "average" returns their average.

```
output = average(4, 6)
print(output) # --> 5
```

### !end-question

### !placeholder

```python
def average(num1, num2):
    # your code here
    pass

```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):

    def test1(self):
        #it should return the average of two numbers
        for num in range(10):
                with self.subTest(num1 = num, num2 = 3 * num):
                    self.assertEqual(main.average(num1, num2), num1*num2/2,
                    msg = f"#it should return the average of two numbers {num1*num2/2}" )

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
