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
                with self.subTest(num = num):
                    self.assertEqual(main.average(num, num*3), 2 * num,
                    msg = "it should return the average of two numbers" )

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: bb88d243-fda0-4b49-ba45-f4a19ead5d03
* title: computeAreaOfATriangle

### !question

Write a function called "computeAreaOfATriangle".

Given the base and height of a triangle, "computeAreaOfATriangle" returns its area.

```
output = computeAreaOfATriangle(4, 6)
print(output) # --> 12
```

### !end-question

### !placeholder

```python
def computeAreaOfATriangle(base, height):
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
        #it should return the area of a triangle
        for num in range(1,10):
                with self.subTest(num):
                    self.assertEqual(main.computeAreaOfATriangle(num, num + 4),
                    num * (num + 4) / 2,
                    msg = "it should return the return the area of a triangle" )
```


### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 327a2860-4858-4627-9632-f451e415e7d4
* title: cube

### !question

Write a function called "cube".

Given a number, "cube" returns the cube of that number.

```
output = cube(3)
print(output) # --> 27
```

### !end-question

### !placeholder

```python
def cube(num):
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
        #it should cube negative, positive, and zero
        for num in range(-5,5):
                with self.subTest(num):
                    self.assertEqual(main.cube(num),
                    num * num * num,
                    msg = "it should cube zero, negative numbers, and positive numbers")
```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 1d51ed19-4978-4574-bb07-9b65921ed07e
* title: square

### !question

Write a function called "square".

Given a number, "square" should return the square of the given number.

```
output = square(5)
print(output) # --> 25
```

### !end-question

### !placeholder

```python
def square(num):
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
        #it should square negative numbers, positive numbers, and zero
        for num in range(-5,5):
                with self.subTest(num):
                    self.assertEqual(main.square(num),
                    num * num,
                    msg = "it should square negative numbers, positive numbers, and zero")
```


### !end-tests

### !explanation

### !end-explanation

### !end-challenge
