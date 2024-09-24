from skimage.transform import resize

def resize(img, properties):
    assert 0 <= properties <= 1, "specify a value between 0 and 1"
    height = int(img.shape[0] * properties)
    width = int(img.shape[1] * properties)
    img_resize = resize(img, (height, width), anti_aliasing=True)

    return img_resize