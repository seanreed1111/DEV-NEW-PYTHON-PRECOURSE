### !challenge

* type: local-snippet
* language: javascript
* id: 49586ccf-27da-4265-abb8-7ba92a2202cc
* title: isLessThan30.md

### !question

Write a function called "isLessThan30".
Given a number, "isLessThan30" returns whether the given number is less than 30.

```
var output = isLessThan30(9);
console.log(output); // --> true
```

### !end-question

### !placeholder

```js
function isLessThan30(num) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("isLessThan30", function() {
  it("should return a boolean", function() {
    expect(typeof isLessThan30(40)).to.deep.eq("boolean");
  });
  it("should return true for a number less than 30", function() {
    expect(isLessThan30(4)).to.deep.eq(true);
  });
  it("should return false for a number greater than 30", function() {
    expect(isLessThan30(400)).to.deep.eq(false);
  });
  it("should return false for the number 30", function() {
    expect(isLessThan30(30)).to.deep.eq(false);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
