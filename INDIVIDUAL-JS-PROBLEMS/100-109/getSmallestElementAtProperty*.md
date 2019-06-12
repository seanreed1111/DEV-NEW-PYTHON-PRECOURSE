### !challenge

* type: local-snippet
* language: javascript
* id: c0da71bc-093b-4eae-a574-d31aa2cb1109
* title: getSmallestElementAtProperty*.md

### !question

Write a function called "getSmallestElementAtProperty".

Given an object and a key, "getSmallestElementAtProperty" returns the smallest element in the array located at the given key.

Notes:
* If the array is empty, it should return undefined.
* If the property at the given key is not an array, it should return undefined.
* If there is no property at the key, it should return undefined.

```
var obj = {
  key: [2, 1, 5]
};
var output = getSmallestElementAtProperty(obj, 'key');
console.log(output); // --> 1
```

### !end-question

### !placeholder

```js

function getSmallestElementAtProperty(obj, key) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("getSmallestElementAtProperty", function() {
  it("should return the smallest element of the array located at key", function() {
    var obj = {
      array: [1, 2, 4]
    };
    expect(getSmallestElementAtProperty(obj, "array")).to.deep.eq(1);
  });
  it("should return undefined if the array is empty", function() {
    var obj = {
      array: []
    };
    expect(getSmallestElementAtProperty(obj, "array")).to.deep.eq(undefined);
  });
  it("should return undefined if the property is not an array", function() {
    var obj = {
      array: "sike"
    };
    expect(getSmallestElementAtProperty(obj, "array")).to.deep.eq(undefined);
  });
  it("should return undefined if the property does not exist", function() {
    var obj = {
      what: "sike"
    };
    expect(getSmallestElementAtProperty(obj, "array")).to.deep.eq(undefined);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
