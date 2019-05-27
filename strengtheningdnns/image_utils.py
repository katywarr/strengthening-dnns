import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


def image_from_file(image_path, required_size=None):
    """Imports an image from a file and represents it as a numpy array. 

    Args:
        image_path: The file location of the image to be uploaded.
        required_size: The required size of the image

    Returns:
        A `numpy` array.

    Raises:
        TypeError: If the `required_size` is not 2D
    """

    if (len(required_size) != 2):
        raise TypeError("The required_shape should be 2D of the form (224,224). The shape passed was: ", required_size)

    raw_image = tf.read_file(image_path)
    image = tf.image.decode_jpeg(raw_image)
    print(image.shape)
    if (required_size != None):
        print('Re-scaling image to ', required_size)
        image = tf.image.resize_images(image, required_size)    
    #image /= 255.0  # normalize to [0,1] range

    with tf.Session().as_default():
    #image = np.asarray(image/255)  
        return image.eval().astype(int)


def show_images_and_predictions(model, images, expected_labels, class_names):
    predictions = model.predict(images)

    plt.figure(figsize=(15, 30))
    for i in range(10):
        plt.subplot(10, 5, i + 1)
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(images[i], cmap=plt.cm.binary)
        predicted_label = np.argmax(predictions[i])
        if predicted_label == expected_labels[i]:
            color = 'blue'
        else:
            color = 'red'

        plt.xlabel("{} ({})".format(class_names[predicted_label],
                                    class_names[expected_labels[i]]),
                                    color=color)


from numpy import linalg as LA


def display_lp_norms(difference):
    diff_flat = difference.flatten()

    l0 = np.sum(diff_flat != 0)
    percentl0 = (l0 / np.size(difference)) * 100
    l2 = LA.norm(diff_flat, 2) # (np.sum(diff_flat ** 2)) ** 0.5
    linf = LA.norm(diff_flat, np.inf) # np.max(np.abs(diff_flat))
    print("Distance measurements: ")
    print("    L0:   ", "{:.2f}".format(l0), "(", "{:.2f}".format(percentl0), "%)")
    print("    L2:   ", "{:.2f}".format(l2))
    print("    Linf: ", "{:.2f}".format(linf))
