### !challenge

* type: local-snippet
* language: javascript
* id: 2b052832-2dec-494d-9a24-090c8051db0a
* title: areBothOdd.md

### !question

Write a function called "areBothOdd".

Given 2 numbers, "areBothOdd" returns whether or not both of the given numbers are odd.

```
var output = areBothOdd(1, 3);
console.log(output); // --> true
```

### !end-question

### !placeholder

```js
function areBothOdd(num1, num2) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("areBothOdd", function() {
  it("should return a boolean", function() {
    expect(typeof areBothOdd(40, 3)).to.deep.eq("boolean");
  });
  it("should return true if both numbers are odd", function() {
    expect(areBothOdd(41, 3)).to.deep.eq(true);
  });
  it("should return false if the first number is even", function() {
    expect(areBothOdd(4, 3)).to.deep.eq(false);
  });
  it("should return false if the second number is even", function() {
    expect(areBothOdd(5, 30)).to.deep.eq(false);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
