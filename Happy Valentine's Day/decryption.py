import io

from PIL import Image
from itertools import cycle

def xor(a, b):
  return [i^j for i, j in zip(a, cycle(b))]

# Convert the key from decimal to bytes
key = bytes([137, 80, 78, 71, 13, 10, 26, 10])

f = open("enc (1).txt", "rb").read()

dec = bytearray(xor(f,key))

try:
  # Attempt to open and display the decrypted image
  img = Image.open(io.BytesIO(dec))
  img.show()
except (OSError, IOError):
  # Handle potential errors like missing dependencies or incompatible formats
  print("Error: Could not display the image.")

# Save the decrypted image as well (optional)
open('decrypted.png', 'wb').write(dec)
