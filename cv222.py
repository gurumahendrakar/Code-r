
import cv2,os,PIL
from mainplayer_body import images


# read input image

#
# os.mkdir('S:/Mage/Leftjump')
object = (cv2.__dict__)
image = object['imread']('S:/Mage/tile.png')
genrated_image = object['hconcat']([image,image]*3)

object['imshow']('image',genrated_image)

object['imwrite']('S:/tilee.png',genrated_image)
object['waitKey'](0)
# for index,image in enumerate(images.rjump):
#     import numpy as np
#     from PIL import Image
#
#     img = np.array(Image.open(image))
#
#     Image.fromarray(np.fliplr(img)).save(f'S:/Mage/Leftjump/Leftjump{index}.png')
#

#

# print(method().__init__)
# class method2(metaclass=method):
#
#
#     def __init__(self,one,two,three):
#         self.name = "guru"
#         self.three = three
#         return None
#
#     def __call__(self, *args, **kwargs):
#         return self.three
#
#
#
# class method():
#
#
#     def __init__(self,one,two,three):
#         print('called')
#
#
#     def __call__(cls, *args, **kwargs):
#         print("How first called")
#
#
#
#



















