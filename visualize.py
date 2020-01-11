import numpy as np
import cv2


"""
Volumetric Viewer: A simple interactive viewer of volumetric data in sequence of slice images.
 
 Use 'W' and 'S' button to view slices
  W -> Forward
  S -> Backward

Press ESC button to exit the program.
"""


# Helpers
def normalize(image):

    """
       Normalize the input tensor to [0,1].
    """

    image = (image - MIN_BOUND) / (MAX_BOUND - MIN_BOUND)
    image[image>1] = 1.
    image[image<0] = 0.
    return image


# Read the volumetric data
# Volume is in Depth, Width, Height format
img_3d = np.load("3D_vol.npy")

# Transpose to Width, Height, Depth format
img_3d = np.transpose(img_3d)

# Normalize
MIN_BOUND = np.min(img_3d)
MAX_BOUND = np.max(img_3d)
    
img_3d = normalize(img_3d)
print("Dimension of the volume: ", img_3d.shape)


counter = 0
window = np.array((1,2))

while True:

    if counter >= img_3d.shape[-1]:
        break

    window = img_3d[:,:,counter]

    cv2.imshow("Volumetric Viewer".format(counter), window)
    
    k = cv2.waitKey(1) & 0xff

    if k != 255:

        if k == 119:

            #print("forward")
            counter+=1
            print("Slice number: ", counter)
            
        if k == 115:

            #print("backward")
            counter-=1
            print("Slice number: ",counter)

    if k == 27: 
        break

print("All slices shown")
cv2.destroyAllWindows()
