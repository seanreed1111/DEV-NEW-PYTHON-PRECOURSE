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
def isOldEnoughToDrive(age)
    #your code here
    pass


```

### !end-placeholder

### !tests

```python

# describe("isOldEnoughToDrive", function() {
#   it("should return a boolean", function() {
#     expect(typeof isOldEnoughToDrive(40)).to.deep.eq("boolean");
#   });
#   it("should return true if the age is 16", function() {
#     expect(isOldEnoughToDrive(16)).to.deep.eq(true);
#   });
#   it("should return false if the age is less than 16", function() {
#     expect(isOldEnoughToDrive(15)).to.deep.eq(false);
#   });
# });

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
