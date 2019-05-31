### !challenge

* type: local-snippet
* language: javascript
* id: 6a474db4-3933-40f0-8af5-d52e55e0dff0
* title: getEvenLengthWordsAtProperty*.md

### !question

Write a function called "getEvenLengthWordsAtProperty".

Given an object and a key, "getEvenLengthWordsAtProperty" returns an array containing all the even length word elements of the array located at the given key.

Notes:
* If the array is empty, it should return an empty array.
* If it contains no even length elements, it should return an empty array.
* If the property at the given key is not an array, it should return an empty array.
* If there is no property at the key, it should return an empty array.

```
var obj = {
  key: ['a', 'long', 'game']
};
var output = getEvenLengthWordsAtProperty(obj, 'key');
console.log(output); // --> ['long', 'game']
```

### !end-question

### !placeholder

```js
function getEvenLengthWordsAtProperty(obj, key) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("getEvenLengthWordsAtProperty", function() {
  it("should return an array containing all the even length elements of the array located at key", function() {
    var obj = {
      array: ["a", "long", "game"]
    };
    expect(getEvenLengthWordsAtProperty(obj, "array")).to.deep.eq(["long", "game"]);
  });
  it("should return an empty array if the array has only no even length elements", function() {
    var obj = {
      array: ["I", "may", "say"]
    };
    expect(getEvenLengthWordsAtProperty(obj, "array")).to.deep.eq([]);
  });
  it("should return an empty array if the array is empty", function() {
    var obj = {
      array: []
    };
    expect(getEvenLengthWordsAtProperty(obj, "array")).to.deep.eq([]);
  });
  it("should return an empty array if the property is not an array", function() {
    var obj = {
      array: "sike"
    };
    expect(getEvenLengthWordsAtProperty(obj, "array")).to.deep.eq([]);
  });
  it("should return an empty array if the property does not exist", function() {
    var obj = {
      what: "sike"
    };
    expect(getEvenLengthWordsAtProperty(obj, "array")).to.deep.eq([]);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
