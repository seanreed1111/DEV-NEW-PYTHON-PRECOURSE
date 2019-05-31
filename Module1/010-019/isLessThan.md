### !challenge

* type: local-snippet
* language: javascript
* id: a5f1e64f-3419-4259-9304-ea54969381ca
* title: isLessThan.md

### !question

Write a function called "isLessThan".
Given 2 numbers, "isLessThan" returns whether num2 is less than num1.

```
var output = isLessThan(9, 4);
console.log(output); // --> true
```


### !end-question

### !placeholder

```js
function isLessThan(num1, num2) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("isLessThan", function() {
  it("should return a boolean", function() {
    expect(typeof isLessThan(40, 30)).to.deep.eq("boolean");
  });
  it("should return whether num2 is less than num1", function() {
    expect(isLessThan(20, 200)).to.deep.eq(false);
  });
  it("should return false if the numbers are equal", function() {
    expect(isLessThan(20, 20)).to.deep.eq(false);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
