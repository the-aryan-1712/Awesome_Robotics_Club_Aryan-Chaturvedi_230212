import cv2
import numpy as np

def find_black_rows(image, intensity):
    black_indices = []
    for i in range(image.shape[0]):
        avg = np.mean(image[i], axis=0)
        if np.average(avg) < intensity:
            black_indices.append(i)
            for j in range(image.shape[1]):
                
                if not np.allclose(image[i][j], [255, 255, 255], atol=10):
                    image[i, j] = [0, 0, 0]           

    return black_indices

def find_black_columns(image, intensity):
    black_indices = []
    for i in range(image.shape[1]):
        avg = np.mean(image[:, i], axis=0)
        if np.average(avg) < intensity:
            black_indices.append(i)
            for j in range(image.shape[0]):
                
                if not np.allclose(image[j][i], [255, 255, 255], atol=10):
                    image[j, i] = [0, 0, 0] 
    
    return black_indices

def process_grid_blocks(image, black_rows, black_cols):
    rows = len(black_rows)-1 
    cols = len(black_cols)-1
    for i in range(rows): 
        for j in range(cols):
            block = image[black_rows[i]+1:black_rows[i+1], black_cols[j]+1:black_cols[j+1]]
            avg_color = np.mean(block, axis=(0, 1))
            block[:, :] = avg_color

# Input for image
image = cv2.imread("sample_input.png")


black_row_indices = find_black_rows(image, 94)
black_col_indices = find_black_columns(image, 94)

process_grid_blocks(image, black_row_indices, black_col_indices)

# Save the result
cv2.imwrite("answer_python.png", image)
