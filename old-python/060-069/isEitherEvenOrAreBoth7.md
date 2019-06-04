### !challenge

* type: local-snippet
* language: javascript
* id: 1f440059-2dd7-472c-8106-c56fa9f75029
* title: isEitherEvenOrAreBoth7.md

### !question

Write a function called "isEitherEvenOrAreBoth7".

Given two numbers, 'isEitherEvenOrAreBoth7' returns whether at least one of them is even, or, both of them are 7.

```
var output = isEitherEvenOrAreBoth7(3, 7);
console.log(output); // --> false

var output = isEitherEvenOrAreBoth7(2, 3);
console.log(output); // --> true
```

### !end-question

### !placeholder

```js
function isEitherEvenOrAreBoth7(num1, num2) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("isEitherEvenOrAreBoth7", function() {
  it("should return a boolean", function() {
    expect(typeof isEitherEvenOrAreBoth7(40, 3)).to.deep.eq("boolean");
  });
  it("should return true if the first number is even", function() {
    expect(isEitherEvenOrAreBoth7(4, 3)).to.deep.eq(true);
  });
  it("should return true if the second number is even", function() {
    expect(isEitherEvenOrAreBoth7(7, 8)).to.deep.eq(true);
  });
  it("should return true if the both numbers are even", function() {
    expect(isEitherEvenOrAreBoth7(2, 4)).to.deep.eq(true);
  });
  it("should return true if the both numbers are 7", function() {
    expect(isEitherEvenOrAreBoth7(7, 7)).to.deep.eq(true);
  });
  it("should return false if the both numbers are odd and not both 7", function() {
    expect(isEitherEvenOrAreBoth7(7, 3)).to.deep.eq(false);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
