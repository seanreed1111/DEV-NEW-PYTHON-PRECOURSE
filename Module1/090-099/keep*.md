### !challenge

* type: local-snippet
* language: javascript
* id: 93c14e61-6f43-4158-848c-268271807a39
* title: keep*.md

### !question

Write a function called "keep".

Given an array and a keeper element, "keep" returns an array containing the items that match the given keeper element.

Notes:
* If no elements match, "keep" should return an empty array.

```
var output = keep([1, 2, 3, 2, 1], 2)
console.log(output); --> [2, 2]
```

### !end-question

### !placeholder

```js
function keep(array, keeper) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("keep", function() {
  it("should return an array", function() {
    expect(Array.isArray(keep(["there", "it", "is", "there"]))).to.deep.eq(true);
  });
  it("returns an array with all strings matching 'kept'", function() {
    expect(keep(["there", "it", "is", "there"], "there")).to.deep.eq(["there", "there"]);
  });
  it("returns an array with all numbers matching 'kept'", function() {
    expect(keep([1, 2, 4, 3, 1, 4], 4)).to.deep.eq([4, 4]);
  });
  it("returns an array with all booleans matching 'kept'", function() {
    expect(keep([true, true, true, false, true], true)).to.deep.eq([true, true, true, true]);
  });
  it("returns an emtpy array when no elements match 'kept'", function() {
    expect(keep([true, true, true, false, true], 4)).to.deep.eq([]);
  });
  it("returns an emtpy array when given an empty array", function() {
    expect(keep([], 4)).to.deep.eq([]);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
