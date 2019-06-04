### !challenge

* type: local-snippet
* language: javascript
* id: 37a022e4-9104-4ac9-b68b-b63377dd3cb8
* title: getLengthOfTwoWords.md

### !question

Write a function called "getLengthOfTwoWords".
Given 2 words, "getLengthOfTwoWords" returns the sum of their lengths.

```
var output = getLengthOfTwoWords('some', 'words');
console.log(output); // --> 9
```

### !end-question

### !placeholder

```js
function getLengthOfTwoWords(word1, word2) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("getLengthOfTwoWords", function() {
  it("should return a number", function() {
    expect(typeof getLengthOfTwoWords("two", "words")).to.deep.eq("number");
  });
  it("should return the sum length of two words", function() {
    expect(getLengthOfTwoWords("one", "two")).to.deep.eq(6)
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
