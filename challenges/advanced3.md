# Advanced 3

### !challenge

* type: code-snippet
* language: python3.6
* id: e7a0d366-b299-4c2a-81ac-45fcbacd2b54
* title: select

### !question

Write a function called "select".

Given list and a dictionary, "select" returns a new dictionary whose keys are  in the given dictionary AND are also present in the given list.

Notes:
* If keys are present in the given list, but are not in the given dict, it should ignore them.
* It does not modify the passed in dict.

```
keys = ['a', 'c', 'e']
input_dict = {a: 1, b: 2, c: 3, d: 4}

output = select(keys, input_dict)
print(output) # --> {'a': 1, 'c': 3}
```

### !end-question

### !placeholder

```python
# your code here



```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):

    def test_0(self):
        # it should return a dictionary
        self.assertIsInstance(main.select(['a', 'c', 'e'],
        {a: 1, b: 2, c: 3, d: 4}), dict,
        msg = 'should return a dictionary')


    def test_1(self):
        # it should return a dictionary with properties from the passed in dict whose keys are present in the given list
        self.assertEqual(main.select(["a", "c", "e"],
        {'a': 11, 'b': 12, 'c': 13, 'd': 14}), {'a': 11, 'c': 13},
        msg = 'should return a dict with properties in from the passed in dict whose keys are present in the given list')


    def test_2(self):
        # it should not modify the passed in dictionary
        obj = {'a': 11, 'b': 12, 'key':'value', 'e':15}
        main.select(["c", "e"], obj)
        self.assertEqual({'a': 11, 'b': 12, 'key':'value', 'e':15}, obj),
        msg = 'should not modify the passed in dictionary')


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
