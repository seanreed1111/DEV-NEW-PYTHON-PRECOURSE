### !challenge

* type: local-snippet
* language: javascript
* id: 17849d44-37ff-4fde-a81f-884838cdb8f5
* title: or.md

### !question

Write a function called "or".

Given 2 boolean expressions, "or" returns true or false, corresponding to the '||' operator.
Notes:
* Do not use the || operator.
* Use ! and && operators instead.

```
var output = or(true, false);
console.log(output); // --> true;
```

### !end-question

### !placeholder

```js
function or(expression1, expression2) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("or", function() {
  it("should not use the logical OR operator", function() {
    var body = or.toString()
    expect(/\|\|/.test(body)).to.deep.eq(false);
  });
  it("should return a boolean", function() {
    expect(typeof or(true, true)).to.deep.eq("boolean");
  });
  it("should return true if the first value is true", function() {
    expect(or(true, false)).to.deep.eq(true);
  });
  it("should return true if the second value is true", function() {
    expect(or(false, true)).to.deep.eq(true);
  });
  it("should return true both values are true", function() {
    expect(or(true, true)).to.deep.eq(true);
  });
  it("should return false both values are false", function() {
    expect(or(false, false)).to.deep.eq(false);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
