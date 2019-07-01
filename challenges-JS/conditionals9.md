# Conditionals 9

### !challenge

* type: local-snippet
* language: javascript
* id: a51b922c-0c0b-42b1-b372-f57a7e3cc12e
* title: getLongestOfThreeWords

### !question

Write a function called "getLongestOfThreeWords".

Given 3 words, "getLongestOfThreeWords" returns the longest of three words.

Notes:
* If there is a tie, it should return the first word in the tie.

```
var output = getLongestOfThreeWords('these', 'three', 'words');
console.log(output); // --> 'these'
```

### !end-question

### !placeholder

```js
function getLongestOfThreeWords(word1, word2, word3) {
  // your code here

}
```

### !end-placeholder

### !tests

```js

describe("getLongestOfThreeWords", function() {
  it("should return a string", function() {
    expect(typeof(getLongestOfThreeWords("a", "be", "see"))).to.deep.eq("string");
  });
  it("should return the longest of three words", function() {
    expect(getLongestOfThreeWords("a", "be", "see")).to.deep.eq("see");
  });
  it("should return the first occurence of a longest word when there is a tie", function() {
    expect(getLongestOfThreeWords("these", "three", "words")).to.deep.eq("these");
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: local-snippet
* language: javascript
* id: e70b8323-50dd-4588-a4c7-56138c5c4bdd
* title: findShortestOfThreeWords

### !question

Write a function called "findShortestOfThreeWords".

Given 3 strings, "findShortestOfThreeWords" returns the shortest of the given strings.

Notes:
* If there are ties, it should return the first word in the parameters list.

```
var output = findShortestOfThreeWords('a', 'two', 'three');
console.log(output); // --> 'a'
```

### !end-question

### !placeholder

```js
function findShortestOfThreeWords(word1, word2, word3) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("findShortestOfThreeWords", function() {
  it("should return a string", function() {
    expect(typeof(findShortestOfThreeWords("a", "be", "see"))).to.deep.eq("string");
  });
  it("should return the shortest of three words", function() {
    expect(findShortestOfThreeWords("abacus", "be", "see")).to.deep.eq("be");
  });
  it("should return the first occurence of a shortest word when there is a tie", function() {
    expect(findShortestOfThreeWords("these", "apple", "words")).to.deep.eq("these");
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
