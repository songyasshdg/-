import os
import time
import pytest

if __name__ == '__main__':
    pytest.main(["-vs", "../Test_Case/test_linjiashon.py", "--alluredir=temp/html"])
    time.sleep(2)
    os.system("allure generate ../Configure/temp/html -o ../report1  --clean")
