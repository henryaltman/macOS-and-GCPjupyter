'''
    单例模式，要确保只有一个实例对象存在，以确保所有信息都从这个对象获取（类比管程）
    【系统的配置对象，线程池，减少数据库连接次数】

    思路：
    只需要找一个变量存放创建的实例，     ----   有一
    「然后每次获取实例时，先检查变量中是否已保存实例，
    如果没有则创建一个实例并将其存放到变量中，以后都从这个变量中获取实例就可以了。」  ---- 唯一
    单例模式中，只会创建一次实例。

'''

class Singleton(object):
    """
    单例模式
    """
    class A_(object):
        """
        被隐藏的真正干活的类。。。
        """
        def __init__(self):
            pass

        def display(self):
            # 这个返回结果会是全局唯一的，保证只有一个实力对象
            return id(self)

    """
    以下是外层类的功能：主要是壳，判断是否允许某种操作
    """
    # 先创建类变量，用于存储 A_ 的实例对象
    instance_ = None

    def __init__(self):
        # 先判断类变量中有没有已经生成的 A_（实际干活）实例，没有则创建并返回
        if Singleton.instance_ is None:     # 只有第一次实例化会调用被隐藏的类
            Singleton.instance_ = Singleton.A_()    # 第一次指向的类是外层.里层() 的实例化，所以最后是里层的属性被操作

    def __getattr__(self, attr):
        # 修改__getattr__确保所有属性都从指定的地方（这里是类变量）获取
        return getattr(self.instance_,attr)


if __name__ == '__main__':
    s1 = Singleton()  # 以后每次初始化 Singleton 时都从 Singleton._instance 获取真正干活的实例
    s2 = Singleton()
    print(id(s1),s1.display())
    print(id(s2),s2.display())
    # 结果是 s1 s2 的实例方法所操作的（这里是 displace（））属性都是同样的，尽管他们不是同一对象
