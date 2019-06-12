### !challenge

* type: local-snippet
* language: javascript
* id: 3fb77f32-bfa4-46a3-b207-3b7cf58ba011
* title: filterEvenElements*.md

### !question

Write a function called "filterEvenElements".

Given an array of numbers, "filterEvenElements" returns an array containing only the even numbers of the given array.
```
var output = filterEvenElements([2, 3, 4, 5, 6]);
console.log(output); // --> [2, 4, 6]
```

### !end-question

### !placeholder

```js
function filterEvenElements(arr) {
  // your code here
}
```

### !end-placeholder

### !tests

```js

describe("filterEvenElements", function() {
  it("should return an array", function() {
    expect(Array.isArray(filterEvenElements([1, 2, 3, 4]))).to.deep.eq(true);
  });
  it("should return an array with the even elements from the passed in array", function() {
    expect(filterEvenElements([1, 2, 3, 4, 5])).to.deep.eq([2, 4]);
  });
  it("should return an array if there are no even numbers", function() {
    expect(filterEvenElements([1, 3, 5])).to.deep.eq([]);
  });
  it("should return an array if given an emtpy array", function() {
    expect(filterEvenElements([])).to.deep.eq([]);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
