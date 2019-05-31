### !challenge

* type: code-snippet
* language: python3.6
* id: UUID
* title: isOldEnoughToDrink.md

### !question

Write a function called "isOldEnoughToDrink".
Given a number, in this case an age, "isOldEnoughToDrink" returns whether a person of this given age is old enough to legally drink in the United States.
Notes:
* The legal drinking age in the United States is 21.

```python
output1 = isOldEnoughToDrink(22)
print(output1) # --> True

output2 = isOldEnoughToDrink(16)
print(output2) # --> False
```

### !end-question

### !placeholder

```python
def isOldEnoughToDrink(age)
    #your code here
    pass
```

### !end-placeholder

### !tests

```python

# describe("isOldEnoughToDrink", function() {
#   it("should return a boolean", function() {
#     expect(typeof isOldEnoughToDrink(40)).to.deep.eq("boolean");
#   });
#   it("should return whether the age is greater than 21", function() {
#     expect(isOldEnoughToDrink(40)).to.deep.eq(true);
#   });
#   it("should return true if the age is 21", function() {
#     expect(isOldEnoughToDrink(21)).to.deep.eq(true);
#   });
# });

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
