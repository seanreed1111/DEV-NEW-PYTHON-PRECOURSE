### !challenge

* type: local-snippet
* language: javascript
* id: a3d52d99-9784-457b-8201-1210a097d449
* title: countCharacter.md

### !question

Write a function called "countCharacter".

Given a string input and a character, "countCharacter" returns the number of occurences of a given character in the given string.

```
var output = countCharacter('I am a hacker', 'a');
console.log(output); // --> 3
```

### !end-question

### !placeholder

```js
function countCharacter(str, char) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("countCharacter", function() {
  it("should return a number", function() {
    expect(typeof countCharacter("say what!?", "a")).to.deep.eq("number");
  });
  it("should return the number of occurences of a character in a string when the character exists", function() {
    expect(countCharacter("say what!?", "a")).to.deep.eq(2);
  });
  it("should return the number of occurences of a character in a string when the character does not exist", function() {
    expect(countCharacter("say what!?", "x")).to.deep.eq(0);
  });
  it("should return the number of occurences of a non-alphanumeric character in a string when the character exists", function() {
    expect(countCharacter("say what!?", " ")).to.deep.eq(1);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
