### !challenge

* type: local-snippet
* language: javascript
* id: c3fcc0c8-628e-40aa-992a-a85008a3d60d
* title: findMaxLengthOfThreeWords.md

### !question

Write a function called "findMaxLengthOfThreeWords".

Given 3 words, "findMaxLengthOfThreeWords" returns the length of the longest word.

```
var output = findMaxLengthOfThreeWords('a', 'be', 'see');
console.log(output); // --> 3
```

### !end-question

### !placeholder

```js
function findMaxLengthOfThreeWords(word1, word2, word3) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("findMaxLengthOfThreeWords", function() {
  it("should return a string", function() {
    expect(typeof findMaxLengthOfThreeWords("a", "be", "see")).to.deep.eq("number");
  });
  it("should return the maximimum length of three words", function() {
    expect(findMaxLengthOfThreeWords("a", "be", "see")).to.deep.eq(3);
  });
  it("should return the maximimum length of three words when there is a tie", function() {
    expect(findMaxLengthOfThreeWords("these", "three", "words")).to.deep.eq(5);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
