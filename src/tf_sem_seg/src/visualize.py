#import scipy.io as sio
import numpy as np
import tensorflow as tf

label_colours = [[128, 64, 128], [244, 35, 231], [69, 69, 69]
                # 0 = road purple, 1 = sidewalk pink, 2 = building grey
                ,[102, 102, 156], [190, 153, 153], [153, 153, 153]
                # 3 = wall light grey, 4 = fence flesh, 5 = pole lightlight grey
                ,[250, 170, 29], [219, 219, 0], [106, 142, 35]
                # 6 = traffic light zonghuangse, 7 = traffic sign huanglvse, 8 = vegetation tuhuangse
                ,[152, 250, 152], [69, 129, 180], [219, 19, 60]
                # 9 = terrain light green, 10 = sky blue, 11 = person red
                ,[255, 0, 0], [0, 0, 142], [0, 0, 69]
                # 12 = rider, 13 = car, 14 = truck
                ,[0, 60, 100], [0, 79, 100], [0, 0, 230]
                # 15 = bus, 16 = train, 17 = motocycle
                ,[119, 10, 32]]
                # 18 = bicycle

matfn = './utils/color150.mat'
#def read_labelcolours(matfn):
#    #mat = sio.loadmat(matfn)
#    color_table = mat['colors']
#    shape = color_table.shape
#    color_list = [tuple(color_table[i]) for i in range(shape[0])]
#
#    return color_list

def decode_labels(mask, img_shape,num_classes):
    
    color_table = label_colours

    color_mat = tf.constant(color_table, dtype=tf.float32)
    onehot_output = tf.one_hot(mask, depth=num_classes)
    onehot_output = tf.reshape(onehot_output, (-1, num_classes))
    pred = tf.matmul(onehot_output, color_mat)
    pred = tf.reshape(pred, (1, img_shape[0], img_shape[1], 3))
    
    return pred

def prepare_label(input_batch, new_size, num_classes, one_hot=True):
    with tf.name_scope('label_encode'):
        input_batch = tf.image.resize_nearest_neighbor(input_batch, new_size) # as labels are integer numbers, need to use NN interp.
        input_batch = tf.squeeze(input_batch, squeeze_dims=[3]) # reducing the channel dimension.
        if one_hot:
            input_batch = tf.one_hot(input_batch, depth=num_classes)
            
    return input_batch
