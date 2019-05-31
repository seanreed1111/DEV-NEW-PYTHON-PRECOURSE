### !challenge

* type: local-snippet
* language: javascript
* id: 184175a0-0e1a-4639-9502-825d7e6cc8f3
* title: repeatString.md

### !question

Write a function called "repeatString".

Given a string and a number, "repeatString" returns the given string repeated the given number of times.

```
var output = repeatString('code', 3);
console.log(output); // --> 'codecodecode'
```

### !end-question

### !placeholder

```js
function repeatString(string, num) {
  // your code here
}
```

### !end-placeholder

### !tests

```js

describe("repeatString", function() {
  it("should return a string", function() {
    expect(typeof(repeatString("what", 3))).to.deep.eq("string");
  });
  it("should repeat a string a given number of times", function() {
    expect(repeatString("what", 3)).to.deep.eq("whatwhatwhat");
  });
  it("should repeat a string 0 number of times", function() {
    expect(repeatString("what", 0)).to.deep.eq("");
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
