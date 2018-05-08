import tensorflow as tf
import os
import numpy as np
from PIL import Image
import math

def _parse_function(filename):
    image_string = tf.read_file(filename)
    image_decoded = tf.image.decode_jpeg(image_string)
    image_resized = tf.image.resize_images(image_decoded, [224, 224])
    scaling = image_resized / 255 - 0.5
    return scaling

def images_squares_grid(images):
    mode = 'RGB'
    save_size = math.floor(np.sqrt(images.shape[0]))
    # Scale to 0-255
    images = (((images - images.min()) * 255) / (images.max() - images.min())).astype(np.uint8)
    
    # Put images in a square arrangement
    images_in_square = np.reshape(
            images[:save_size*save_size],
            (save_size, save_size, images.shape[1], images.shape[2], images.shape[3]))
    # Combine images to grid image
    new_im = Image.new(mode, (images.shape[2] * save_size, images.shape[1] * save_size))
    for col_i, col_images in enumerate(images_in_square):
        for image_i, image in enumerate(col_images):
            im = Image.fromarray(image, mode)
            new_im.paste(im, (col_i * images.shape[2], image_i * images.shape[1]))
    return new_im


def get_dataset_iterator(dirpath, batch_size, initializable= False):
    image_paths = list(map(lambda x: dirpath+x, os.listdir(dirpath)))
    filenames = tf.constant(image_paths)
    dataset = tf.data.Dataset.from_tensor_slices((filenames))
    dataset = dataset.map(_parse_function)
    dataset.shuffle(buffer_size=10000)
    dataset = dataset.batch(batch_size)
    if initializable:
        iterator = dataset.make_initializable_iterator()
    else:
        iterator = dataset.make_one_shot_iterator()
    return iterator, dataset.output_shapes.as_list()

def save_as_image(images, name):
    images = (((images - images.min()) * 255) / (images.max() - images.min())).astype(np.uint8)

    for i, img in enumerate(images):
        im = Image.fromarray(img)
        im.save("/workspace/data/visualization/{}_generation_{}.jpeg".format(name, i))
