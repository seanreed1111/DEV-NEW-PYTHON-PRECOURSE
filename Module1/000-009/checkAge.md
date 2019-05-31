### !challenge

* type: code-snippet
* language: python3.6
* id: UUID
* title: checkAge.md

### !question

Write a function called "checkAge".
Given a person's name and age, "checkAge" returns one of two messages:
"Go home, insert_name_here!", if they are younger than 21.
"Welcome, insert_name_here!", if they are 21 or older.
Naturally, replace "insert_name_here" with the given name. :)

```python
output = checkAge('Adrian', 22)
print(output); # --> 'Welcome, Adrian!'
```

### !end-question

### !placeholder

```python
def checkAge(name, age)
    #your code here
    pass


```

### !end-placeholder

### !tests

```python

# describe("checkAge", function() {
#   it("should return a string", function() {
#     expect(typeof(checkAge("Dan", "24"))).to.deep.eq("string");
#   });
#   it("should welcome someone over 21", function() {
#     expect(checkAge("Dan", "24")).to.deep.eq("Welcome, Dan!");
#   });
#   it("should welcome a 21 year old", function() {
#     expect(checkAge("Toni", "21")).to.deep.eq("Welcome, Toni!");
#   });
#   it("should bounce someone under 21", function() {
#     expect(checkAge("Rad", "4")).to.deep.eq("Go home, Rad!");
#   });
# });

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
