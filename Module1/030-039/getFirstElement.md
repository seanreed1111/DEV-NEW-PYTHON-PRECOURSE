### !challenge

* type: local-snippet
* language: javascript
* id: 7c720b84-05ae-44b5-ab40-5ef78db09bec
* title: getFirstElement.md

### !question

Write a function called "getFirstElement".

Given an array, "getFirstElement" returns the first element of the given array.

Notes:
* If the given array has a length of 0, it should return undefined.

```
var output = getFirstElement([1, 2, 3, 4, 5]);
console.log(output); // --> 1
```

### !end-question

### !placeholder

```js
function getFirstElement(array) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js


describe("getFirstElement", function() {
  it("should return the first element of an array", function() {
    expect(getFirstElement([1, 3, 5])).to.deep.eq(1);
  });
  it("should return undefined if the array is empty", function() {
    expect(getFirstElement([])).to.deep.eq(undefined);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
