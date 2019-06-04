# Math 6

### !challenge

* type: local-snippet
* language: javascript
* id: 2cbdc32a-d1bb-4538-9dcb-eb64072cae56
* title: computeCompoundInterest

### !question

Write a function called "computeCompoundInterest".

Given a principal, an interest rate, a compounding frequency, and a time (in years), "computeCompoundInterest" returns the amount of compound interest generated.

```
var output = computeCompoundInterest(1500, .043, 4, 6);
console.log(output); // --> 438.8368221341061
```

Reference:
https://en.wikipedia.org/wiki/Compound_interest#Calculation_of_compound_interest
This shows the formula used to calculate the total compound interest generated.

### !end-question

### !placeholder

```js

function computeCompoundInterest(principal, interestRate, compoundingFrequency, timeInYears) {
  // your code here

}
```

### !end-placeholder

### !tests

```js

describe("computeCompoundInterest", function() {
  it("should return a number", function() {
    expect(typeof computeCompoundInterest(1500, .043, 4, 6)).to.deep.eq("number");
  });
  it("should return the amount of compound interest generated", function() {
    expect(computeCompoundInterest(1500, .043, 4, 6).toFixed(4)).to.deep.eq(438.8368221341061.toFixed(4));
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
