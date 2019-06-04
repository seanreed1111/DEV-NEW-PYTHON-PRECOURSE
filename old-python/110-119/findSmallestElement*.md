### !challenge

* type: local-snippet
* language: javascript
* id: 3e9cfffd-1ec6-4243-a91b-4546c2d647aa
* title: findSmallestElement*.md

### !question

Write a function called "findSmallestElement".

Given an array of numbers, "findSmallestElement" returns the smallest number within the given array.

Notes:
* If the given array is empty, it should return 0.

```
var output = findSmallestElement([4, 1, 9, 10]);
console.log(output); // --> 1
```

### !end-question

### !placeholder

```js
function findSmallestElement(arr) {
  // your code here
}
```

### !end-placeholder

### !tests

```js

describe("findSmallestElement", function() {
  it("should return a number", function() {
    expect(typeof findSmallestElement([3, 5, 3, 1])).to.deep.eq("number");
  });
  it("should return the smallest element in an array", function() {
    expect(findSmallestElement([3, 5, 3, 1])).to.deep.eq(1);
  });
  it("should return the smallest element in an array when there are ties", function() {
    expect(findSmallestElement([3, 1, 3, 1, 5])).to.deep.eq(1);
  });
  it("should return the smallest element in an array when they are all negative", function() {
    expect(findSmallestElement([-1, -5, -3])).to.deep.eq(-5);
  });
  it("should return 0 if the array is empty", function() {
    expect(findSmallestElement([])).to.deep.eq(0);
  })
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
