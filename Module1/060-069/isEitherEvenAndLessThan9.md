### !challenge

* type: local-snippet
* language: javascript
* id: 45e91a10-4d74-4f10-83ef-b7b065d45830
* title: isEitherEvenAndLessThan9.md

### !question

Write a function called "isEitherEvenAndLessThan9".

Given two numbers, 'isEitherEvenAndLessThan9' returns whether at least one of them is even, and, both of them are less than 9.

```
var output = isEitherEvenAndLessThan9(2, 4);
console.log(output); // --> true

var output = isEitherEvenAndLessThan9(72, 2);
console.log(output); // --> false
```

### !end-question

### !placeholder

```js
function isEitherEvenAndLessThan9(num1, num2) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("isEitherEvenAndLessThan9", function() {
  it("should return a boolean", function() {
    expect(typeof isEitherEvenAndLessThan9(40, 3)).to.deep.eq("boolean");
  });
  it("should return true if the first number is even and both are less than 9", function() {
    expect(isEitherEvenAndLessThan9(4, 3)).to.deep.eq(true);
  });
  it("should return true if the second number is even and both are less than 9", function() {
    expect(isEitherEvenAndLessThan9(7, 8)).to.deep.eq(true);
  });
  it("should return true if the both numbers are even and both are less than 9", function() {
    expect(isEitherEvenAndLessThan9(2, 4)).to.deep.eq(true);
  });
  it("should return false if the both numbers are greater than 9", function() {
    expect(isEitherEvenAndLessThan9(72, 32)).to.deep.eq(false);
  });
  it("should return false if the first number is greater than 9", function() {
    expect(isEitherEvenAndLessThan9(72, 2)).to.deep.eq(false);
  });
  it("should return false if the second number is greater than 9", function() {
    expect(isEitherEvenAndLessThan9(2, 20)).to.deep.eq(false);
  });
  it("should return false if neither is even", function() {
    expect(isEitherEvenAndLessThan9(3, 5)).to.deep.eq(false);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
