# Math 5

### !challenge

* type: local-snippet
* language: javascript
* id: 5daa1fba-b275-4f89-a5f5-fafd4f9604d1
* title: calculateBillTotal

### !question

Write a function called "calculateBillTotal".

Given the pre tax and pre tip amount of a meal, "calculateBillTotal" returns the total amount due after tax and tip.

Notes:
* Assume that sales tax is 9.5% and tip is 15%.
* Do NOT tip on the sales tax, only on the pre tip amount.

```
var output = calculateBillTotal(20);
console.log(output); // --> 24.9
```

### !end-question

### !placeholder

```js
function calculateBillTotal(preTaxAndTipAmount) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("calculateBillTotal", function() {
  it("should return a number", function() {
    expect(typeof calculateBillTotal(20)).to.deep.eq("number");
  });
  it("should return the bill total, incuding tax and tip", function() {
    expect(calculateBillTotal(20)).to.deep.eq(24.9);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
