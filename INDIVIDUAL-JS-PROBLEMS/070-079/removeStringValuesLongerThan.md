### !challenge

* type: local-snippet
* language: javascript
* id: 47b07382-07c8-41b1-98e0-dae82ed992da
* title: removeStringValuesLongerThan.md

### !question

Write a function called "removeStringValuesLongerThan".

Given an number and an object, "removeStringValuesLongerThan" removes any properties on the given object whose values are strings longer than the given number.

```
var obj = {
  name: 'Montana',
  age: 20,
  location: 'Texas'
};
removeStringValuesLongerThan(6, obj);
console.log(obj); // { age: 20, location: 'Texas' }
```

### !end-question

### !placeholder

```js
function removeStringValuesLongerThan(num, obj) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("removeStringValuesLongerThan", function() {
  it("should remove any properties with values that are strings longer than num", function() {
    var obj = {
      a: "hello",
      b: 2,
      c: "montana",
      d: 4
    };
    var result = {
      a: "hello",
      b: 2,
      d: 4
    };
    removeStringValuesLongerThan(5, obj);
    expect(obj).to.deep.eq(result);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
