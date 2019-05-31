### !challenge

* type: local-snippet
* language: javascript
* id: 56940947-7f0a-444b-bb8a-635464d92f45
* title: addFullNameProperty.md

### !question

Write a function called "addFullNameProperty".

Given an object that has a "firstName" property and a "lastName" property, "addFullNameProperty" returns a "fullName" property whose value is a string with the first name and last name separated by a space.

```
var person = {
  firstName: 'Jade',
  lastName: 'Smith'
};
addFullNameProperty(person);
console.log(person.fullName); // --> 'Jade Smith'
```

### !end-question

### !placeholder

```js
function addFullNameProperty(obj) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js


describe("addFullNameProperty", function() {
  it("should create a fullName property with the firstName and lastName separated by a space", function() {
    var tim = {
      firstName: "Tim",
      lastName: "Goldfish"
    };
    addFullNameProperty(tim);
    expect(tim.fullName).to.deep.eq("Tim Goldfish");
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
