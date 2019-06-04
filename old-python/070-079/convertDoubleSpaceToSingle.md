### !challenge

* type: local-snippet
* language: javascript
* id: d27d4372-5782-4123-8b80-e060455dd96e
* title: convertDoubleSpaceToSingle.md

### !question

Write a function called "convertDoubleSpaceToSingle".

Given a string, "convertDoubleSpaceToSingle" returns the passed in string, with all the double spaces converted to single spaces.

```
var output = convertDoubleSpaceToSingle("string  with  double  spaces");
console.log(output); // --> "string with double spaces"
````

Notes:
* In order to do this problem, you should be familiar with "String.split", and "Array.join".


### !end-question

### !placeholder

```js
function convertDoubleSpaceToSingle(str) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("convertDoubleSpaceToSingle", function() {
  it("should return a string", function() {
    expect(typeof convertDoubleSpaceToSingle("This  here sentence")).to.deep.eq("string");
  });
  it("should return the passed in string, with any double spaces converted to single spaces", function() {
    expect(convertDoubleSpaceToSingle("this  here  string")).to.deep.eq("this here string");
  });
  it("should return the passed in string when there are no double spaces", function() {
    expect(convertDoubleSpaceToSingle("this here string")).to.deep.eq("this here string");
  });
  it("should return an empty string when passed an empty string", function() {
    expect(convertDoubleSpaceToSingle("")).to.deep.eq("");
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
