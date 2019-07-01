import os
import re

source_file_name = "arraymethods8.md"
source_path = os.path.join("challenges-JS", source_file_name)
target_path = os.path.join("challenges", source_file_name)

test_class_string = '''
```python
import main
import unittest

class TestScript(unittest.TestCase):
    def test1(self):
        # it
        self.assertIs(type(main.myfunc()), bool,
        msg =  )

    def test2(self):
        # it
        self.assertEqual(main.myfunc(), correct_answer,
        msg = )

    def test3(self):
        # it
        self.assertEqual(main.myfunc(), correct_answer,
        msg = )

    def test4(self):
        # it
        self.assertEqual(main.myfunc(), correct_answer,
        msg = )

    def test5(self):
        # it
        self.assertEqual(main.myfunc(), correct_answer,
        msg = )

    def test6(self):
        # it
        self.assertTrue(main.myfunc(),
        msg = )

```
'''

with open(source_path, "rt") as f:
    data = f.read()
data = unicodedata.normalize("NFKD", data)


describe = re.compile(r'describe[^`]*')
describe_blocks = describe.findall(string)
function_name = re.compile(r'describe\(\"([A-z]*)')
test_description = re.compile(r'it\("([^"]*)')
expected_result = re.compile(r'eq\(([^\)]*)\)')

test_object = {}

for block in describe_blocks:
    name = function_name.findall(block)[0]
    function_with_args = re.compile(r'{}\([^)]+\)'.format(name))
    test_object[name] = list(zip(function_with_args.findall(block),
                                 expected_result.findall(block),
                                 test_description.findall(block)))    

data = re.sub(r'local-snippet', 'code-snippet', data)
data = re.sub(r'true', 'True', data)
data = re.sub(r'false', 'False', data)
data = re.sub(r'javascript', r'python3.6', data)
data = re.sub(r'var\s+', '', data)
data = re.sub(r';', '', data) #everyone hates semicolons, amirite?
data = re.sub(r'{\s*', ':', data)
data = re.sub(r'}', '', data)
data = re.sub(r'\s{0,2}//\s+your code here', '\n    # your code here\n    pass', data)
data = re.sub(r'//', r'#', data) #pythonic comments
data = re.sub(r'console.log', r'print', data) #python print statement
data = re.sub(r'function\s(?!called)', r'def ', data) #function -> def
data = re.sub(r'`js', r'`python', data)
data = re.sub(r'!tests', "!tests\n"+test_class_string, data)
data = re.sub(r'\)\s+:', r'):', data)

with open(target_path, "wt") as f:
    f.write(data)
