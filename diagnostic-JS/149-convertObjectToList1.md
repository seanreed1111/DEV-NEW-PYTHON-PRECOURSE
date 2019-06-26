### !challenge

* type: local-snippet
* language: javascript
* id: c484fcc2-9db9-4e13-9362-a1377b196679
* title: convertObjectToList1.md

### !question

Write a function called "getAllKeys" which returns an array of all the input object's keys.
Example input:
```
{
  name : 'Sam',
  age : 25,
  hasPets : true
}
```

Function's return value (output) :
```
['name', 'age', 'hasPets']
```

Do not use "Object.keys" to solve this prompt.

Note that your function should be able to handle any object passed in it.

E.g. it should also handle an input like:
```
{
  a : 'a',
  number : 11,
  hungry : true,
  grammyWins : 1
}
```

Function's return value (output):
```
['a', 'number', 'hungry', 'grammyWins']
```

### !end-question

### !placeholder

```js
function getAllKeys(obj) {
  // your code here
}
```

### !end-placeholder

### !tests

```js

describe('getAllKeys', function() {
  it('should_output_an_array_of_key_names', function(){
    var input = {
      foo: 'bar',
      level: 1,
      red: 'green',
      number: true
    }
    var expected = Object.keys(input);
    var actual = getAllKeys(input);

    expect(actual).not.to.deep.eq(undefined);
    expect(actual[0]).to.deep.eq(expected[0]);
    expect(actual[1]).to.deep.eq(expected[1]);
    expect(actual[2]).to.deep.eq(expected[2]);
    expect(actual[3]).to.deep.eq(expected[3]);
  });

  it ('should_not_use_restricted_methods', function() {
    var body = getAllKeys.toString();

    expect(/Object\.keys/.test(body)).to.deep.eq(false);
  });

});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
