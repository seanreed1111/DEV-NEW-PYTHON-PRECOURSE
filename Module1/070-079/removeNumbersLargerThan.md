### !challenge

* type: local-snippet
* language: javascript
* id: 09b2c4c3-d899-49fa-a943-60a03de413c2
* title: removeNumbersLargerThan.md

### !question

Write a function called "removeNumbersLargerThan".

Given a number and an object, "removeNumbersLargerThan" removes any properties whose values are numbers greater than the given number.

```
var obj = {
  a: 8,
  b: 2,
  c: 'montana'
}
removeNumbersLargerThan(5, obj);
console.log(obj); // --> { b: 2, c: 'montana' }
```

### !end-question

### !placeholder

```js
function removeNumbersLargerThan(num, obj) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("removeNumbersLargerThan", function() {
  it("should remove any properties with values that are numbers greater than num", function() {
    var obj = {
      a: "hello",
      b: 2,
      c: "montana",
      d: 4
    };
    var result = {
      a: "hello",
      b: 2,
      c: "montana"
    };
    removeNumbersLargerThan(3, obj);
    expect(obj).to.deep.eq(result);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
