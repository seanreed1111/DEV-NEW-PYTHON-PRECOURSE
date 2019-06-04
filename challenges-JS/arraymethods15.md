# Array Methods 15

### !challenge

* type: local-snippet
* language: javascript
* id: 4f89dd25-b751-49fe-9fa9-fe8c368c1a7c
* title: findShortestWordAmongMixedElements

### !question

Write a function called "findShortestWordAmongMixedElements".

Given an array, "findShortestWordAmongMixedElements" returns the shortest string within the given array.

Notes:
* If there are ties, it should return the first element to appear in the given array.
* Expect the given array to have values other than strings.
* If the given array is empty, it should return an empty string.
* If the given array contains no strings, it should return an empty string.

```
var output = findShortestWordAmongMixedElements([4, 'two', 2, 'three']);
console.log(output); // --> 'two'
```

### !end-question

### !placeholder

```js

function findShortestWordAmongMixedElements(arr) {
  // your code here

}
```

### !end-placeholder

### !tests

```js


describe("findShortestWordAmongMixedElements", function() {
  it("should return a string", function() {
    expect(typeof findShortestWordAmongMixedElements(["these", "are", "strings"])).to.deep.eq("string");
  });
  it("should return the shortest string in an array", function() {
    expect(findShortestWordAmongMixedElements([3, "word", 5, "up", 3, 1])).to.deep.eq("up");
  });
  it("should return the shortest string in an array that appears first when there are ties", function() {
    expect(findShortestWordAmongMixedElements(["word", 3, 5, 3, "yo", "up", 1, 5])).to.deep.eq("yo");
  });
  it("should return an empty string when the array is empty", function() {
    expect(findShortestWordAmongMixedElements([])).to.deep.eq("");
  });
  it("should return an empty string there are no strings", function() {
    expect(findShortestWordAmongMixedElements([1, 2, 4])).to.deep.eq("");
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: local-snippet
* language: javascript
* id: 0bbe947d-3174-4fe2-98c4-1a84331477d7
* title: findSmallestNumberAmongMixedElements

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
