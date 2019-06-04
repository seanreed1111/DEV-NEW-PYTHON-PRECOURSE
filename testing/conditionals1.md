# Conditionals 1

### !challenge

* type: local-snippet
* language: python3.6
* id: aa5deeb1-c053-4c31-90e7-4a5fb0546afa
* title: isOldEnoughToDrink

### !question

Write a function called "isOldEnoughToDrink".
Given a number, in this case an age, "isOldEnoughToDrink" returns whether a person of this given age is old enough to legally drink in the United States.
Notes:
* The legal drinking age in the United States is 21.

```
output = isOldEnoughToDrink(22)
print(output) # --> true
```

### !end-question

### !placeholder

```python
defisOldEnoughToDrink(age) :
    # your code here
    pass
  

```

### !end-placeholder

### !tests

```python
import unittest

class TestScript(unittest.TestCase):
    def test1(self):
        # it {} 
        pass

    def test2(self):
        #it {}
        pass

    def test3(self):
        #it {}
        pass
```


```python

describe("isOldEnoughToDrink", function() :it("should return a boolean", function() :expect(typeof isOldEnoughToDrink(40)).to.deep.eq("boolean")
  )
  it("should return whether the age is greater than 21", function() :expect(isOldEnoughToDrink(40)).to.deep.eq(true)
  )
  it("should return true if the age is 21", function() :expect(isOldEnoughToDrink(21)).to.deep.eq(true)
  )
  it("should return false if the age is 20", function() :expect(isOldEnoughToDrink(20)).to.deep.eq(false)
  )
)

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: local-snippet
* language: python3.6
* id: 4b181e05-9f6d-4e2d-beaa-ad80ab8d3c26
* title: isOldEnoughToDrive

### !question

Write a function called "isOldEnoughToDrive".
Given a number, in this case an age, "isOldEnoughToDrive" returns whether a person of this given age is old enough to legally drive in the United States.
Notes:
* The legal driving age in the United States is 16.

```
output = isOldEnoughToDrive(22)
print(output) # --> true
```

### !end-question

### !placeholder

```python
defisOldEnoughToDrive(age) :
    # your code here
    pass
  

```

### !end-placeholder

### !tests

```python
import unittest

class TestScript(unittest.TestCase):
    def test1(self):
        # it {} 
        pass

    def test2(self):
        #it {}
        pass

    def test3(self):
        #it {}
        pass
```


```python

describe("isOldEnoughToDrive", function() :it("should return a boolean", function() :expect(typeof isOldEnoughToDrive(40)).to.deep.eq("boolean")
  )
  it("should return true if the age is 16", function() :expect(isOldEnoughToDrive(16)).to.deep.eq(true)
  )
  it("should return false if the age is less than 16", function() :expect(isOldEnoughToDrive(15)).to.deep.eq(false)
  )
)

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: local-snippet
* language: python3.6
* id: 8aa5586d-36c6-4677-bd29-bbadd91027b8
* title: isOldEnoughToVote

### !question

Write a function called "isOldEnoughToVote".
Given a number, in this case an age, 'isOldEnoughToVote' returns whether a person of this given age is old enough to legally vote in the United States.
Notes:
* The legal voting age in the United States is 18.

```
output = isOldEnoughToVote(22)
print(output) # --> true
```

### !end-question

### !placeholder

```python
defisOldEnoughToVote(age) :
    # your code here
    pass
  

```

### !end-placeholder

### !tests

```python
import unittest

class TestScript(unittest.TestCase):
    def test1(self):
        # it {} 
        pass

    def test2(self):
        #it {}
        pass

    def test3(self):
        #it {}
        pass
```


```python

describe("isOldEnoughToVote", function() :it("should return a boolean", function() :expect(typeof isOldEnoughToVote(40)).to.deep.eq("boolean")
  )
  it("should return whether the age is greater than 18", function() :expect(isOldEnoughToVote(40)).to.deep.eq(true)
  )
  it("should return true if the age is 18", function() :expect(isOldEnoughToVote(18)).to.deep.eq(true)
  )
)

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: local-snippet
* language: python3.6
* id: 4031a186-73da-4384-95c9-8d8510aa67a9
* title: isOldEnoughToDrinkAndDrive

### !question

Write a function called "isOldEnoughToDrinkAndDrive".
Given a number, in this case an age, "isOldEnoughToDrinkAndDrive" returns whether a person of this given age is old enough to legally drink and drive in the United States.
Notes:
* The legal drinking age in the United States is 21.
* It is always illegal to drink and drive in the United States.

```
output = isOldEnoughToDrinkAndDrive(22)
print(output) # --> false
```

### !end-question

### !placeholder

```python
defisOldEnoughToDrinkAndDrive(age) :
    # your code here
    pass
  

```

### !end-placeholder

### !tests

```python
import unittest

class TestScript(unittest.TestCase):
    def test1(self):
        # it {} 
        pass

    def test2(self):
        #it {}
        pass

    def test3(self):
        #it {}
        pass
```


```python

describe("isOldEnoughToDrinkAndDrive", function() :it("should return a boolean", function() :expect(typeof isOldEnoughToDrinkAndDrive(19)).to.deep.eq("boolean")
  )
  it("should return false", function() :expect(isOldEnoughToDrinkAndDrive(99999)).to.deep.eq(false)
  )
)

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
