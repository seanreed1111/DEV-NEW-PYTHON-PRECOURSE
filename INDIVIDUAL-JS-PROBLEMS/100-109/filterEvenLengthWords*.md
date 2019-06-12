### !challenge

* type: local-snippet
* language: javascript
* id: 1beb59a5-644c-4508-922f-4d8b4910bf77
* title: filterEvenLengthWords*.md

### !question

Write a function called "filterEvenLengthWords".

Given an array of strings, "filterEvenLengthWords" returns an array containing only the elements of the given array whose length is an even number.

```
var output = filterEvenLengthWords(['word', 'words', 'word', 'words']);
console.log(output); // --> ['word', 'word']
```

### !end-question

### !placeholder

```js
function filterEvenLengthWords(words) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("filterEvenLengthWords", function() {
  it("should return an array", function() {
    expect(Array.isArray(filterEvenLengthWords(["there", "it", "is", "now"]))).to.deep.eq(true);
  });
  it("should return an array with even lengthed words", function() {
    expect(filterEvenLengthWords(["there", "it", "is", "now"])).to.deep.eq(["it", "is"]);
  });
  it("should return an empty array when passed an array with no even lengthed words", function() {
    expect(filterEvenLengthWords(["there", "now"])).to.deep.eq([]);
  });
  it("should return an empty array when passed an empty array", function() {
    expect(filterEvenLengthWords([])).to.deep.eq([]);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
