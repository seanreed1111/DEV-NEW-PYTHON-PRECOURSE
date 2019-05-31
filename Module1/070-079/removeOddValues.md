### !challenge

* type: local-snippet
* language: javascript
* id: e01182d1-9906-49b8-830d-bae725ad5b4b
* title: removeOddValues.md

### !question

Write a function called "removeOddValues".

Given an object, "removeOddValues" removes any properties whose values are odd numbers.

```
var obj = {
  a: 2,
  b: 3,
  c: 4
};
removeOddValues(obj);
console.log(obj); // --> { a: 2, c: 4 }
```

### !end-question

### !placeholder

```js
function removeOddValues(obj) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("removeOddValues", function() {
  it("should remove any properties with values that are odd numbers", function() {
    var obj = {
      a: 1,
      b: 2,
      c: 3,
      d: 4
    };
    var result = {
      b: 2,
      d: 4
    };
    removeOddValues(obj);
    expect(obj).to.deep.eq(result);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
