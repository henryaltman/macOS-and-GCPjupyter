import tensorflow as tf

#

state = tf.Variable(0)
new_value = tf.add(state,tf.constant(1))
update = tf.assign(state,new_value)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(state))
    for item in range(3):
        sess.run(update)
        print(sess.run(state))