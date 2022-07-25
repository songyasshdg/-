# -*- coding: utf-8 -*-
import os
import pytest

if __name__ == '__main__':
    pytest.main()
    os.system('allure generate C:\\Users\\Administrator\\a\\Apis\\Reports\\temp -o '
              'C:\\Users\\Administrator\\a\\Apis\\Reports\\report --clean')
    os.system("allure open Reports/report")



