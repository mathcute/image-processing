from skimage.io import imread, imsave

def read_image(path, is_grayscale= False):
    img = imread(path, is_grayscale = is_grayscale)

    return img

def save_image(img, path):
    imsave(path, img)