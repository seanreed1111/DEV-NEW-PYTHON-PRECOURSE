# Advanced 7

### !challenge

* type: local-snippet
* language: javascript
* id: 8bf521f7-88bd-47f1-a173-4a0a4d1d8389
* title: isOddWithoutModulo

### !question

Write a function called "isOddWithoutModulo".

Given a number, "isOddWithoutModulo" returns whether the passed in number is odd.

Note:
* It does so without using the modulo operator (%).
* It should work for negative numbers and zero.

```
var output = isOddWithoutModulo(17);
console.log(output); // --> true
```

### !end-question

### !placeholder

```js
function isOddWithoutModulo(num) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("isOddWithoutModulo", function() {
  it("should return a boolean", function() {
    expect(typeof isOddWithoutModulo(40)).to.deep.eq("boolean");
  });
  it("should not use the modulo operator", function() {
    var body = isOddWithoutModulo.toString();
    expect(/%/.test(body)).to.deep.eq(false);
  });
  it("should return true when a number is odd", function() {
    expect(isOddWithoutModulo(41)).to.deep.eq(true);
  });
  it("should return true when a negative number is odd", function() {
    expect(isOddWithoutModulo(-41)).to.deep.eq(true);
  });
  it("should return false when a number is even", function() {
    expect(isOddWithoutModulo(40)).to.deep.eq(false);
  });
  it("should return false when a negative number is even", function() {
    expect(isOddWithoutModulo(-40)).to.deep.eq(false);
  });
  it("should return false when a passed 0", function() {
    expect(isOddWithoutModulo(0)).to.deep.eq(false);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
