### !challenge

* type: local-snippet
* language: javascript
* id: 39be5abf-26c2-4d8c-be67-116467662bed
* title: multiply.md

### !question

Write a function called "multiply".

Given 2 numbers, "multiply" returns their product.

Notes:
* It should not use the multiply operator - *

```
var output = multiply(4, 7);
console.log(output); // --> 28
```

### !end-question

### !placeholder

```js
function multiply(num1, num2) {
  // your code here
}
```

### !end-placeholder

### !tests

```js

describe("multiply", function() {
  it("should return a number", function() {
    expect(typeof multiply(5, 6)).to.deep.eq("number");
  });
  it("should not use the multiply operator", function() {
    var body = multiply.toString();
    expect(/\*/.test(body)).to.deep.eq(false);
  });
  it("should multiply two numbers", function() {
    expect(multiply(6, 8)).to.deep.eq(48);
  });
  it("should multiply negative numbers", function() {
    expect(multiply(6, -8)).to.deep.eq(-48);
  });
  it("should multiply with the second number as 0", function() {
    expect(multiply(6, 0)).to.deep.eq(0);
  });
  it("should multiply with the first number as 0", function() {
    expect(multiply(0, 10)).to.deep.eq(0);
  });
  it("should multiply negative numbers", function() {
    expect(multiply(-4, -3)).to.deep.eq(12);
  })
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
