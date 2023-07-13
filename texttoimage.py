from PIL import Image, ImageDraw, ImageFont

# Ask the user to enter the text to be used for the image
text = input("Enter the text to be used for the image: ")

# Ask the user to enter a filename for the output image
filename = input("Enter a filename for the output image (without extension): ")

# Set the font to be used for the text
font = ImageFont.truetype("Arial.ttf", 48)

# Set the dimensions of the image
width = 400
height = 200

# Create a new image object
image = Image.new("RGB", (width, height), (255, 255, 255))

# Create a draw object for the image
draw = ImageDraw.Draw(image)

# Calculate the size of the text
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

# Calculate the position of the text
x = (width - text_width) / 2
y = (height - text_height) / 2

# Draw the text on the image
draw.text((x, y), text, font=font, fill=(0, 0, 0))

# Save the image to a file with the specified filename
image.save(f"{filename}.png")
