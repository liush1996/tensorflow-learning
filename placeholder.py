import tensorflow as tf
a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)
add = tf.add(a, b)
multiply = tf.multiply(a, b)
with tf.Session() as sess:
    print "Addition with variables: %i" %sess.run(add, feed_dict={a: 2, b: 3})
    print "Multiplication with variables: %i" %sess.run(multiply, feed_dict={a: 2, b: 3})