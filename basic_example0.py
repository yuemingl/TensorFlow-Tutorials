import tensorflow as tf

# define symbolic variables
x = tf.placeholder("float") 
y = tf.placeholder("float")

# Launch a session for the default graph to comput sqrt(x^2,y^2) with parameters x=3, y=4.
sess = tf.Session()
result = sess.run(tf.sqrt((x*x+y*y)), {x:3,y:4})
print result
#5.0
