from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_fcn import fcn8_vgg

import tensorflow as tf


def inference(hypes, images, phase='train'):
    """Build the MNIST model up to where it may be used for inference.

    Args:
      images: Images placeholder, from inputs().
      train: whether the network is used for train of inference

    Returns:
      softmax_linear: Output tensor with the computed logits.
    """
    train = (phase == 'train')
    vgg_fcn = fcn8_vgg.FCN8VGG()

    if not train:
        tf.get_variable_scope().reuse_variables()

    num_classes = hypes["fc_size"]
    vgg_fcn.build(images, train=train, num_classes=num_classes,
                  random_init_fc8=True)

    vgg_dict = {'deep_feat': vgg_fcn.pool5,
                'deep_feat_channels': 512,
                'early_feat': vgg_fcn.conv4_3,
                'scored_feat': vgg_fcn.score_fr}

    return vgg_dict
