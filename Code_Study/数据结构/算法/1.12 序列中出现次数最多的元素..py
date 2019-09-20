"""
    怎样找出一个序列中出现次数最多的元素呢？
"""

# collections.Counter 类就是专门为这类问题而设计的， 它甚至有一个有用的 most_common() 方法直接给了你答案。
# 假设你有一个单词列表并且想找出哪个单词出现频率最高。你可以这样做：

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter
word_count = Counter(words)

top_three = word_count.most_common(3)   # 出现频率最高的3个单词


# Counter 对象可以接受任意的由可哈希（hashable）元素构成的序列对象作为输入。
# 在底层实现上，一个 Counter 对象就是一个字典，将元素映射到它出现的次数上。