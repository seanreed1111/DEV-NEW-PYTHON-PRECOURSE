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
def isOldEnoughToDrinkAndDrive(age)
  # your code here
    pass

```

### !end-placeholder

### !tests

```python

# describe("isOldEnoughToDrinkAndDrive", function() {
#   it("should return a boolean", function() {
#     expect(typeof isOldEnoughToDrinkAndDrive(19)).to.deep.eq("boolean");
#   });
#   it("should return false", function() {
#     expect(isOldEnoughToDrinkAndDrive(99999)).to.deep.eq(false);
#   });
# });

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
