### !challenge

* type: local-snippet
* language: javascript
* id: 5fc75a18-76e2-4e35-afac-e8433908ea84
* title: removeElement*.md

### !question

Write a function called "removeElement".

Given an array of elements, and a "discarder" parameter, "removeElement" returns an array containing the items in the given array that do not match the "discarder" parameter.

Notes:
* If all the elements match, it should return an empty array.
* If an empty array is passed in, it should return an empty array.

```
var output = removeElement([1, 2, 3, 2, 1], 2);
console.log(output); // --> [1, 3, 1]
```

### !end-question

### !placeholder

```js
function removeElement(array, discarder) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("removeElement", function() {
  it("should return an array", function() {
    expect(Array.isArray(removeElement(["there", "it", "is", "there"]))).to.deep.eq(true);
  });
  it("return an array with all strings not matching 'discarder'", function() {
    expect(removeElement(["there", "it", "is", "there"], "there")).to.deep.eq(["it", "is"]);
  });
  it("return an array with all numbers not matching 'discarder'", function() {
    expect(removeElement([1, 2, 4, 3, 1, 4], 4)).to.deep.eq([1, 2, 3, 1]);
  });
  it("return an array with all booleans not matching 'discarder'", function() {
    expect(removeElement([true, true, true, false, true], true)).to.deep.eq([false]);
  });
  it("return an emtpy array when all elements match 'discarder'", function() {
    expect(removeElement([true, true, true, true], true)).to.deep.eq([]);
  });
  it("return an emtpy array when given an empty array", function() {
    expect(removeElement([], 4)).to.deep.eq([]);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
