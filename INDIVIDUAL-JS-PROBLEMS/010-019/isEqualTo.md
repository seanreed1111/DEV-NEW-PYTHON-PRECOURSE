### !challenge

* type: local-snippet
* language: javascript
* id: 9d6af24e-85e1-441c-a10c-d629d6381469
* title: isEqualTo.md

### !question

Write a function called "isEqualTo".
Given 2 numbers, "isEqualTo" returns whether num2 is equal to num1.

```
var output = isEqualTo(11, 10);
console.log(output); // --> false
```

### !end-question

### !placeholder

```js
function isEqualTo(num1, num2) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("isEqualTo", function() {
  it("should return a boolean", function() {
    expect(typeof isEqualTo(40, 30)).to.deep.eq("boolean");
  });
  it("should return false if num2 is greater than num1", function() {
    expect(isEqualTo(20, 200)).to.deep.eq(false);
  });
  it("should return false if num2 is less than num1", function() {
    expect(isEqualTo(20, 2)).to.deep.eq(false);
  });
  it("should return true if the numbers are equal", function() {
    expect(isEqualTo(20, 20)).to.deep.eq(true);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
