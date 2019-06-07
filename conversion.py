import os
import re

source_file_name = "conditionals2.md"
source_path = os.path.join("challenges-JS",source_file_name)
target_path = os.path.join("challenges",source_file_name)

test_class_string ='''
```python
import main
import unittest

class TestScript(unittest.TestCase):
    def test1(self):
        # it should
        self.assertIs(type(main.myfunc()), msg="")

    def test2(self):
        #it should
        self.assertTrue(main.myfunc(), msg="")

    def test3(self):
        #it should
        self.assertTrue(main.myfunc(), msg="")

    def test4(self):
        #it should
        self.assertTrue(main.myfunc(), msg="")
```
'''

with open(source_path, "rt") as f:
    data = f.read()
    data = re.sub(r'local-snippet', 'code-snippet', data)
    data = re.sub(r'true', 'True', data)
    data = re.sub(r'false', 'False', data)
    data = re.sub(r'javascript', r'python3.6', data)
    data = re.sub(r'var\s+', '', data)
    data = re.sub(r';', '', data)
    data = re.sub(r'{\s*', ':', data)
    data = re.sub(r'}', '', data)
    data = re.sub(r'\s{0,2}//\s+your code here', '\n    # your code here\n    pass', data)
    data = re.sub(r'//', r'#', data)
    data = re.sub(r'console.log', r'print', data)
    data = re.sub(r'function\s(?!called)', r'def ', data)
#    data = re.sub(r'`js', r'`python', data)
    data = re.sub(r'!tests', "!tests\n"+test_class_string, data)
    data = re.sub(r'\)\s+:', r'):', data)

with open(target_path, "wt") as f:
    f.write(data)
