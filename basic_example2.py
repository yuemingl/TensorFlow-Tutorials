# This example shows the matrix multiplication
import tensorflow as tf

# Launch a session
sess = tf.Session()

#1x2 matrix
m1=tf.constant([[3.,3.]])
#2x1 matrix
m2=tf.constant([[1.],[2.]])

print sess.run(m1)
#[[ 3.  3.]]
print sess.run(m2)
#[[ 1.]
# [ 2.]]
print sess.run(tf.matmul(m1,m2))
#[[ 9.]]
print sess.run(tf.matmul(m2,m1))
#[[ 3.  3.]
# [ 6.  6.]]

# The operator overloading is not correctly supported now.
# The follow will return the same result
print sess.run(m1*m2)
print sess.run(m1*m2)
#[[ 3.  3.]
# [ 6.  6.]]
