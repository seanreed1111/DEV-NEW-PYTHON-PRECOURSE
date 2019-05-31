### !challenge

* type: local-snippet
* language: javascript
* id: 74b7a416-a4bc-4854-b870-0f92c6d57335
* title: countNumberOfKeys.md

### !question

Write a function called "countNumberOfKeys".

Given an object, "countNumberOfKeys" returns how many properties the given object has.

```
var obj = {
  a: 1,
  b: 2,
  c: 3
};
var output = countNumberOfKeys(obj);
console.log(output); // --> 3
```

### !end-question

### !placeholder

```js
function countNumberOfKeys(obj) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("countNumberOfKeys", function() {
  it("should return a number", function() {
    var obj = {};
    expect(typeof(countNumberOfKeys(obj))).to.deep.eq("number");
  });
  it("should return the number of keys for an object", function() {
    var obj = {
      a: 1,
      b: 2,
      c: 3
    };
    expect(countNumberOfKeys(obj)).to.deep.eq(3);
  });
  it("should return 0 for an object with no keys", function() {
    var obj = {};
    expect(countNumberOfKeys(obj)).to.deep.eq(0);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
