'''
    单例模式，要确保只有一个实例对象存在，以确保所有信息都从这个对象获取（类比管程）
    【系统的配置对象，线程池，减少数据库连接次数】
    新加入装饰者模式啦

    思路：
    只需要找一个变量存放创建的实例，
    然后每次获取实例时，先检查变量中是否已保存实例，
    如果没有则创建一个实例并将其存放到变量中，以后都从这个变量中获取实例就可以了。
    单例模式中，只会创建一次实例。
'''

class Singleton(object):
    """
    单例的类装饰器实现，【不能用于多线程环境】
    """
    def __init__(self,cls):   # 传入一个类
        self.cls = cls

    def instance(self):   # 也是使用内置的属性 Singleton._instance 来存储实例的
        """
        返回真正的实例
        """
        try:
            return self.instance_
        except AttributeError:
            self.instance_ = self.cls()
            return self.instance_

    def __call__(self, *args, **kwargs):
        raise TypeError('Singletons must be accessed through "instance".')

    def __instancecheck__(self, inst):
        return isinstance(inst,self._decorated)   # ????


@Singleton
class A:
    '''
    这是某个需要单例模式的类
    '''

    def __init__(self):
        pass

    def display(self):
        return id(self)


if __name__ == '__main__':
    s1 = A.Instance()
    s2 = A.Instance()
    print(s1, s1.display())
    print(s2, s2.display())
    print(s1 is s2)     # True
    # 会发现 s1 和 s2 的 id 是相同的。

