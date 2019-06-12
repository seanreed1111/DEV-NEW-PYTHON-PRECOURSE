### !challenge

* type: local-snippet
* language: javascript
* id: f606fc41-1d59-4fa5-8d68-d95dfd88a02e
* title: filterOddLengthWords*.md

### !question

Write a function called "filterOddLengthWords".

Given an array of string, "filterOddLengthWords" returns an array containing only the elements of the given array whose lengths are odd numbers.

```
var output = filterOddLengthWords(['there', 'it', 'is', 'now']);
console.log(output); // --> ['there', "now']
```

### !end-question

### !placeholder

```js
function filterOddLengthWords(words) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("filterOddLengthWords", function() {
  it("should return an array", function() {
    expect(Array.isArray(filterOddLengthWords(["there", "it", "is", "now"]))).to.deep.eq(true);
  });
  it("should return an array with odd lengthed words", function() {
    expect(filterOddLengthWords(["there", "it", "is", "now"])).to.deep.eq(["there", "now"]);
  });
  it("should return an empty array when passed an array with no odd lengthed words", function() {
    expect(filterOddLengthWords(["it", "cats"])).to.deep.eq([]);
  });
  it("should return an empty array when passed an empty array", function() {
    expect(filterOddLengthWords([])).to.deep.eq([]);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
