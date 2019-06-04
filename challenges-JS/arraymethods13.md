# Array Methods 13

### !challenge

* type: local-snippet
* language: javascript
* id: 54143016-2767-47af-9931-408799951ba0
* title: getLargestElement

### !question

Write a function called "getLargestElement".

Given an array, "getLargestElement" returns the largest number in the given array.

Notes:
* It should return 0 if the array is empty.

```
var output = getLargestElement([5, 2, 8, 3]);
console.log(output); // --> 8;
```

### !end-question

### !placeholder

```js
function getLargestElement(arr) {
  // your code here

}
```

### !end-placeholder

### !tests

```js

describe("getLargestElement", function() {
  it("should return a number", function() {
    expect(typeof getLargestElement([3, 5, 3, 1])).to.deep.eq("number");
  });
  it("should return the largest element in an array", function() {
    expect(getLargestElement([3, 5, 3, 1])).to.deep.eq(5);
  });
  it("should return the largest element in an array when there are ties", function() {
    expect(getLargestElement([3, 5, 3, 1, 5])).to.deep.eq(5);
  });
  it("should return the largest element in an array when they are all negative", function() {
    expect(getLargestElement([-1, -5, -3])).to.deep.eq(-1);
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
* id: baa3bc1e-1a67-4a6b-a66a-72cc6e55c8b4
* title: computeSumOfAllElements

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
