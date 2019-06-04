### !challenge

* type: local-snippet
* language: javascript
* id: 52e8002f-f926-4b68-b70b-c41fe566ba8c
* title: addToBackOfNew.md

### !question

Write a function called "addToBackNew".

Given an array and an element, "addToBackNew" returns a clone of the given array, with the given element added to the end.

Important: It should be a NEW array instance, not the original array instance.

```
var input = [1, 2];
var output = addToBackOfNew(input, 3);
console.log(input); // --> [1, 2]
console.log(output); // --> [1, 2, 3]
```

### !end-question

### !placeholder

```js
function addToBackOfNew(arr, element) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("addToBackOfNew", function() {
  it("should return an array", function() {
    expect(Array.isArray(addToBackOfNew([1, 2], 3))).to.deep.eq(true);
  });
  it("should add an element to the end of an array", function() {
    expect(addToBackOfNew([1, 2], 3)).to.deep.eq([1, 2, 3]);
  });
  it("should add an element to the end of an empty array", function() {
    expect(addToBackOfNew([], 3)).to.deep.eq([3]);
  });
  it("should leave arr unmodified", function() {
    var originalArray = [1, 2];
    var newArray = addToBackOfNew(originalArray, 3);
    expect(originalArray).to.deep.eq([1, 2]);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
