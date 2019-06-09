# Objects 1

### !challenge

* type: local-snippet
* language: javascript
* id: 3469deaf-8010-4036-b39c-902d281a897e
* title: getProperty

### !question

Write a function called "getProperty".
Given an object and a key, "getProperty" returns the value of the property at the given key.
Notes:
* If there is no property at the given key, it should return undefined.

```
var obj = {
  key: 'value'
};
var output = getProperty(obj, 'key');
console.log(output); // --> 'value'
```

### !end-question

### !placeholder

```js
function getProperty(obj, key) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("getProperty", function() {
  var obj;

  beforeEach(function() {
    obj = {
      name: "You"
    }
  });

  it("should return the value of the property located in the object at the passed in key", function() {
    expect(getProperty(obj, "name")).to.deep.eq("You");
  });
  it("should return undefined when there is no property at the passed in key", function() {
    expect(getProperty(obj, "age")).to.deep.eq(undefined);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: local-snippet
* language: javascript
* id: 62b814e5-85d4-4d5b-8b5b-327692487625
* title: addProperty

### !question

Write a function called "addProperty".
Given an object, and a key, "addProperty" sets a new property on the given object with a value of true.

```
var myObj = {};
addProperty(myObj, 'myProperty');
console.log(myObj.myProperty); // --> true
```

### !end-question

### !placeholder

```js
function addProperty(obj, key) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("addProperty", function() {
  var testObj;
  beforeEach(function() {
    testObj = {};
  });
  it("should add a property to the passed in object at the passed in key", function() {
    addProperty(testObj, "testKey");
    expect(testObj.testKey).to.deep.eq(true);
  });
  it("should set the value at the passed in key to true on the passed in object", function() {
    addProperty(testObj, "testKey");
    expect(testObj).to.deep.eq({'testKey': true});
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: local-snippet
* language: javascript
* id: 89e3ad32-7097-4f1b-a4c8-445738b02a39
* title: removeProperty

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
