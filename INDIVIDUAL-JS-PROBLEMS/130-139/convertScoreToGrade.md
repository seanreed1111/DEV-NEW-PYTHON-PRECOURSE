### !challenge

* type: local-snippet
* language: javascript
* id: f328e513-d275-4a7b-aa70-b3ac917ce57a
* title: convertScoreToGrade.md

### !question

Write a function called "convertScoreToGrade".

Given a score, "convertScoreToGrade" returns a string representing the letter grade corresponding to the given score.

Notes:
* (100 - 90) --> 'A'
* (89  - 80) --> 'B'
* (79  - 70) --> 'C'
* (69  - 60) --> 'D'
* (59  -  0) --> 'F'
* If the given score is greater than 100 or less than 0, it should return 'INVALID SCORE'.

```
var output = convertScoreToGrade(91);
console.log(output); // --> 'A'
```

### !end-question

### !placeholder

```js
function convertScoreToGrade(score) {
  // your code here
}
```

### !end-placeholder

### !tests

```js

describe("convertScoreToGrade", function() {
  it("should return a string", function() {
    expect(typeof(convertScoreToGrade(95))).to.deep.eq("string");
  });
  it("should return 'A' for scores between 90 and 100", function() {
    expect(convertScoreToGrade(95)).to.deep.eq("A");
  });
  it("should return 'B' for scores between 80 and 89", function() {
    expect(convertScoreToGrade(80)).to.deep.eq("B");
  });
  it("should return 'C' for scores between 70 and 79", function() {
    expect(convertScoreToGrade(79)).to.deep.eq("C");
  });
  it("should return 'D' for scores between 60 and 69", function() {
    expect(convertScoreToGrade(60)).to.deep.eq("D");
  });
  it("should return 'F' for 59", function() {
    expect(convertScoreToGrade(59)).to.deep.eq("F");
  });
  it("should return 'F' for scores between 0 and 59", function() {
    expect(convertScoreToGrade(50)).to.deep.eq("F");
  });
  it("should return 'F' for 0", function() {
    expect(convertScoreToGrade(0)).to.deep.eq("F");
  });
  it("should return 'INVALID SCORE' for scores less than 0", function() {
    expect(convertScoreToGrade(-1)).to.deep.eq("INVALID SCORE");
  });
  it("should return 'INVALID SCORE' for scores greater than 100", function() {
    expect(convertScoreToGrade(101)).to.deep.eq("INVALID SCORE");
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
