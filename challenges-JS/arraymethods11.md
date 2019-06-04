# Array Methods 11

### !challenge

* type: local-snippet
* language: javascript
* id: 3fb77f32-bfa4-46a3-b207-3b7cf58ba011
* title: filterEvenElements

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

### !challenge

* type: local-snippet
* language: javascript
* id: 0c0a6c72-d8a0-488e-a0c7-c3a8df27630f
* title: getLengthOfShortestElement

### !question

Write a function called "getLengthOfShortestElement".

Given an array, "getLengthOfShortestElement" returns the length of the shortest string in the given array.

Notes:
* It should return 0 if the array is empty.

```
var output = getLengthOfShortestElement(['one', 'two', 'three']);
console.log(output); // --> 3
```

### !end-question

### !placeholder

```js
function getLengthOfShortestElement(arr) {
  // your code here

}
```

### !end-placeholder

### !tests

```js

describe("getLengthOfShortestElement", function() {
  it("should return a number", function() {
    expect(typeof getLengthOfShortestElement(["one", "two", "three"])).to.deep.eq("number");
  });
  it("should return the length of the shortest element in an array", function() {
    expect(getLengthOfShortestElement(["one", "four", "three"])).to.deep.eq(3);
  });
  it("it should handle ties", function() {
    expect(getLengthOfShortestElement(["one", "to", "no"])).to.deep.eq(2);
  });
  it("it should return 0 when given an empty array", function() {
    expect(getLengthOfShortestElement([])).to.deep.eq(0);
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
* id: c910016d-56a3-4e65-88d8-01111d85a609
* title: getLongestElement

### !question

Write a function called "getLongestElement".

Given an array, "getLongestElement" returns the longest string in the given array.

Notes:
* If there are ties, it returns the first element to appear.
* If the array is empty, it should return an empty string.

```
var output = getLongestElement(['one', 'two', 'three']);
console.log(output); // --> 'three'
```

### !end-question

### !placeholder

```js
function getLongestElement(arr) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("getLongestElement", function() {
  it("should return a string", function() {
    expect(typeof(getLongestElement(["one", "two", "three"]))).to.deep.eq("string");
  });
  it("should return the longest element in an array", function() {
    expect(getLongestElement(["one", "two", "three"])).to.deep.eq("three");
  });
  it("should return the first longest element in an array when there are ties", function() {
    expect(getLongestElement(["one", "two", "one"])).to.deep.eq("one");
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
