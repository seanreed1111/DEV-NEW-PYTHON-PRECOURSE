### !challenge

* type: local-snippet
* language: javascript
* id: 6a2a074c-7652-488e-b51c-0a441fa0fae9
* title: average.md

### !question

Write a function called "average".

Given two numbers, "average" returns their average.

```
var output = average(4, 6);
console.log(output); // --> 5
```

### !end-question

### !placeholder

```js
function average(num1, num2) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("average", function() {
  it("should return a number", function() {
    expect(typeof average(1, 12)).to.deep.eq("number");
  });
  it("should return the average of two numbers", function() {
    expect(average(2, 4)).to.deep.eq(3);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
