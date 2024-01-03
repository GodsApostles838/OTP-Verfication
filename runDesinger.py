import subprocess
import os
from constructions import returnOutput

directory_path = r"/OTP-Verfication"
os.chdir(directory_path)
subprocess.run(["cmd", "/k", "pyside6-designer"])

if subprocess.check_output(["tasklist", "/FI", "imagename eq pyside6-designer.exe"]):
    returnOutput("Status", '401')
else:
    returnOutput("Status", '201')
