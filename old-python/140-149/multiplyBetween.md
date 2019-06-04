### !challenge

* type: local-snippet
* language: javascript
* id: 49c67b68-aa6f-4fc6-a5b9-f1de6a3c8079
* title: multiplyBetween.md

### !question

Write a function called "multiplyBetween".

Given 2 integers, "multiplyBetween" returns the product between the two given integers, beginning at num1, and excluding num2.

Notes:
* The product between 1 and 4 is 1 * 2 * 3 = 6.
* If num2 is not greater than num1, it should return 0.
```
var output = multiplyBetween(2, 5);
console.log(output); // --> 24
```

### !end-question

### !placeholder

```js
function multiplyBetween(num1, num2) {
  // your code here
}
```

### !end-placeholder

### !tests

```js

describe("multiplyBetween", function() {
  it("should return a number", function() {
    expect(typeof multiplyBetween(4, 8)).to.deep.eq("number");
  });
  it("should multiply between the first and second number exclusive", function() {
    expect(multiplyBetween(4, 6)).to.deep.eq(20);
  });
  it("should multiply between the first and second number when they are one number apart", function() {
    expect(multiplyBetween(4, 5)).to.deep.eq(4);
  });
  it("should multiply between the first and second number exclusive with negatives", function() {
    expect(multiplyBetween(-5, -3)).to.deep.eq(20);
  });
  it("should return 0 if the second number is less than the first", function() {
    expect(multiplyBetween(1, -3)).to.deep.eq(0);
  });
  it("should return 0 if the 2 numbers are equal", function() {
    expect(multiplyBetween(1, 1)).to.deep.eq(0);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
