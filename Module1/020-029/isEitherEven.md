### !challenge

* type: local-snippet
* language: javascript
* id: 2aa4cdd8-0158-438d-8a53-b9c0283226c7
* title: isEitherEven.md

### !question

Write a function called "isEitherEven".

Given two numbers, "isEitherEven" returns whether or not either one of the given numbers is even.

```
var output = isEitherEven(1, 4);
console.log(output); // --> true
```

### !end-question

### !placeholder

```js
function isEitherEven(num1, num2) {
  // your code here
   

   
}

```

### !end-placeholder

### !tests

```js

describe("isEitherEven", function() {
  it("should return a boolean", function() {
    expect(typeof isEitherEven(40, 3)).to.deep.eq("boolean");
  });
  it("should return true if the first number is even", function() {
    expect(isEitherEven(4, 3)).to.deep.eq(true);
  });
  it("should return true if the second number is even", function() {
    expect(isEitherEven(7, 30)).to.deep.eq(true);
  });
  it("should return true if the both numbers are even", function() {
    expect(isEitherEven(70, 30)).to.deep.eq(true);
  });
  it("should return false if both numbers are odd", function() {
    expect(isEitherEven(71, 31)).to.deep.eq(false);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
