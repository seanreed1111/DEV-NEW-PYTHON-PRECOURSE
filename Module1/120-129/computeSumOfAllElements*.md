### !challenge

* type: local-snippet
* language: javascript
* id: baa3bc1e-1a67-4a6b-a66a-72cc6e55c8b4
* title: computeSumOfAllElements*.md

### !question

Write a function called "computeSumOfAllElements".

Given an array of numbers, "computeSumOfAllElements" returns the sum of all the elements in the given array.

```
var output = computeSumOfAllElements([1, 2, 3])
console.log(output); // --> 6
```

### !end-question

### !placeholder

```js
function computeSumOfAllElements(arr) {
  // your code here
}
```

### !end-placeholder

### !tests

```js

describe("computeSumOfAllElements", function() {
  it("should return a number", function() {
    expect(typeof computeSumOfAllElements([1, 2, 4])).to.deep.eq("number");
  });
  it("return the sum of all elements", function() {
    expect(computeSumOfAllElements([1, 2, 4])).to.deep.eq(7);
  });
  it("return 0 if the passed in array is empty", function() {
    expect(computeSumOfAllElements([])).to.deep.eq(0);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
