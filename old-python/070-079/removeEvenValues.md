### !challenge

* type: local-snippet
* language: javascript
* id: 5c68f405-579c-4427-8f13-9df8539009c7
* title: removeEvenValues.md

### !question

Write a function called "removeEvenValues".

Given an object, "removeEvenValues" removes any properties whose values are even numbers.

Do this in place and return the original object, do not construct a cloned object that omits the properties.

Example:

```
var obj = {
  a: 2,
  b: 3,
  c: 4
};
removeEvenValues(obj);
console.log(obj); // --> { b: 3 }
```

### !end-question

### !placeholder

```js
function removeEvenValues(obj) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("removeEvenValues", function() {
  it("should remove any properties with values that are even numbers", function() {
    var obj = {
      a: 1,
      b: 2,
      c: 3,
      d: 4
    };
    var result = {
      a: 1,
      c: 3
    };
    removeEvenValues(obj);
    expect(obj).to.deep.eq(result);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
