### !challenge

* type: local-snippet
* language: javascript
* id: cbcdeb30-874c-43d4-bf34-efee529c29d9
* title: computeFactorialOfN.md

### !question

Write a function called "computeFactorialOfN".

Given a natural number (a whole number greater than 0), "computeFactorialOfN" returns its factorial.

```
var output = computeFactorialOfN(3);
console.log(output); // --> 6

var output = computeFactorialOfN(4);
console.log(output); // --> 24
```

### !end-question

### !placeholder

```js

function computeFactorialOfN(n) {
  // your code here
}
```

### !end-placeholder

### !tests

```js

describe("computeFactorialOfN", function() {
  it("should return a number", function() {
    expect(typeof computeFactorialOfN(7)).to.deep.eq("number");
  });
  it("should return the factorial of 'n'", function() {
    expect(computeFactorialOfN(4)).to.deep.eq(24);
  });
  it("should return the factorial of 1", function() {
    expect(computeFactorialOfN(1)).to.deep.eq(1);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
