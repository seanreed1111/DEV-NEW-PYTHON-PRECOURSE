# Array String Methods 1

### !challenge

* type: local-snippet
* language: javascript
* id: 7efe888f-b6e0-4255-933e-0f6f12bfe7f2
* title: getAllLetters

### !question

Write a function called "getAllLetters".

Given a word, "getAllLetters" returns an array containing every character in the word.

Notes:
* If given an empty string, it should return an empty array.

```
var output = getAllLetters('Radagast');
console.log(output); // --> ['R', 'a', 'd', 'a', 'g', 'a', 's', 't']
```

### !end-question

### !placeholder

```js
function getAllLetters(str) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("getAllLetters", function() {
  it("should return an array", function() {
    expect(Array.isArray(getAllLetters("something like this here"))).to.deep.eq(true);
  });
  it("should return an array containing all the letters in the word", function() {
    expect(getAllLetters("Eowin")).to.deep.eq(["E", "o", "w", "i", "n"]);
  });
  it("should return an empty array when given an empty string", function() {
    expect(getAllLetters("")).to.deep.eq([]);
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
* id: afe8bb31-31d2-4ef6-b344-e7cbcfe01d1f
* title: getAllWords

### !question

Write a function called "getAllWords".

Given a sentence, "getAllWords" returns an array containing every word in the sentence.

Notes:
* If given an empty string, it should return an empty array.

```
var output = getAllWords('Radagast the Brown');
console.log(output); // --> ['Radagast', 'the', 'Brown']
```

### !end-question

### !placeholder

```js
function getAllWords(str) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js


describe("getAllWords", function() {
  it("should return an array", function() {
    expect(Array.isArray(getAllWords("something like this here"))).to.deep.eq(true);
  });
  it("should return an array containing all the words in the sentence", function() {
    expect(getAllWords("Something like this here")).to.deep.eq(["Something", "like", "this", "here"]);
  });
  it("should return an empty array when given an empty string", function() {
    expect(getAllWords("")).to.deep.eq([]);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
