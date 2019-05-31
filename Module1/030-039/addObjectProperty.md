### !challenge

* type: local-snippet
* language: javascript
* id: c3b7ef25-71fe-47ff-9a75-2f9965695f31
* title: addObjectProperty.md

### !question

Write a function called "addObjectProperty".

Given two objects and a key, "addObjectProperty" sets a new property on the 1st object at the given key. The value of that new property is the entire 2nd object.

```
var person1 = {
  name: 'Joe Blow',
  role: 'schlub'
};
var person2 = {
  name: 'Mr. Burns',
  role: 'supervisor'
};
addObjectProperty(person1, 'manager', person2);
console.log(person1.manager); // --> { name: 'Mr. Burns', role: 'supervisor' }
```

### !end-question

### !placeholder

```js
function addObjectProperty(obj1, key, obj2) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("addObjectProperty", function() {
  var obj1;
  var obj2;
  beforeEach(function() {
    obj1 = {};
    obj2 = {
      name: "Dude"
    };
  });
  it('should set the value at the passed in key on the passed in object to be the second passed in object', function() {
    addObjectProperty(obj1, 'testKey', obj2);
    expect(obj1.testKey).to.deep.eq(obj2);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
