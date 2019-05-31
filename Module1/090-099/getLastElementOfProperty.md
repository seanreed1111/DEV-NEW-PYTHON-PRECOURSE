### !challenge

* type: local-snippet
* language: javascript
* id: 0128dc86-b7a6-4022-8aa6-178ac9dd020b
* title: getLastElementOfProperty.md

### !question

Write a function called "getLastElementOfProperty".

Given an object and a key, "getLastElementOfProperty" returns the last element of an array located at the given key.

Notes:
* If the array is empty, it should return undefined.
* if the property at the given key is not an array, it should return undefined.
* If there is no property at the key, it should return undefined.

```
var obj = {
  key: [1, 2, 5]
};
var output = getLastElementOfProperty(obj, 'key');
console.log(output); // --> 5
```

### !end-question

### !placeholder

```js
function getLastElementOfProperty(obj, key) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("getLastElementOfProperty", function() {
  it("should return the last element of the array located at key", function() {
    var obj = {
      array: [1, 2, 4]
    };
    expect(getLastElementOfProperty(obj, "array")).to.deep.eq(4);
  });
  it("should return undefined if the array is empty", function() {
    var obj = {
      array: []
    };
    expect(getLastElementOfProperty(obj, "array")).to.deep.eq(undefined);
  });
  it("should return undefined if the property is not an array", function() {
    var obj = {
      array: "sike"
    };
    expect(getLastElementOfProperty(obj, "array")).to.deep.eq(undefined);
  });
  it("should return undefined if the property does not exist", function() {
    var obj = {
      what: "sike"
    };
    expect(getLastElementOfProperty(obj, "array")).to.deep.eq(undefined);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
