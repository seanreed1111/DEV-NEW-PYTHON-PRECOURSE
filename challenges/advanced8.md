# Advanced 8

### !challenge

* type: local-snippet
* language: javascript
* id: ee922c51-e401-4df2-821c-93a2080342b1
* title: isEvenWithoutModulo

### !question

Write a function called "isEvenWithoutModulo".

Given a number, "isEvenWithoutModulo" returns whether it is even.

Notes:
* It does so without using the modulo operator (%).
* It should work for negative numbers and zero.

```
var output = isEvenWithoutModulo(8);
console.log(output); // --> true
```

### !end-question

### !placeholder

```js
function isEvenWithoutModulo(num) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("isEvenWithoutModulo", function() {
  it("should return a boolean", function() {
    expect(typeof isEvenWithoutModulo(40)).to.deep.eq("boolean");
  });
  it("should not use the modulo operator", function() {
    var body = isEvenWithoutModulo.toString();
    expect(/%/.test(body)).to.deep.eq(false);
  });
  it("should return true when a number is even", function() {
    expect(isEvenWithoutModulo(40)).to.deep.eq(true);
  });
  it("should return true when a negative number is even", function() {
    expect(isEvenWithoutModulo(-40)).to.deep.eq(true);
  });
  it("should return false when a number is odd", function() {
    expect(isEvenWithoutModulo(41)).to.deep.eq(false);
  });
  it("should return false when a negative number is odd", function() {
    expect(isEvenWithoutModulo(-41)).to.deep.eq(false);
  });
  it("should return true when a passed 0", function() {
    expect(isEvenWithoutModulo(0)).to.deep.eq(true);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
