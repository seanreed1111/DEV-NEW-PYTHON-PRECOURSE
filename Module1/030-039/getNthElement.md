### !challenge

* type: local-snippet
* language: javascript
* id: 95a46849-2478-44f2-8783-0729dd17eaae
* title: getNthElement.md

### !question

Write a function called "getNthElement".

Given an array and an integer, "getNthElement" returns the element at the given integer, within the given array.

Notes:
* If the array has a length of 0, it should return 'undefined'.

```
var output = getNthElement([1, 3, 5], 1);
console.log(output); // --> 3
```

### !end-question

### !placeholder

```js
function getNthElement(array, n) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("getNthElement", function() {
  it("should return the nth element of an array", function() {
    expect(getNthElement([1, 3, 5], 1)).to.deep.eq(3);
  });
  it("should return undefined if the array is empty", function() {
    expect(getNthElement([], 1)).to.deep.eq(undefined);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
