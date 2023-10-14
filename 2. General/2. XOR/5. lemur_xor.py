from PIL import Image
import numpy as np

# Load the two PNG images
image1 = Image.open('f1.png')
image2 = Image.open('f2.png')

# Ensure that the images have the same size
if image1.size != image2.size:
    raise ValueError("Images must have the same dimensions")

# Convert images to numpy arrays for faster processing
array1 = np.array(image1)
array2 = np.array(image2)

# Perform the XOR operation
result_array = np.bitwise_xor(array1, array2)

# Convert the resulting numpy array back to an image
result_image = Image.fromarray(result_array)

# Save the result as a new PNG image
result_image.save('result.png')
