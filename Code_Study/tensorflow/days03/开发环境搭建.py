"""
    python 虚拟环境可以让你不需要两个机器就能跑两套环境 - virtualenv
"""


import tensorflow as tf

hello = tf.constant('Hello TensorFlow')

sess = tf.Session()   # with语句操作上下文环境，会话也是一种上下文环境

print(sess.run(hello))