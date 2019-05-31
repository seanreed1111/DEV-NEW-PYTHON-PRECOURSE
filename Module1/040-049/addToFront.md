### !challenge

* type: local-snippet
* language: javascript
* id: 81d6b24b-5a97-408c-9681-c698da6881f6
* title: addToFront.md

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
