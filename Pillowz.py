from PIL import Image, ImageFilter, ImageEnhance
# Open an image file
image = Image.open('Alex.png')
print("Original Image Size:", image.size)

# Resize the image
resized_image = image.resize((300, 300))
resized_image.save('Alex_resized.png')
print("Resized Image Size:", resized_image.size)

# Display the image
resized_image.show()

# Rotate the image
rotated_image = image.rotate(45)
rotated_image.save('Alex_rotated.png')
rotated_image.show()

