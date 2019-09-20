class QueueError(Exception):
    pass

# 树形结构的子集（线性结构）的数据结构和算法 ，可以用在树形结构中【子集的数据结构和算法，可以被父集使用，似乎是一种自下而上的复用】，其中遍历的方法是（“移动的根节点”+打印根节点），移动的方法是由嵌套的结构决定的。
class SQueue:
    def __init__(self):   # 将被模拟对象：队列，看成一个由另一个逻辑实体限制下的逻辑实体  001
        self.elements = []

    def is_empty(self):     # 查
        return self.elements == []

    def enqueue(self, elem):    # 增
        self.elements.append(elem)  # 改变局部状态以反映质能的变化

    def dequeue(self, elem):        # 查&删
        if not self.elements:       # 分情况，反面情况优先
            raise QueueError('Queue is empty')
        return self.elements.pop(0)  # 改变局部状态以反映质能的变化

class TreeNode:
      # 将被模拟对象：二叉树，看成一个由三个部分组成的逻辑实体  000   --- 比线性结构多一维，线性结构因此成为树形结构的特殊
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right



class Bitree:
    def __init__(self, root=None):  
        self.root = root        # 添加被模拟对象：树：的限制条件 ？？？

    def preOrder(self, node):
        if node is None:        # 分情况，反面情况优先
            return
        print(node.data, end=' ')
        self.preOrder(node.left)    # 递归作为一种延时求值技术
        self.preOrder(node.right)

    def inOrder(self, node):    # 递归函数内的实际（普通）代码只有三行
        if node is None:        # 1，是不是 None
            return              #    如果是 则返回到上一层函数
        self.inOrder(node.left) # 递归，递归结构:延时求值,直到最左下的节点left遇到 None
        print(node.data, end=' ')  # 2，不是 None 就打印(当前节点),实际与结构的结合点
        self.inOrder(node.right)# 递归，递归结构:延时求值,仅当访问过根节点才能访问right

    def postOrder(self, node):
        if node is None:
            return
        self.postOrder(node.left)   # 由于是嵌套函数，内部执行完会返回到外层继续向下执行
        self.postOrder(node.right)
        print(node.data, end=' ')   # 程序至上而下执行，要访问根节点将先会陷入上面的嵌套
        
        

if __name__ == "__main__":
  # 　后序遍历　ＢＦＧＤＩＨＥＣＡ
  # 构建树 (笔记中)
  b = TreeNode('B')
  f = TreeNode('F')
  g = TreeNode('G')
  d = TreeNode('D', f, g)
  i = TreeNode('I')
  h = TreeNode('H')
  e = TreeNode('E', i, h)
  c = TreeNode('C', d, e)
  a = TreeNode('A', b, c)  # 树根

  # 　初始化树对象，得到树根
  bt = Bitree(a)
  #　先序
  bt.preOrder(bt.root)
  print()
  # 　中序
  bt.inOrder(bt.root)
  print()
#   bt.postOrder(bt.root)
#   print()
#   bt.levelOrder(bt.root)
#   print()
