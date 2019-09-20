class StackError(Exception):
    pass
class SStack:
    def __init__(self):       # 将被模拟对象：栈，看成一个由以个部分组成的逻辑实体 000
        self.elements = []    # 使用指定变量接收外部数据     112

    def is_empty(self):       # 有没有
        return self.elements == []   # 变量作为要反映出去的信息  011

    def push(self, elem):
        self.elements.append(elem)   # 改变局部状态以反映质能的变化

    def pop(self):
        if not self.elements:   # 分情况，反面情况优先
            raise StackError
        return self.elements.pop()  # 局部状态作为输出

    def show_top(self):
        if not self.elements:   # 分情况，反面情况优先
            raise StackError
        return self.elements[-1]    # 局部状态作为输出

"""
    功能：检查括号
"""


text = "Open source software is made better when users (can easily) contribute code and [documentation] to fix bugs and add {fea(tures).} Python {strongly} encoura[ges community] (in{vo}lv[em]ent) in improving the software. Learn more about how to make Python better for everyone."

parens = "(){}[]"
left_parens = "({["
opposite = {'}':'{',']':'[',')':'('}    # 变量作为目标状态信息的标识符

st = SStack()  # 变量作为数据结构的名称

def parent(text):
    i, text_len = 0, len(text)
    while 1:
        while i < text_len and text[i] not in parens:
            i += 1
    if i >= text_len:
        return
    else:
        yield text[i], i
        i += 1

def verify():
    for pr, i in parent(text):    # 函数作为一个过程中的一部分
        if pr in left_parens:
            st.push((pr,i))   
        elif st.is_empty() or st.pop()[0] != opposite[pr]:
            print('No match is found at %d for %s'%(i, pr))
            break
    else:
        if st.is_empty():
            print('All parentheses are matched.')
        else:
            p = st.pop()
            print('No match is found at %d for %s'%(p[1],p[0]))
