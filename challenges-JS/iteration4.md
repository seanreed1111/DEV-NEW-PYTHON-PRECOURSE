# Iteration 4

### !challenge

* type: local-snippet
* language: javascript
* id: cbcdeb30-874c-43d4-bf34-efee529c29d9
* title: computeFactorialOfN

### !question

Write a function called "computeFactorialOfN".

Given a natural number (a whole number greater than 0), "computeFactorialOfN" returns its factorial.

```
var output = computeFactorialOfN(3);
console.log(output); // --> 6

var output = computeFactorialOfN(4);
console.log(output); // --> 24
```

### !end-question

### !placeholder

```js

function computeFactorialOfN(n) {
  // your code here

}
```

### !end-placeholder

### !tests

```js

describe("computeFactorialOfN", function() {
  it("should return a number", function() {
    expect(typeof computeFactorialOfN(7)).to.deep.eq("number");
  });
  it("should return the factorial of 'n'", function() {
    expect(computeFactorialOfN(4)).to.deep.eq(24);
  });
  it("should return the factorial of 1", function() {
    expect(computeFactorialOfN(1)).to.deep.eq(1);
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
* id: 184175a0-0e1a-4639-9502-825d7e6cc8f3
* title: repeatString

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
