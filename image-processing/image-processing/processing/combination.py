import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def difference(img1, img2):
    assert img1.shape == img2.shape, "specify the same shape"
    img1_gray = rgb2gray(img1)
    img2_gray = rgb2gray(img2)
    (score, diff) = structural_similarity(img1_gray, img2_gray, full=True)
    print("Similarity: {:.4f}".format(score))
    normalized = (diff - np.min(diff) / (np.max(diff)) - np.min(diff))

    return normalized

def histogram_transfer(img1, img2):
    math_img = match_histograms(img1, img2, multichannel=True)
    return math_img