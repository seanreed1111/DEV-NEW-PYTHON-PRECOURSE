### !challenge

* type: local-snippet
* language: javascript
* id: 717ab908-571e-4a56-a675-ec540640c6ea
* title: removeNumberValues.md

### !question

Write a function called "removeNumberValues".

Given an object, "removeNumberValues" removes any properties whose values are numbers.

```
var obj = {
  a: 2,
  b: 'remaining',
  c: 4
};
removeNumberValues(obj);
console.log(obj); // --> { b: 'remaining' }
```

### !end-question

### !placeholder

```js
function removeNumberValues(obj) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js


describe("removeNumberValues", function() {
  it("should remove any properties with values that are numbers", function() {
    var obj = {
      a: [true, false],
      b: 2,
      c: [8, 0],
      d: 4
    };
    var result = {
      a: [true, false],
      c: [8, 0]
    };
    removeNumberValues(obj);
    expect(obj).to.deep.eq(result);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
