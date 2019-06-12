### !challenge

* type: local-snippet
* language: javascript
* id: e2ea174d-35c8-441d-9d82-7f2690a30278
* title: addToBack.md

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
