# Lane Detection using OpenCV
# Developed By: Subashini K
# Register No: 212225240160

# Step 1: Import Libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 2: Read the Image
img = cv2.imread(r"road.jpeg")
if img is None:
    img = cv2.imread(r"C:\Users\acer\Desktop\road.jpeg")

if img is None:
    print("Image not found. Check path.")
else:
    print("Image loaded successfully.")

# Step 3: Convert to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 4: Display Images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")
plt.show()

# Step 5: Thresholding
_, threshold = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
plt.figure()
plt.imshow(threshold, cmap='gray')
plt.title("Thresholded Image")
plt.axis("off")
plt.show()

# Step 6: Region of Interest (ROI)
mask = np.zeros_like(gray)
height, width = gray.shape
roi = np.array([[(100, height), (width - 100, height), (width // 2, height // 2)]])
cv2.fillPoly(mask, roi, 255)
roi_img = cv2.bitwise_and(threshold, mask)

plt.figure()
plt.imshow(roi_img, cmap='gray')
plt.title("ROI Masked Image")
plt.axis("off")
plt.show()

# Step 7: Edge Detection (Canny)
edges = cv2.Canny(roi_img, 50, 150)
plt.figure()
plt.imshow(edges, cmap='gray')
plt.title("Edge Detected Image")
plt.axis("off")
plt.show()

# Step 8: Gaussian Blur
blurred = cv2.GaussianBlur(edges, (5, 5), 0)
plt.figure()
plt.imshow(blurred, cmap='gray')
plt.title("Smoothed Image")
plt.axis("off")
plt.show()

# Step 9: Hough Transform
lines = cv2.HoughLinesP(blurred, 1, np.pi / 180, threshold=50, minLineLength=100, maxLineGap=50)
line_img = np.copy(img)

if lines is not None:
    for line in lines:
        if len(line) == 4:
            x1, y1, x2, y2 = line
        else:
            x1, y1, x2, y2 = line[0]
        cv2.line(line_img, (x1, y1), (x2, y2), (0, 255, 0), 3)
else:
    print("No lines detected. Try adjusting parameters.")

plt.figure()
plt.imshow(cv2.cvtColor(line_img, cv2.COLOR_BGR2RGB))
plt.title("Detected Lines")
plt.axis("off")
plt.show()

# Step 10: Lane Detection Logic
final_output = cv2.addWeighted(img, 0.8, line_img, 1, 0)
plt.figure()
plt.imshow(cv2.cvtColor(final_output, cv2.COLOR_BGR2RGB))
plt.title("Final Lane Detection Output")
plt.axis("off")
plt.show()
