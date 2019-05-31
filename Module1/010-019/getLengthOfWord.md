### !challenge

* type: local-snippet
* language: javascript
* id: bba621c8-20e7-49e3-a5d3-30dd3fc58057
* title: getLengthOfWord.md

### !question

Write a function called "getLengthOfWord".
Given a word, "getLengthOfWord" returns the length of the given word.

```
var output = getLengthOfWord('some');
console.log(output); // --> 4
```

### !end-question

### !placeholder

```js
function getLengthOfWord(word) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("getLengthOfWord", function() {
  it("should return a number", function() {
    expect(typeof getLengthOfWord("something")).to.deep.eq("number");
  });
  it("should return the length of the passed in word", function() {
    expect(getLengthOfWord("random")).to.deep.eq(6)
  });
  it("should return the length of an empty word", function() {
    expect(getLengthOfWord("")).to.deep.eq(0)
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
