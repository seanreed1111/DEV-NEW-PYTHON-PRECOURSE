# Array Methods 2

### !challenge

* type: local-snippet
* language: javascript
* id: 81d6b24b-5a97-408c-9681-c698da6881f6
* title: addToFront

### !question

Write a function called "addToFront".

Given an array and an element, "addToFront" adds the given element to the front of the given array, and returns the given array.

Notes:
* It should be the SAME array, not a new array.

```
var output = addToFront([1, 2], 3);
console.log(output); // -> [3, 1, 2]
```

### !end-question

### !placeholder

```js
function addToFront(arr, element) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("addToFront", function() {
  it("should return an array", function() {
    expect(Array.isArray(addToFront([1, 2], 3))).to.deep.eq(true);
  });

  it("addToFront should add an element to the beginning of an array", function() {
    expect(addToFront([1, 2], 3)).to.deep.eq([3, 1, 2]);
  });

  it("should add an element to the beginning of an empty array", function() {
    expect(addToFront([], 3)).to.deep.eq([3]);
  });

  it("should be the same array instance that was passed in", function() {
    var input = [1, 2, 3];
    expect(addToFront(input, 4)).to.deep.eq(input);
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
* id: e2ea174d-35c8-441d-9d82-7f2690a30278
* title: addToBack

### !question

Write a function called "addToBack".

Given an array and an element, "addToBack" returns the given array with the given element added to the end.

Note: It should be the SAME array, not a new array.

```
var output = addToBack([1, 2], 3);
console.log(output); // -> [1, 2, 3]
```

### !end-question

### !placeholder

```js
function addToBack(arr, element) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("addToBack", function() {
  it("should return an array", function() {
    expect(Array.isArray(addToBack([1, 2], 3))).to.deep.eq(true);
  });

  it("should add an element to the end of an array", function() {
    expect(addToBack([1, 2], 3)).to.deep.eq([1, 2, 3]);
  });

  it("should add an element to the end of an empty array", function() {
    expect(addToBack([], 3)).to.deep.eq([3]);
  });

  it("should be the same array instance that was passed in", function() {
    var input = [1, 2, 3];
    expect(addToBack(input, 4)).to.deep.eq(input);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
