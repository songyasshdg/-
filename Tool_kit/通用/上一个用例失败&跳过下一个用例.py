# 基本用法
# pip install pytest-dependency
# @pytest.mark.dependency(name=None, depends=0, scope='module')
#
#
# import pytest
#
#
# @pytest.mark.dependency()  # 代表这条用例为主条件
# @pytest.mark.xfail(reason="deliberate fail")  # 标记为xfail
# def test_a():
#     assert False  # 故意让test_a失败，后续依赖于test_a的用例均会跳过
#
#
# @pytest.mark.dependency()
# def test_b():
#     pass  # test_b成功，后续依赖于test_b的用例均会执行，不会跳过
#
#
# @pytest.mark.dependency(depends=["test_a"])
# def test_c():
#     pass  # test_c依赖于test_a，所以直接跳过
#
#
# @pytest.mark.dependency(depends=["test_b"])
# def test_d():
#     pass  # test_d依赖于test_b，由于b是成功的，所以test_d会执行通过
#
#
# @pytest.mark.dependency(depends=["test_b", "test_c"])
# def test_e():
#     pass  # test_e取决于test_b和test_c。test_b确实成功了，但test_c已被跳过。所以这一个也将被跳过。

# 依赖范围scope------------------------------------------
# import pytest
#
#
# class Test1(object):
#
#     @pytest.mark.dependency()
#     @pytest.mark.xfail()
#     def test_a(self):
#         assert False
#
#
# class Test2(object):
#
#     @pytest.mark.dependency()
#     def test_a(self):
#         pass
#
#     @pytest.mark.dependency(depends=["test_a"], scope="class")
#     def test_b(self):
#         pass

import pytest

#
# @pytest.mark.dependency()
# @pytest.mark.xfail()
# def test_a():
#     assert False
#
#
# class Test1(object):
#
#     @pytest.mark.dependency()
#     def test_a(self):
#         pass
#
#
# class Test2(object):
#
#     @pytest.mark.dependency()
#     def test_a(self):
#         pass
#
#     @pytest.mark.dependency(depends=["test_a"], scope="module")
#     def test_b(self):
#         pass