from random import random
import numpy as np
from copy import deepcopy
from PIL import Image
import cv2
import numpy as np
import os

from scipy import linalg


def compute_homography(pair1, pair2, pair3, pair4):
    """
    Compute the homography matrix between two sets of corresponding points using RANSAC.

    Args:
    - pair1: 4-tuple of (x1,y1,x2,y2) coordinates of corresponding points.
    - pair2: 4-tuple of (x1,y1,x2,y2) coordinates of corresponding points.
    - pair3: 4-tuple of (x1,y1,x2,y2) coordinates of corresponding points.
    - pair4: 4-tuple of (x1,y1,x2,y2) coordinates of corresponding points.

    Returns:
    - H: 3x3 homography matrix.
    """

    rrefmatr = []
    avec = []
    for pointpair in [pair1, pair2, pair3, pair4]:

        x1, y1, x2, y2 = pointpair[0], pointpair[1], pointpair[2], pointpair[3]
        rrefmatr.append([x1, y1, 1, 0, 0, 0, -x1 * x2, -y1 * x2])
        rrefmatr.append([0, 0, 0, x1, y1, 1, -x1 * y2, -y1 * y2])
        avec.extend([x2, y2])

    rrefmatr = np.asarray(rrefmatr)
    avec = np.asarray(avec)
    try:
        sol = np.matmul(linalg.inv(rrefmatr), np.transpose(avec))
    except:
        return np.zeros([3, 3])
    return np.asarray([[sol[0], sol[1], sol[2]],
                       [sol[3], sol[4], sol[5]],
                       [sol[6], sol[7], 1]])


fp = os.path.dirname(__file__)

sourceim = "DanaOffice/DSC_0308.JPG"

addim = "pika.jpg"


image = cv2.imread(f"{fp}/{sourceim}")
imagergb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
imagepil = Image.fromarray(imagergb)

image2 = cv2.imread(f"{fp}/{addim}")
imagergb2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

print(image2.shape)
points = [(0, 0), (0, 131), (149, 0), (146, 131)]
# points = [(91, 375), (75, 481), (165, 373), (175, 480)]
# [(113, 247), (98, 302), (210, 232), (226, 280)]
# [(305, 236), (298, 294), (340, 242), (335, 313)]

(imrows, imcols, _) = image2.shape
pointpairs = \
    [(0, 0, *points[0]),
        (0, imcols, *points[1]),
        (imrows, 0, *points[2]),
        (imrows, imcols, *points[3])]

hg = compute_homography(*pointpairs)

newimg = deepcopy(imagergb)
for pr in range(0, imrows):
    for pc in range(0, imcols):
        dst = np.matmul(hg, np.transpose(np.asarray([pr, pc, 1])))
        (destr, destc, _) = dst / dst[2]
        newimg[int(destr), int(destc), :] = imagergb2[pr, pc, :]
pilimage = Image.fromarray(newimg)


name = "applied_%s.jpg" % (int(100*random()))
pilimage.save(f"{fp}/insert/{name}", "JPEG")
