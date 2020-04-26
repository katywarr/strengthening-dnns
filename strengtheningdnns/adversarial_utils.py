import foolbox
from foolbox import attacks

import numpy as np
from numpy import linalg as LA


def generate_adversarial_data(original_images,
                              predictions,
                              attack_fn,
                              verbose = False):

    """
    Generates adversarial data based on a specific FoolBos attack

    Args:
        original_images: The original images from which to generate the data.
        predictions: The original image predictions
        attack_fn: The required adversarial attack function

    Returns:
        A `numpy` array of the generated adversarial objects
        A `numpy' array of perturbation metrics (dict)
        A `numpy' array of the original (non-adversarial) labels associated with the adversarial images

    Raises:

    """
    num_original_images = original_images.shape[0]

    image_dimension = len(original_images.shape)-1
    if image_dimension == 2:  # Monochrome images 
        adv_images = np.empty((0, original_images.shape[1], original_images.shape[2]), dtype=int)
    else: 
        if image_dimension == 3:  # Colour images
            adv_images = np.empty((0, original_images.shape[1], original_images.shape[2], original_images.shape[3]), dtype=int)
        else:  # Error case
            print('Error: Original images array was not a valid dimension for monochrome or colour images')
            return [], [], []

    l0_norms = np.empty(0, dtype=float)
    l2_norms = np.empty(0, dtype=float)
    linf_norms = np.empty(0, dtype=float)
    foolbox_diff = np.empty(0, dtype=float)

    x_labels = np.empty(0, dtype=int)

    for x_num in range(num_original_images):

        x_adv = None
        x = original_images[x_num]
        y = np.argmax(predictions[x_num])

        x_adv = attack_fn(input_or_adv=x, label=y, unpack=False)

        if verbose:
            print("Image: ",  x_num, " Prediction: ", x_adv.adversarial_class, "(", y, ")")
        if (x_adv is not None) and (x_adv.image is not None):
            x_adv_image = x_adv.image
            adv_images = np.append(adv_images, np.expand_dims(x_adv_image, axis=0), axis=0)
            x_labels = np.append(x_labels, y)

            diff = (x_adv.image - x).flatten()
            l0_norms = np.append(l0_norms, LA.norm(diff, 0))
            l2_norms = np.append(l2_norms, LA.norm(diff, 2))
            linf_norms = np.append(linf_norms, LA.norm(diff, np.inf))
            foolbox_diff = np.append(foolbox_diff, x_adv.distance.value)
            if verbose:
                print("Distance: ",  x_adv.distance)
        else:
            print('Warning: Unable to find adversarial example for image at index: ', x_num)

    adv_perturbs = {
        "l0_norms": l0_norms,
        "l2_norms": l2_norms,
        "linf_norms": linf_norms,
        "foolbox_diff": foolbox_diff
    }
    return adv_images, adv_perturbs, x_labels
