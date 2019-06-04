### !challenge

* type: local-snippet
* language: javascript
* id: 5c6e257b-c85d-4a59-9df2-777bc47d4d92
* title: convertArrayToObject3.md

### !question

Write a function called "transformEmployeeData" that transforms some employee data from one format to another.

The argument will look like this:

```
[
    [
        ['firstName', 'Joe'], ['lastName', 'Blow'], ['age', 42], ['role', 'clerk']
    ],
    [
        ['firstName', 'Mary'], ['lastName', 'Jenkins'], ['age', 36], ['role', 'manager']
    ]
]
```

Given that input, the return value should look like this:

```
[
    {firstName: 'Joe', lastName: 'Blow', age: 42, role: 'clerk'},
    {firstName: 'Mary', lastName: 'Jenkins', age: 36, role: 'manager'}
]
```

Note that the input may have a different number of rows or different keys than the given sample.

For example, let's say the HR department adds a "tshirtSize" field to each employee record.
Your code should flexibly accommodate that.

### !end-question

### !placeholder

```js
function transformEmployeeData(employeeData) {
  // your code here
}
```

### !end-placeholder

### !tests

```js

describe('transformEmployeeData', function() {
  it('transforms_the_sample_data', function() {
    var input = [[['firstName', 'Joe'], ['lastName', 'Blow'], ['age', 42], ['role', 'clerk']],
                 [['firstName', 'Mary'], ['lastName', 'Jenkins'], ['age', 36], ['role', 'manager']]];
    var output = transformEmployeeData(input);
    expect(output[0].firstName).to.deep.eq('Joe');
    expect(output[1].age).to.deep.eq(36);
  });

  it('transforms_some_other_data', function() {
    var input = [[['firstName', 'Joe'], ['lastName', 'Blow'], ['favoriteIceCream', 'chocolate'], ['role', 'clerk']],
                 [['firstName', 'Carl'], ['lastName', 'Sagan'], ['favoriteIceCream', 'starfruit'], ['role', 'seer']],
                 [['firstName', 'Mary'], ['lastName', 'Jenkins'], ['favoriteIceCream', 'vanilla'], ['role', 'manager']]];
    var output = transformEmployeeData(input);
    expect(output[1].favoriteIceCream).to.deep.eq('starfruit');
  });

});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
