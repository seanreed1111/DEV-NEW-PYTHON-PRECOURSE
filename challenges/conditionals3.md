# Conditionals 3

### !challenge

* type: code-snippet
* language: python3.6
* id: a5f1e64f-3419-4259-9304-ea54969381ca
* title: isLessThan

### !question

Write a function called "isLessThan".
Given 2 numbers, "isLessThan" returns whether num2 is less than num1.

```python
output = isLessThan(9, 4)
print(output) # --> True
```


### !end-question

### !placeholder

```python
def isLessThan(num1, num2):
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
        # it should return a boolean
        self.assertIs(type(main.isLessThan(0,10)), msg="it should return a boolean")

    def test2(self):
        #it should return whether num2 is less than num1
        for num1 in range(10):
            for num2 in range(10):
                with self.subTest(num1=num1, num2=num2):
                    self.assertTrue(main.isLessThan(num1,num2), msg="it should return True if num2 is less than num1")

    def test3(self):
        #it should return False if the numbers are equal
        for num in range(10):
                with self.subTest(num=num):
                    self.assertFalse(main.isLessThan(num,num), msg="it should return False if the numbers are equal")

```

<!--
```js

describe("isLessThan", function():it("should return a boolean", function():expect(typeof isLessThan(40, 30)).to.deep.eq("boolean")
  )
  it("should return whether num2 is less than num1", function():expect(isLessThan(20, 200)).to.deep.eq(False)
  )
  it("should return False if the numbers are equal", function():expect(isLessThan(20, 20)).to.deep.eq(False)
  )
)

``` -->

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
### !challenge

* type: local-snippet
* language: javascript
* id: 4fa4323d-3abd-4206-ba59-91c3df97203f
* title: isGreaterThan

### !question

Write a function called "isGreaterThan".
Given 2 numbers, "isGreaterThan" returns whether num2 is greater than num1.

```
var output = isGreaterThan(11, 10);
console.log(output); // --> false
```

### !end-question

### !placeholder

```js
function isGreaterThan(num1, num2) {
  // your code here

}
```

### !end-placeholder

### !tests

```js

describe("isGreaterThan", function() {
  it("should return a boolean", function() {
    expect(typeof isGreaterThan(40, 30)).to.deep.eq("boolean");
  });
  it("should return whether num2 is greater than num1", function() {
    expect(isGreaterThan(20, 200)).to.deep.eq(true);
  });
  it("should return false if the numbers are equal", function() {
    expect(isGreaterThan(20, 20)).to.deep.eq(false);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: local-snippet
* language: javascript
* id: 9d6af24e-85e1-441c-a10c-d629d6381469
* title: isEqualTo

### !question

Write a function called "isEqualTo".
Given 2 numbers, "isEqualTo" returns whether num2 is equal to num1.

```
var output = isEqualTo(11, 10);
console.log(output); // --> false
```

### !end-question

### !placeholder

```js
function isEqualTo(num1, num2) {
  // your code here

}
```

### !end-placeholder

### !tests

```js

describe("isEqualTo", function() {
  it("should return a boolean", function() {
    expect(typeof isEqualTo(40, 30)).to.deep.eq("boolean");
  });
  it("should return false if num2 is greater than num1", function() {
    expect(isEqualTo(20, 200)).to.deep.eq(false);
  });
  it("should return false if num2 is less than num1", function() {
    expect(isEqualTo(20, 2)).to.deep.eq(false);
  });
  it("should return true if the numbers are equal", function() {
    expect(isEqualTo(20, 20)).to.deep.eq(true);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: local-snippet
* language: javascript
* id: 32135330-a5c2-49cd-b9a4-cffe41db64b3
* title: isEven

### !question

Write a function called "isEven".
Given a number, "isEven" returns whether it is even.

```
var output = isEven(11);
console.log(output); // --> false
```

### !end-question

### !placeholder

```js
function isEven(num) {
  // your code here

}
```

### !end-placeholder

### !tests

```js

describe("isEven", function() {
  it("should return a boolean", function() {
    expect(typeof isEven(40)).to.deep.eq("boolean");
  });
  it("should return if the number is even", function() {
    expect(isEven(8)).to.deep.eq(true);
  });
  it("should return true if the number is 0", function() {
    expect(isEven(0)).to.deep.eq(true);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
