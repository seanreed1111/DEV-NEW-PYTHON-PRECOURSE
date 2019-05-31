### !challenge

* type: local-snippet
* language: javascript
* id: bc26b616-3099-4e47-ad75-5670968a8ed1
* title: filterOddElements*.md

### !question

Write a function called "filterOddElements".

Given an array of numbers, "filterOddElements" returns an array containing only the odd numbers of the given array.
```
var output = filterOddElements([1, 2, 3, 4, 5]);
console.log(output); // --> [1, 3, 5]
```

### !end-question

### !placeholder

```js
function filterOddElements(arr) {
  // your code here
}
```

### !end-placeholder

### !tests

```js

describe("filterOddElements", function() {
  it("should return an array", function() {
    expect(Array.isArray(filterOddElements([1, 2, 3, 4]))).to.deep.eq(true);
  });
  it("should return an array with the odd elements from the passed in array", function() {
    expect(filterOddElements([1, 2, 3, 4, 5])).to.deep.eq([1, 3, 5]);
  });
  it("should return an array if there are no odd numbers", function() {
    expect(filterOddElements([2, 4, 6])).to.deep.eq([]);
  });
  it("should return an array if given an emtpy array", function() {
    expect(filterOddElements([])).to.deep.eq([]);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
