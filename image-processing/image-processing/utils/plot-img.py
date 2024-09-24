import matplotlib.pyplot as plt

def plot_img(img):
    plt.figure(figsize = (12, 4))
    plt.imshow(img, cmap = 'gray')
    plt.axis('off')
    plt.show()

def result_plot(*args):
    number_of_imgs = len(args)
    fig, axis = plt.subplots(nrows = 1, ncols = number_of_imgs, figsize = (12, 4))
    names_lst = ['Image 1()'.format(i) for i in range(i, number_of_imgs)]
    names_lst.append('Result')

    for ax, name, img in zip(axis, names_lst, args):

        ax.set_title(name)
        ax.imshow(img, cmap = 'gray')
        ax.axis('off')
    
    fig.tight_layout()
    plt.show()

def histogram_plot(img):
    fig, axis = plt.subplots(nrows = 1, ncols = 3, figsize = (12, 4), sharex = True, sharey = True)
    color_lst = ['red', 'green', 'blue']
    
    for index, (ax, color) in enumerate(zip, (axis, color_lst)):

        ax.set_title('Histogram'.format(color.title()))
        ax.hist(img[:, :, index].raveel(), bins = 256, color = color, alpha = 0.8)

    fig.tight_layout()
    plt.show()