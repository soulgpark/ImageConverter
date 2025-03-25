# ImageConverter
Image converter transforms images into cartoon style representation using OpenCV. It takes a photo as input and applies edge highlighting and color filtering to create a cartoon effect.

## Features
- **Load Image**: Uses OpenCV to read the input image and resize it to 500x500 pixels.
- **Convert to Grayscale**: Converts the image to grayscale to simplify edge detection.
- **Reduce Noise**: Applies medianBlur to reduce noise.
- **Edge Detection**: Uses adaptiveThreshold to emphasize image contours.
- **Color Filtering**: Applies bilateralFilter to smooth colors while preserving details.
- **Apply Cartoon Effect**: Combines the edge-detected image as a mask with the color-filtered image.

## Output
**Images That Work Well**
Images with simple colors and strong outlines
![realcat](https://github.com/user-attachments/assets/93c15d43-871f-48d6-aaee-6389ccb1ccea)
![cat](https://github.com/user-attachments/assets/003c5979-547f-4f98-b8ca-3901c56f1e4e)

**Images That Do Not Work Well**
Images with blurry edges
![realsea](https://github.com/user-attachments/assets/64e16585-c686-4b7c-a971-552fa206fcd7)
![sea](https://github.com/user-attachments/assets/2cdf951f-d1f3-47c8-80f6-d8b1a6ce0156)

**Limitations of the Algorithm**
Images with soft or blurry edges may not produce clear contours, leading to less defined cartoon effects. The algorithm relies on strong edges for effective segmentation.
