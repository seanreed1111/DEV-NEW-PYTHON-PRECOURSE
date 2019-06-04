### !challenge

* type: local-snippet
* language: javascript
* id: ebb36275-fc12-4110-8f39-9ef16ac2aeae
* title: getLengthOfThreeWords.md

### !question

Write a function called "getLengthOfThreeWords".

Given 3 words, "getLengthOfThreeWords" returns the sum of their lengths.

```
var output = getLengthOfThreeWords('some', 'other', 'words');
console.log(output); // --> 14
```

### !end-question

### !placeholder

```js
function getLengthOfThreeWords(word1, word2, word3) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("getLengthOfThreeWords", function() {
  it("should return a number", function() {
    expect(typeof getLengthOfThreeWords("three", "random", "words")).to.deep.eq("number");
  });
  it("should return the sum length of three words", function() {
    expect(getLengthOfThreeWords("some", "other", "words")).to.deep.eq(14)
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
