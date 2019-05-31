### !challenge

* type: local-snippet
* language: javascript
* id: 53bb0534-cafa-44a2-85ce-1d450e1f79ef
* title: addArrayProperty.md

### !question

Write a function called "addArrayProperty".

Given an object, a key, and an array, "addArrayProperty" sets a new property on the object at the given key, with its value set to the given array.

```
var myObj = {};
var myArray = [1, 3];
addArrayProperty(myObj, 'myProperty', myArray);
console.log(myObj.myProperty); // --> [1, 3]
```

### !end-question

### !placeholder

```js
function addArrayProperty(obj, key, arr) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("addArrayProperty", function() {
  var testObj;
  var testArray;
  beforeEach(function() {
    testObj = {};
    testArray = [1, 4];
  });
  it("should set the value at the passed in key on the passed in object to be the passed in array", function() {
    addArrayProperty(testObj, "testKey", testArray);
    expect(testObj.testKey).to.deep.eq(testArray);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
