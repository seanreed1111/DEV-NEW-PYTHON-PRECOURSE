### !challenge

* type: local-snippet
* language: javascript
* id: 8c8e3983-9ea7-403f-abaf-4df141fef106
* title: computeSummationToN.md

### !question

Write a function called "computeSummationToN".

Given a number, "computeSummationToN" returns the sum of sequential numbers leading up to the given number, beginning at 0.

Notes:
* If n = 4, it should calculate the sum of 1 + 2 + 3 + 4, and return 10.

```
var output = computeSummationToN(6);
console.log(output); // --> 21
```

### !end-question

### !placeholder

```js
function computeSummationToN(n) {
  // your code here
}
```

### !end-placeholder

### !tests

```js

describe("computeSummationToN", function() {
  it("should return a number", function() {
    expect(typeof computeSummationToN(7)).to.deep.eq("number");
  });
  it("should return the summation of numbers up to and including 'n'", function() {
    expect(computeSummationToN(4)).to.deep.eq(10);
  });
  it("should return the summation of 0", function() {
    expect(computeSummationToN(0)).to.deep.eq(0);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
