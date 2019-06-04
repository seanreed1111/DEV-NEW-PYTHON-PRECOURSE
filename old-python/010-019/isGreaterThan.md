### !challenge

* type: local-snippet
* language: javascript
* id: 4fa4323d-3abd-4206-ba59-91c3df97203f
* title: isGreaterThan.md

### !question

Write a function called "isGreaterThan".
Given 2 numbers, "isGreaterThan" returns whether num2 is greater than num1.

```
var output = isGreaterThan(11, 10);
console.log(output); // --> false
```

### !end-question

### !placeholder

```js
function isGreaterThan(num1, num2) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("isGreaterThan", function() {
  it("should return a boolean", function() {
    expect(typeof isGreaterThan(40, 30)).to.deep.eq("boolean");
  });
  it("should return whether num2 is greater than num1", function() {
    expect(isGreaterThan(20, 200)).to.deep.eq(true);
  });
  it("should return false if the numbers are equal", function() {
    expect(isGreaterThan(20, 20)).to.deep.eq(false);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
