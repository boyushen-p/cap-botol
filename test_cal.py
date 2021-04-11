from Calculator import Calculator
import pytest


# 模块级(setup_module/teardown_module)模块始末，全局的(优先级最高)
# 函数级(setup_function/teardown_function)只对函数用例生效(不在类中)
# 类级**(setup_class/teardown_class) **只在类中前后运行一次(在类中)
# 方法级(setup_method/teardown_method)开始于方法始末(在类中)
# **类里面的(setup/teardown) **运行在调用方法的前后

class TestCal:

    def setup_class(self):
        # setup()是初始化操作
        # 测试类是不允许使用__init__()方法的
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize('a,b,expect', [[1, 1, 2], [0.1, 0.1, 0.2], [1000, 1000, 2000], [-1, 1, 0], [1, -1, 0],
                                            [-0.01, 0.01, 0], [0.01, -0.01, 0], [-0.01, -0.01, -0.02],
                                            [1, 0, 1], [0, 1, 1], [0, 0, 0], [-0.01, 0, -0.01], [0, -0.01, -0.01]],
                             ids=['正整数', '正小数',
                                  '正胜数（大）', '负整与正整', '正整与负整', '负小数与正小数', '正小数与负小数', '负小数与负小数',
                                  '正整数与0', '0与正整数', '0与0', '负小数与0', '0与负小数'])
    def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize('a,b,expect', [[-1, 1, -1], [10, 5, 2], [0, 10, 0], [-0.2, 0.5, -0.4]],
                             ids=['-1与1', '10与5', '0与10', '-0.2与0.5'])
    def test_div(self, a, b, expect):
        assert expect == self.calc.div(a, b)


@pytest.mark.parametrize('a, b', [
    [1, 1], [100, 100]
])
@pytest.mark.skip(reason='学习代码,暂不执行')
class TestDemo:
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("结束计算")

    def test_a(self, a, b):
        print(a, b)

    def test_b(self, a, b):
        print(a, b)


# a: int,str,float
# b: 1,2,3
# c: x, y, z
# 笛卡尔积

def setup_function():
    print("开始计算")


def teardown_function():
    print("结束计算")


@pytest.mark.parametrize('c', ['x', 'y', 'z'])
@pytest.mark.parametrize('b', [1, 2, 3])
@pytest.mark.parametrize('a, d', [['int', 'a'], ['str', 'b'], ['float', 'c']])
@pytest.mark.skip(reason='学习代码,暂不执行')
def test_ab(a, d, b, c):
    print(a, d, b, c)
