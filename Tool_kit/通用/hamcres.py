from hamcrest import *
import pytest
from hamcrest import *


# 安装：
# pip install pyhamcrest
#
# 导入：
# from hamcrest import *
@pytest.mark.parametrize("price, expect_price, delta", [
    (96.0, 100, 0.05), (101, 96, 0.1), (90, 100, 0.05)
])
def test_demo(price, expect_price, delta):
    print(price, ",", round(expect_price * delta, 2), ",", expect_price - expect_price * delta, ",",
          expect_price + expect_price * delta)
    assert_that(price, close_to(expect_price, round(expect_price * delta, 2)))
    assert_that()
    assert_that("this is a string", equal_to("this is a string"))
    assert_that(1.0, close_to(0.5, 0.5))
    assert_that('abc', contains_string('a'))
# 常用方法
# equal_to(obj): 比较两个对象
#
# close_to(value, delta): 比较两个值是否接近，范围：[value-delta, value+delta]
#
# contains_string(substring: str)：包含某个字符
