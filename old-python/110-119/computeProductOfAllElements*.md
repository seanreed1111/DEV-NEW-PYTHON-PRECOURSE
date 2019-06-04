### !challenge

* type: local-snippet
* language: javascript
* id: e2f51369-1a84-42dc-8613-2ccd23f46bc2
* title: computeProductOfAllElements*.md

### !question

Write a function called "computeProductOfAllElements".

Given an array of numbers, "computeProductOfAllElements" returns the products of all the elements in the given array.

Notes:
* If given array is empty, it should return 0.

```
var output = computeProductOfAllElements([2, 5, 6]);
console.log(output); // --> 60
```

### !end-question

### !placeholder

```js
function computeProductOfAllElements(arr) {
  // your code here
}
```

### !end-placeholder

### !tests

```js

describe("computeProductOfAllElements", function() {
  it("should return a number", function() {
    expect(typeof computeProductOfAllElements([1, 2, 4])).to.deep.eq("number");
  });
  it("return the product of all elements", function() {
    expect(computeProductOfAllElements([1, 2, 4])).to.deep.eq(8);
  });
  it("return 0 if the passed in array is empty", function() {
    expect(computeProductOfAllElements([])).to.deep.eq(0);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
