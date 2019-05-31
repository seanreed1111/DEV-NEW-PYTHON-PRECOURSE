### !challenge

* type: local-snippet
* language: javascript
* id: a5d9e27b-ea2f-4134-ad30-ef9366b3c761
* title: addToFrontOfNew.md

### !question

Write a function called "addToFrontOfNew".

Given an array and an element, "addToFrontOfNew" returns a new array containing all the elements of the given array, with the given element added to the front.

Important: It should be a NEW array instance, not the original array instance.

```
var input = [1, 2];
var output = addToFrontOfNew(input, 3);
console.log(output); // --> [3, 1, 2];
console.log(input); --> [1, 2]
```

### !end-question

### !placeholder

```js
function addToFrontOfNew(arr, element) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("addToFrontOfNew", function() {
  it("should return an array", function() {
    expect(Array.isArray(addToFrontOfNew([1, 2], 3))).to.deep.eq(true);
  });
  it("should add an element to the end of an array", function() {
    expect(addToFrontOfNew([1, 2], 3)).to.deep.eq([3, 1, 2]);
  });
  it("should add an element to the end of an empty array", function() {
    expect(addToFrontOfNew([], 3)).to.deep.eq([3]);
  });
  it("should leave arr unmodified", function() {
    var originalArray = [1, 2];
    var newArray = addToFrontOfNew(originalArray, 3);
    expect(originalArray).to.deep.eq([1, 2]);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
