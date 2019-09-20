import tensorflow as tf

# 先写好文本程序，再交给Session会话函数去初始化、执行。

x = tf.Variable([[0.5,1.0]])
y = tf.Variable([[2.0],[1.0]])
z = tf.matmul(x,y)

init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op)
    print(z.eval())