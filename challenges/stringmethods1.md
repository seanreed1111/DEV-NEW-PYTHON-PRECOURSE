# String Methods 1

### !challenge

* type: local-snippet
* language: javascript
* id: 9a909a65-ed43-4747-ac79-18fb4a9eacc5
* title: getFullName

### !question

Write a function called "getFullName".
Given a first and a last name, "getFullName" returns a single string with the given first and last names separated by a single space.

```
var output = getFullName('Joe', 'Smith');
console.log(output); // --> 'Joe Smith'
```

### !end-question

### !placeholder

```js

function getFullName(firstName, lastName) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("getFullName", function() {
  it("should return a string", function() {
    expect(typeof(getFullName("Rebecca", "Solnit"))).to.deep.eq("string");
  });
  it("should return a full name using firstName and lastName", function() {
    expect(getFullName("Rebecca", "Solnit")).to.deep.eq("Rebecca Solnit");
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
* id: bba621c8-20e7-49e3-a5d3-30dd3fc58057
* title: getLengthOfWord

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

### !challenge

* type: local-snippet
* language: javascript
* id: 37a022e4-9104-4ac9-b68b-b63377dd3cb8
* title: getLengthOfTwoWords

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
