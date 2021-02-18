import tensorflow as tf
import numpy as np
# data = np.loadtxt('data/zoo/zoo.csv', delimiter=',')
# print(data)
# ydata = data[:10, -1:]
# print(ydata)
# y = tf.placeholder(tf.int64, [None, 1])
# onehot1 = tf.one_hot(y, 7)
# onehot2 = tf.reshape(onehot1, [-1, 7])
# argmax1 = tf.argmax(onehot2, 1)d
# argmax2 = tf.reshape(argmax1, [-1, 1])
# sess = tf.Session()
# equal1 = tf.equal(y, argmax2)
# cast1 = tf.cast(equal1, tf.float32)
# mean1 = tf.reduce_mean(cast1)
#
# print('y =',sess.run(y, feed_dict={y: ydata}))
# print('onehot1 =', sess.run(onehot1, feed_dict={y: ydata}))
# print('onehot2 =', sess.run(onehot2, feed_dict={y: ydata}))
# print('argmax1 =', sess.run(argmax1, feed_dict={y: ydata}))
# print('argmax2 =', sess.run(argmax2, feed_dict={y: ydata}))
# print('equal1 =', sess.run(equal1, feed_dict={y: ydata}))
# print('mean1 =', sess.run(mean1, feed_dict={y: ydata}))
#
# sess.close()

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('data/wine.csv', sep=';')
print(data)
s1 = data.groupby('quality').size()
print(s1)
plt.plot(s1)
# plt.show()
plt.savefig('img\\wine.png')

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 5]])
print(a)
print(a[:, -1])
# 5보다 작은 경우 0
# 5이상 8이하 9

print('1번', a[:, -1] < 5)
print('2번', a[a[:, -1] < 5])
a[a[:, -1] < 5, -1] = 0
print('3번', a)
a[(a[:, -1] >=  5) & (a[:, -1] <= 8), -1]=9
print('4번', a)