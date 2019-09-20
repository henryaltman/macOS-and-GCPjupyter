"""
     when we work with TensorFlow,
     it is the same as defining a series of operations in a Graph.
"""


import tensorflow as tf


# Building a Graph
graph1 = tf.Graph()

with graph1.as_default():
    a = tf.constant([2],name = 'constant_a')
    b = tf.constant([3],name = 'constant_b')

a