### !challenge

* type: local-snippet
* language: javascript
* id: 89e3ad32-7097-4f1b-a4c8-445738b02a39
* title: removeProperty.md

### !question

Write a function called "removeProperty".
Given an object and a key, "removeProperty" removes the given key from the given object.

```
var obj = {
  name: 'Sam',
  age: 20
}
removeProperty(obj, 'name');
console.log(obj.name); // --> undefined
```

### !end-question

### !placeholder

```js
function removeProperty(obj, key) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("removeProperty", function() {
  it("should remove the property from the passed in object at the passed in key", function() {

    var testObj = {
      name: "Mel",
      age: 88
    };

    removeProperty(testObj, "name");
    expect(testObj.name).to.deep.eq(undefined);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
