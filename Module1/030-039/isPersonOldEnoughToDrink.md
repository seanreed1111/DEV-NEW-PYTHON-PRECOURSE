### !challenge

* type: local-snippet
* language: javascript
* id: 50c8d3fe-9c02-40cd-af93-0936ee80bfc5
* title: isPersonOldEnoughToDrink.md

### !question

Write a function called "isPersonOldEnoughToDrink".

Given a "person" object, that contains an "age" property, "isPersonOldEnoughToDrink" returns whether the given person is old enough to drink.

Notes:
* The legal drinking age in the United States is 21.

```
var obj = {
  age: 16
};
var output = isPersonOldEnoughToDrink(obj);
console.log(output); // --> false
```

### !end-question

### !placeholder

```js
function isPersonOldEnoughToDrink(person) {
  // your code here
   

   
}

```

### !end-placeholder

### !tests

```js

describe("isPersonOldEnoughToDrink", function() {
  it("should return a boolean", function() {
    var person = {
      age: 55
    };
    expect(typeof isPersonOldEnoughToDrink(person)).to.deep.eq("boolean");
  });
  it("should return true if a person has an age of over 21", function() {
    var person = {
      age: 55
    };
    expect(isPersonOldEnoughToDrink(person)).to.deep.eq(true);
  });
  it("should return true if a person has an age of 21", function() {
    var person = {
      age: 21
    };
    expect(isPersonOldEnoughToDrink(person)).to.deep.eq(true);
  });
  it("should return false if a person has an age under 21", function() {
    var person = {
      age: 20
    };
    expect(isPersonOldEnoughToDrink(person)).to.deep.eq(false);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
