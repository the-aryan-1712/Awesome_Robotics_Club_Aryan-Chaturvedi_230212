import cv2
import numpy as np

def find_black_blocks(image, intensity):
    black_indices = []
    for i in range(image.shape[0]):
        avg = np.mean(image[i], axis=0)
        if np.average(avg) < intensity:
            black_indices.append(i)
            image[i] = [0, 0, 0]
    return black_indices

def find_black_columns(image, intensity):
    black_indices = []
    for i in range(image.shape[1]):
        avg = np.mean(image[:, i], axis=0)
        if np.average(avg) < intensity:
            black_indices.append(i)
            image[:, i] = [0, 0, 0]
    return black_indices

def process_grid_blocks(image, black_rows, black_cols, intensity):
    rows = len(black_rows) - 1
    cols = len(black_cols) - 1
    grid = []
    for i in range(rows):
        row_arr = []
        for j in range(cols):
            block = image[black_rows[i]+1:black_rows[i+1], black_cols[j]+1:black_cols[j+1]]
            avg_color = np.mean(block, axis=(0, 1))
            if avg_color[0] > intensity:
                row_arr.append(1)
                block[:, :] = [255, 0, 0]
            else:
                row_arr.append(0)
                block[:, :] = [0, 255, 255]
        grid.append(row_arr)
    return grid


# Read the image
image = cv2.imread("Screenshot 2024-04-08 205039.png")
# Find black rows and columns

black_row_indices = find_black_blocks(image, 94)
black_col_indices = find_black_columns(image, 94)


# Process grid blocks
grid = process_grid_blocks(image, black_row_indices, black_col_indices, 165)


cv2.imwrite("answer_python.png", image)