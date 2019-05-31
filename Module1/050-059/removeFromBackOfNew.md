### !challenge

* type: local-snippet
* language: javascript
* id: 241a37de-4069-418a-8f8d-64a40cc74f49
* title: removeFromBackOfNew.md

### !question

Write a function called "removeFromBackOfNew".

Given an array, "removeFromBackOfNew" returns a new array containing all but the last element of the given array.

Notes:
* You should be familiar with the 'slice' method.

```
var arr = [1, 2, 3];
var output = removeFromBackOfNew(arr);
console.log(output); // --> [1, 2]
console.log(arr); // --> [1, 2, 3]
```

### !end-question

### !placeholder

```js
function removeFromBackOfNew(arr) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("removeFromBackOfNew", function() {
  it("should return an array", function() {
    expect(Array.isArray(removeFromBackOfNew([1, 2], 3))).to.deep.eq(true);
  });
  it("should return an array with the last element of the passed in array removed", function() {
    expect(removeFromBackOfNew([1, 2])).to.deep.eq([1]);
  });
  it("should handle an empty array", function() {
    expect(removeFromBackOfNew([])).to.deep.eq([]);
  });
  it("should leave arr unmodified", function() {
    var originalArray = [1, 2];
    var newArray = removeFromBackOfNew(originalArray);
    expect(originalArray).to.deep.eq([1, 2]);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
