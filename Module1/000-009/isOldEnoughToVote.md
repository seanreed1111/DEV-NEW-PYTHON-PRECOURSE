### !challenge

* type: code-snippet
* language: python3.6
* id: UUID
* title: isOldEnoughToVote.md

### !question

Write a function called "isOldEnoughToVote".
Given a number, in this case an age, 'isOldEnoughToVote' returns whether a person of this given age is old enough to legally vote in the United States.
Notes:
* The legal voting age in the United States is 18.

```python
output = isOldEnoughToVote(22)
print(output) # True
```

### !end-question

### !placeholder

```python
def isOldEnoughToVote(age)
    # your code here
    pass
```

### !end-placeholder

### !tests

```python

# describe("isOldEnoughToVote", function() {
#   it("should return a boolean", function() {
#     expect(typeof isOldEnoughToVote(40)).to.deep.eq("boolean");
#   });
#   it("should return whether the age is greater than 18", function() {
#     expect(isOldEnoughToVote(40)).to.deep.eq(true);
#   });
#   it("should return true if the age is 18", function() {
#     expect(isOldEnoughToVote(18)).to.deep.eq(true);
#   });
# });

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
