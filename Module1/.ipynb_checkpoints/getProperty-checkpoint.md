### !challenge

* type: local-snippet
* language: javascript
* id: 3469deaf-8010-4036-b39c-902d281a897e
* title: getProperty.md

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
