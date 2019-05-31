### !challenge

* type: local-snippet
* language: javascript
* id: 0fa027aa-cf1a-4b02-a19e-5d43a6c83a32
* title: removeArrayValues.md

### !question

Write a function called "removeArrayValues".

Given an object, "removeArrayValues" removes any properties whose values are arrays.

```
var obj = {
  a: [1, 3, 4],
  b: 2,
  c: ['hi', 'there']
}
removeArrayValues(obj);
console.log(obj); // --> { b: 2 }
```

### !end-question

### !placeholder

```js
function removeArrayValues(obj) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("removeArrayValues", function() {
  it("should remove any properties with values that are arrays", function() {
    var obj = {
      a: [true, false],
      b: 2,
      c: [8, 0],
      d: 4
    };
    var result = {
      b: 2,
      d: 4
    };
    removeArrayValues(obj);
    expect(obj).to.deep.eq(result);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
