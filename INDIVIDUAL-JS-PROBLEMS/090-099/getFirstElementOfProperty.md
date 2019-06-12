### !challenge

* type: local-snippet
* language: javascript
* id: aa75a574-cc22-47c9-9464-6d9cf0a3b7de
* title: getFirstElementOfProperty.md

### !question

Write a function called "getFirstElementOfProperty".

Given an object and a key, "getFirstElementOfProperty" returns the first element of the array located at the given key.

Notes:
* If the array is empty, it should return undefined.
* If the property at the given key is not an array, it should return undefined.
* If there is no property at the key, it should return undefined.

```
var obj = {
  key: [1, 2, 4]
};
var output = getFirstElementOfProperty(obj, 'key');
console.log(output); // --> 1
```

### !end-question

### !placeholder

```js
function getFirstElementOfProperty(obj, key) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("getFirstElementOfProperty", function() {
  it("should return the first element of the array located at key", function() {
    var obj = {
      array: [1, 2, 4]
    };
    expect(getFirstElementOfProperty(obj, "array")).to.deep.eq(1);
  });
  it("should return undefined if the array is empty", function() {
    var obj = {
      array: []
    };
    expect(getFirstElementOfProperty(obj, "array")).to.deep.eq(undefined);
  });
  it("should return undefined if the property is not an array", function() {
    var obj = {
      array: "sike"
    };
    expect(getFirstElementOfProperty(obj, "array")).to.deep.eq(undefined);
  });
  it("should return undefined if the property does not exist", function() {
    var obj = {
      what: "sike"
    };
    expect(getFirstElementOfProperty(obj, "array")).to.deep.eq(undefined);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
