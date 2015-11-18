This is a collection of examples for how to use and extend TensorFlow.

#An advanced example

```python
# This example shows the use of the low level function tf.gradients() 
# [](http://tensorflow.org/api_docs/python/train.html#gradients)
# The definiton of function R=R(x,y) is taken from the example on Wiki 
# [](https://en.wikipedia.org/wiki/Gauss%E2%80%93Newton_algorithm)
# If you are interested in creating new Optimizers for Tensorflow 
#you may want to continue reading this example.
import tensorflow as tf

# define symbolic variables
x = tf.placeholder("float") 
y = tf.placeholder("float")

# define a function R=R(x,y)
R = 0.127-(x*0.194/(y+0.194))

# The derivative of R with respect to y
Rdy = tf.gradients(R, y); 

# Launch a session for the default graph to comput dR/dy at (x,y)=(0.362, 0.556)
sess = tf.Session()
result = sess.run(Rdy, {x:0.362,y:0.556})
print result
#[0.12484978]
``` 

```Java
//The above example actually is implemented in SymJava which provides symbolic-numeric
//computations with just-in-time (JIT) compilation.
//[](https://github.com/yuemingl/SymJava/blob/master/src/symjava/examples/Example0.java)

public class Example0 {
	public static void main(String[] args) {
		Expr R = 0.127-(x*0.194/(y+0.194));
		Expr Rdy = R.diff(y);
		System.out.println(Rdy);
		//Just-In-Time compile the symbolic expression to native code
		BytecodeFunc func = JIT.compile(new Expr[]{x,y}, Rdy);
		System.out.println(func.apply(0.362, 0.556));
	}
}
```
