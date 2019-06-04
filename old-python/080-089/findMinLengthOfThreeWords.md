### !challenge

* type: local-snippet
* language: javascript
* id: 705f1f9a-9afa-4ae7-be40-ddebbb95204b
* title: findMinLengthOfThreeWords.md

### !question

Write a function called "findMinLengthOfThreeWords".

Given 3 words, "findMinLengthOfThreeWords" returns the length of the shortest word.

```
var output = findMinLengthOfThreeWords('a', 'be', 'see');
console.log(output); // --> 1
```

### !end-question

### !placeholder

```js
function findMinLengthOfThreeWords(word1, word2, word3) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("findMinLengthOfThreeWords", function() {
  it("should return a number", function() {
    expect(typeof findMinLengthOfThreeWords("a", "be", "see")).to.deep.eq("number");
  });
  it("should return the minimimum length of three words", function() {
    expect(findMinLengthOfThreeWords("a", "be", "see")).to.deep.eq(1);
  });
  it("should return the minimimum length of three words when there is a tie", function() {
    expect(findMinLengthOfThreeWords("these", "three", "words")).to.deep.eq(5);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
