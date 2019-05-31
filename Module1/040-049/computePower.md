### !challenge

* type: local-snippet
* language: javascript
* id: bf41eed3-a9de-4e31-9750-a645da0ab576
* title: computePower.md

### !question

Write a function called "computePower".

Given a number and an exponent, "computePower" returns the given number, raised to the given exponent.

```
var output = computePower(2, 3);
console.log(output); // --> 8
```

### !end-question

### !placeholder

```js
function computePower(num, exponent) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("computePower", function() {
  it("should return a number", function() {
    expect(typeof computePower(2, 4)).to.deep.eq("number");
  });
  it("should return a number raised to a given exponent", function() {
    expect(computePower(2, 4)).to.deep.eq(16);
  });
  it("should return a negative number raised to a given exponent", function() {
    expect(computePower(-2, 4)).to.deep.eq(16);
  });
  it("should return a number raised to 0", function() {
    expect(computePower(-2, 0)).to.deep.eq(1);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
