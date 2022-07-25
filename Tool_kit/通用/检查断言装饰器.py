# # 断言装饰器
# @pytest.mark.xfail(raises=ZeroDivisionError)
# def test_f():
#     1 / 0
# import pytest
#
#
# def myfunc():
#  raise ValueError("Exception 123 raised")
#
#
# def test_match():
#  with pytest.raises(ValueError) as excinfo:
#   myfunc()
#  assert '123' in str(excinfo.value)