from multiprocessing.pool import Pool
from spider import get_url
from get_image import get_images
from get_image import save_images


def func(offset):
    json = get_url(offset)
    x = get_images(json)
    for item in x:
        save_images(item)


page_start = 0
page_end = 5

if __name__ == '__main__':
    pool = Pool(5)
    groups = [x * 20 for x in range(page_start, page_end)]
    pool.map(func, groups)
