import tensorflow as tf
with tf.Graph().as_default() as graph:
    var = tf.constant(['Tensorflow 基础教程做的不错 中午加肉肉',
    'Tensorboard 做的也很棒',
    '你是⼀一个全能型选⼿手'])
    text = tf.summary.text('text', var)
with tf.Session(graph=graph) as sess:
    writer = tf.summary.FileWriter('./graphs')
    writer.add_graph(graph)
    sess.run(tf.global_variables_initializer())
    summaries, _ = sess.run([text, var])
    writer.add_summary(summaries)
writer.close()