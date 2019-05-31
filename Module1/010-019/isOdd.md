### !challenge

* type: local-snippet
* language: javascript
* id: c13afed5-de19-458a-a3b9-65fc3d34f842
* title: isOdd.md

### !question

Write a function called "isOdd".
Given a number, "isOdd" returns whether the given number is odd.

```
var output = isOdd(9);
console.log(output); // --> true
```

### !end-question

### !placeholder

```js
function isOdd(num) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("isOdd", function() {
  it("should return a boolean", function() {
    expect(typeof isOdd(40)).to.deep.eq("boolean");
  });
  it("should return if the number is odd", function() {
    expect(isOdd(7)).to.deep.eq(true);
  });
  it("should return false if the number is 0", function() {
    expect(isOdd(0)).to.deep.eq(false);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
