import os
import re

source_file_name = "conditional1.md"
source_path = os.path.join("challenges",source_file_name)
target_path = os.path.join("testing",source_file_name)


with open(source_path, "rt") as f:
    data = f.read()

data = re.sub(r'javascript',r'python3.6',data)
data = re.sub(r'var','',data)
data = re.sub(r';','',data)
data = re.sub(r'//\s*your code here','# your code here\n\t\\pass',data)
data = re.sub(r'//',r'#',data)
data = re.sub(r'console.log',r'print',data)
data = re.sub(r'function',r'def',data)
data = re.sub(r'`js',r'`python3.6',data)
data = re.sub(r'!tests',"!tests\n'''",data)
data = re.sub(r'!end-tests',"'''\n!end-tests",data)

with open(target_path, "wt") as f:
    f.write(data)
