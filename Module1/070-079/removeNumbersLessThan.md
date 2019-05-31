### !challenge

* type: local-snippet
* language: javascript
* id: ee54e130-d037-4ff7-9c59-5461322523e1
* title: removeNumbersLessThan.md

### !question

Write a function called "removeNumbersLessThan".

Given a number and an object, "removeNumbersLessThan" removes any properties whose values are numbers less than the given number.

```
var obj = {
  a: 8,
  b: 2,
  c: 'montana'
}
removeNumbersLessThan(5, obj);
console.log(obj); // --> { a: 8, c: 'montana' }
```

### !end-question

### !placeholder

```js
function removeNumbersLessThan(num, obj) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("removeNumbersLessThan", function() {
  it("should remove any properties with values that are numbers less than num", function() {
    var obj = {
      a: "hello",
      b: 2,
      c: "montana",
      d: 4
    };
    var result = {
      a: "hello",
      c: "montana",
      d: 4
    };
    removeNumbersLessThan(3, obj);
    expect(obj).to.deep.eq(result);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
