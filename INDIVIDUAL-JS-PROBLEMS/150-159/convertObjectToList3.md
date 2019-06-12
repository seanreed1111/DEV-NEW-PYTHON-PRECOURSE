### !challenge

* type: local-snippet
* language: javascript
* id: 862b3ed4-83e2-4253-9e53-e7d2263c2727
* title: convertObjectToList3.md

### !question

Write a function called "convertObjectToList" which converts an object literal into an array of arrays, like this:

Argument:

```
{
  name: 'Holly',
  age: 35,
  role: 'producer'
}
```

Return value:

```
[['name', 'Holly'], ['age', 35], ['role', 'producer']]
```

### !end-question

### !placeholder

```js
function convertObjectToList(obj) {
  // your code here
}
```

### !end-placeholder

### !tests

```js

describe('convertObjectToList', function() {
  it('converts_the_sample_data', function() {
    var input = {
      name: 'Holly',
      age: 35,
      role: 'producer'
    };
    var output = convertObjectToList(input);
    expect(output[0][0]).to.deep.eq('name');
    expect(output[0][1]).to.deep.eq('Holly');
    expect(output[1][0]).to.deep.eq('age');
    expect(output[1][1]).to.deep.eq(35);
    expect(output[2][0]).to.deep.eq('role');
    expect(output[2][1]).to.deep.eq('producer');
  });
});

describe('convertObjectToList', function() {
  it('converts_some_other_data', function() {
    var input = {
      foo: 'FOO',
      bar: 'BAR',
      baz: 123,
      'another key': null
    };
    var output = convertObjectToList(input);
    expect(output[0][0]).to.deep.eq('foo');
    expect(output[0][1]).to.deep.eq('FOO');
    expect(output[1][0]).to.deep.eq('bar');
    expect(output[1][1]).to.deep.eq('BAR');
    expect(output[2][0]).to.deep.eq('baz');
    expect(output[2][1]).to.deep.eq(123);
    expect(output[3][0]).to.deep.eq('another key');
    expect(output[3][1]).to.deep.eq(null);
  })
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
