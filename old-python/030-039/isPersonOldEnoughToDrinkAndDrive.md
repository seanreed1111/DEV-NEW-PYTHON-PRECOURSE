### !challenge

* type: local-snippet
* language: javascript
* id: 67b64495-b5b3-4d3a-b3a2-7a471de45c03
* title: isPersonOldEnoughToDrinkAndDrive.md

### !question

Write a function called "isPersonOldEnoughToDrinkAndDrive".

Given a "person" object, that contains an "age" property, "isPersonOldEnoughToDrinkAndDrive" returns whether the given person is old enough to legally drink and drive in the United States.

Notes:
* The legal drinking age in the United States is 21.
* The legal driving age in the United States is 16.
* It is ALWAYS illegal to drink and drive in the United States.

```
var obj = {
  age: 45
};
var output = isPersonOldEnoughToDrinkAndDrive(obj);
console.log(output); // --> false
```

### !end-question

### !placeholder

```js
function isPersonOldEnoughToDrinkAndDrive(person) {
  // your code here
   

   
}

```

### !end-placeholder

### !tests

```js

describe("isPersonOldEnoughToDrinkAndDrive", function() {
  it("should return a boolean", function() {
    var person = {
      age: 55
    };
    expect(typeof isPersonOldEnoughToDrinkAndDrive(person)).to.deep.eq("boolean");
  });
  it("should return false", function() {
    expect(isPersonOldEnoughToDrinkAndDrive()).to.deep.eq(false);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge