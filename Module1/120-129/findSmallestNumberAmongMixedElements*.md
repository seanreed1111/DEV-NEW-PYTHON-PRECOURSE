### !challenge

* type: local-snippet
* language: javascript
* id: 0bbe947d-3174-4fe2-98c4-1a84331477d7
* title: findSmallestNumberAmongMixedElements*.md

### !question

Write a function called "findSmallestNumberAmongMixedElements".

Given an array of mixed elements, "findSmallestNumberAmongMixedElements" returns the smallest number within the given array.

Notes:
* If the given array is empty, it should return 0.
* If the array contains no numbers, it should return 0.

```
var output = findSmallestNumberAmongMixedElements([4, 'lincoln', 9, 'octopus']);
console.log(output); // --> 4
```

### !end-question

### !placeholder

```js
function findSmallestNumberAmongMixedElements(arr) {
  // your code here
}
```

### !end-placeholder

### !tests

```js


describe("findSmallestNumberAmongMixedElements", function() {
  it("should return a number", function() {
    expect(typeof findSmallestNumberAmongMixedElements([3, 5, 3, 1])).to.deep.eq("number");
  });
  it("should return the smallest element in an array", function() {
    expect(findSmallestNumberAmongMixedElements([3, "word", 5, "up", 3, 1])).to.deep.eq(1);
  });
  it("should return the smallest element in an array when there are ties", function() {
    expect(findSmallestNumberAmongMixedElements(["word", 3, 1, 3, "wordy", "up", 1, 5])).to.deep.eq(1);
  });
  it("should return the smallest element in an array when they are all negative", function() {
    expect(findSmallestNumberAmongMixedElements([-1, -5, "word", -3])).to.deep.eq(-5);
  });
  it("should return 0 when the array is empty", function() {
    expect(findSmallestNumberAmongMixedElements([])).to.deep.eq(0);
  });
  it("should return 0 when there are no numbers", function() {
    expect(findSmallestNumberAmongMixedElements(["word", "up"])).to.deep.eq(0);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
