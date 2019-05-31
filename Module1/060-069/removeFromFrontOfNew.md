### !challenge

* type: local-snippet
* language: javascript
* id: 8a97c37b-54f3-4db0-845f-d2e7901e4244
* title: removeFromFrontOfNew.md

### !question

Write a function called "removeFromFrontOfNew".

Given an array, "removeFromFrontOfNew" returns a new array containing all but the first element of the given array.

Notes:
* You should be familiar with the 'slice' method.

```
var arr = [1, 2, 3];
var output = removeFromFrontOfNew(arr);
console.log(output); // --> [2, 3]
console.log(arr); // --> [1, 2, 3]
```

### !end-question

### !placeholder

```js
function removeFromFrontOfNew(arr) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("removeFromFrontOfNew", function() {
  it("should return an array", function() {
    expect(Array.isArray(removeFromFrontOfNew([1, 2]))).to.deep.eq(true);
  });
  it("should remove an element from the front of an array", function() {
    expect(removeFromFrontOfNew([1, 2])).to.deep.eq([2]);
  });
  it("should handle an empty array", function() {
    expect(removeFromFrontOfNew([])).to.deep.eq([]);
  });
  it("should leave arr unmodified", function() {
    var originalArray = [1, 2];
    var newArray = removeFromFrontOfNew(originalArray);
    expect(originalArray).to.deep.eq([1, 2]);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
