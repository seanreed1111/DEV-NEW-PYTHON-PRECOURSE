# Array Methods 4

### !challenge

* type: local-snippet
* language: javascript
* id: 879c0dc1-12a5-4dad-876a-5f698f0dbe05
* title: getAllElementsButFirst

### !question

Write a function called "getAllElementsButFirst".

Given an array, "getAllElementsButFirst" returns an array with all the elements but the first.

```
var input = [1, 2, 3, 4];
var output = getAllElementsButFirst(input);
console.log(output); // --> [2, 3, 4]
```

### !end-question

### !placeholder

```js
function getAllElementsButFirst(array) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("getAllElementsButFirst", function() {
  it("should return an array", function() {
    expect(Array.isArray(getAllElementsButFirst([4, 5, 6]))).to.deep.eq(true);
  });
  it("should return an array with all the elements of the passed in array, except for the first", function() {
    expect(getAllElementsButFirst([4, 5, 6])).to.deep.eq([5, 6]);
  });
  it("should return an empty array when passed in a single element array", function() {
    expect(getAllElementsButFirst([4])).to.deep.eq([]);
  });
  it("should return an empty array when passed in an empty array", function() {
    expect(getAllElementsButFirst([])).to.deep.eq([]);
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
* id: 1662f5c1-43d4-4cbe-8a0e-2c6866408de5
* title: getAllElementsButLast

### !question

Write a function called "getAllElementsButLast".

Given an array, "getAllElementsButLast" returns an array with all the elements but the last.

```
var input = [1, 2, 3, 4];
var output = getAllElementsButLast(input);
console.log(output); // --> [1, 2 , 3]
```

### !end-question

### !placeholder

```js
function getAllElementsButLast(array) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("getAllElementsButLast", function() {
  it("should return an array", function() {
    expect(Array.isArray(getAllElementsButLast([4, 5, 6]))).to.deep.eq(true);
  });
  it("should return an array with all the elements of the passed in array, except for the last", function() {
    expect(getAllElementsButLast([4, 5, 6])).to.deep.eq([4, 5]);
  });
  it("should return an empty array when passed in a single element array", function() {
    expect(getAllElementsButLast([4])).to.deep.eq([]);
  });
  it("should return an empty array when passed in an empty array", function() {
    expect(getAllElementsButLast([])).to.deep.eq([]);
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
* id: 94f66a0e-795b-439b-bb69-c12c78b475b0
* title: removeFromFront

### !question

Write a function called "removeFromFront".

Given an array, "removeFromFront" returns the given array with its first element removed.

Notes:
* You should be familiar with the method 'shift'.

```
var output = removeFromFront([1, 2, 3]);
console.log(output); // --> [2, 3]
```

### !end-question

### !placeholder

```js
function removeFromFront(arr) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("removeFromFront", function() {
  it("should return an array", function() {
    expect(Array.isArray(removeFromFront([1, 2, 3]))).to.deep.eq(true);
  });
  it("should return the array with the first element removed", function() {
    expect(removeFromFront([1, 2])).to.deep.eq([2]);
  });
  it("should handle an empty array", function() {
    expect(removeFromFront([])).to.deep.eq([]);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
