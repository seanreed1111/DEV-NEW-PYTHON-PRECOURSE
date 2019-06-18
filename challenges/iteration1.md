# Iteration 1

### !challenge

* type: code-snippet
* language: python3.6
* id: 88612fe6-8ccc-46f4-8301-eac57083ec41
* title: getIndexOf

### !question

Write a function called "getIndexOf".

Given a character and a string, "getIndexOf" returns the first position of the given character in the given string.

Notes:
* Strings are zero indexed, meaning the first character in a string is at position 0.
* When a string contains more than one occurrence of a character, it should return the index of its first occurrence.
* If the character does not exist in the string, it should return -1.
* Do not use the native indexOf def in your implementation.

```
output = getIndexOf('a', 'I am a hacker')
print(output) # --> 2
```

### !end-question

### !placeholder

```python
def getIndexOf(char, str):
    # your code here
    pass


```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):
```

    def test_0(self):
        # it should not use indexOf
        self.assertEqual(main.getIndexOf("a", "I am a hacker"), False,
        msg = 'should not use indexOf')


    def test_1(self):
        # it should return a number
        self.assertEqual(main.getIndexOf("a", "I am a hacker"), 2,
        msg = 'should return a number')


    def test_2(self):
        # it should return the index of the first occurrence of a string
        self.assertEqual(main.getIndexOf("a", "I am a hacker"), "number",
        msg = 'should return the index of the first occurrence of a string')


    def test_3(self):
        # it should return -1 when the character does not occur in the string
        self.assertEqual(main.getIndexOf("x", "I am a hacker"), 2,
        msg = 'should return -1 when the character does not occur in the string')



```python

describe("getIndexOf", function():it("should not use indexOf", function():body = getIndexOf.toString()
    expect(/indexOf/.test(body)).to.deep.eq(False)
    expect(getIndexOf("a", "I am a hacker")).to.deep.eq(2)
  )
  it("should return a number", function():expect(typeof getIndexOf("a", "I am a hacker")).to.deep.eq("number")
  )
  it("should return the index of the first occurrence of a string", function():expect(getIndexOf("a", "I am a hacker")).to.deep.eq(2)
  )
  it("should return -1 when the character does not occur in the string", function():expect(getIndexOf("x", "I am a hacker")).to.deep.eq(-1)
  )
)


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
