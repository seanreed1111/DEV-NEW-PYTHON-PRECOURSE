### !challenge

* type: local-snippet
* language: javascript
* id: 9f1f81f6-8067-40a8-82ce-c9de9c13bcae
* title: isGreaterThanTen.md

### !question

Write a function called "isGreaterThan10".
Given a number, "isGreaterThan10" returns whether the given number is greater than 10.

```
var output = isGreaterThan10(11);
console.log(output); // --> true
```

### !end-question

### !placeholder

```js
function isGreaterThan10(num) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("isGreaterThan10", function() {
  it("should return a boolean", function() {
    expect(typeof isGreaterThan10(40)).to.deep.eq("boolean");
  });
  it("should return false for a number less than 10", function() {
    expect(isGreaterThan10(4)).to.deep.eq(false);
  });
  it("should return true for a number greater than 10", function() {
    expect(isGreaterThan10(40)).to.deep.eq(true);
  });
  it("should return false for the number 10", function() {
    expect(isGreaterThan10(10)).to.deep.eq(false);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
