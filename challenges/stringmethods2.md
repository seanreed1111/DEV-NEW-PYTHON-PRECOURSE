# String Methods 2

### !challenge

* type: code-snippet
* language: python3.6
* id: e094a4bd-4b1a-4a9d-847b-634336385767
* title: computeAverageLengthOfWords

### !question

Write a function called "computeAverageLengthOfWords".

Given two words, "computeAverageLengthOfWords" returns the average of their lengths.

```
output = computeAverageLengthOfWords('code', 'programs')
print(output) # --> 6
```

### !end-question

### !placeholder

```python
def computeAverageLengthOfWords(word1, word2):
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
        #it should return the average length of the two words
        self.assertEqual(computeAverageLengthOfWords('code', 'programs'), 6,
        msg = "it should return the average length of the two words" )


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
