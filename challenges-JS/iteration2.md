# Iteration 2

### !challenge

* type: local-snippet
* language: javascript
* id: 0c21c708-bcb4-4810-a951-c47b6e27184b
* title: getStringLength

### !question

Write a function called "getStringLength".

Given a string, "getStringLength" returns the length of the given string.

Notes:
* Do NOT use any native 'length' methods.
* You might consider using 'substring' or 'slice' as alternatives.

```
var output = getStringLength('hello');
console.log(output); // --> 5
```

### !end-question

### !placeholder

```js
function getStringLength(string) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("getStringLength", function() {
  it("should return a number", function() {
    expect(typeof getStringLength("heyo")).to.deep.eq("number");
  });
  it("should not use the native length operator", function() {
    var body = getStringLength.toString();
    expect(/length/.test(body)).to.deep.eq(false);
  });
  it("should return the length of a string", function() {
    expect(getStringLength("heyo")).to.deep.eq(4);
  });
  it("should return the length of an empty string", function() {
    expect(getStringLength("")).to.deep.eq(0);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
