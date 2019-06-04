### !challenge

* type: local-snippet
* language: javascript
* id: e094a4bd-4b1a-4a9d-847b-634336385767
* title: computeAverageLengthOfWords.md

### !question

Write a function called "computeAverageLengthOfWords".

Given two words, "computeAverageLengthOfWords" returns the average of their lengths.

```
var output = computeAverageLengthOfWords('code', 'programs');
console.log(output); // --> 6
```

### !end-question

### !placeholder

```js
function computeAverageLengthOfWords(word1, word2) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("computeAverageLengthOfWords", function() {
  it("should return a number", function() {
    expect(typeof computeAverageLengthOfWords("these", "words")).to.deep.eq("number");
  });
  it("should return the average length of the two words", function() {
    expect(computeAverageLengthOfWords("is", "this")).to.deep.eq(3);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
