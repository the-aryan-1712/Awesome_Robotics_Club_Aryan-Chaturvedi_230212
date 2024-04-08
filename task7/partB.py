import cv2
import numpy as np
from collections import deque

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

# Input for image
image = cv2.imread("answer_python.png")

black_row_indices = find_black_rows(image, 105)
black_col_indices = find_black_columns(image, 94)

r=[]
for i in range(len(black_row_indices)-1):
    if(black_row_indices[i+1]-black_row_indices[i]>10):
        r.append(black_row_indices[i])
r.append(black_row_indices[-1])

c=[]
for i in range(len(black_col_indices)-1):
    if(black_col_indices[i+1]-black_col_indices[i]>10):
        c.append(black_col_indices[i])
c.append(black_col_indices[-1])

r_centre=[]
c_centre=[]

for i in range(len(r)-1):
    mid=(r[i+1]+r[i])/2
    r_centre.append(mid)
for i in range(len(c)-1):
    mid=(c[i+1]+c[i])/2
    c_centre.append(mid)


arr=np.zeros([len(r_centre),len(c_centre)])
for i in range(len(r_centre)):
    for j in range(len(c_centre)):
        if((image[int(r_centre[i])][int(c_centre[j])])[0]>200):
            arr[i,j]=1

print(arr)

def shortest_path(matrix):
  
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
  
    rows, cols = matrix.shape
    
   
    visited = np.full((rows, cols), False)
    queue = deque([(0, 0)])  
    visited[0][0] = True
    
    parent = [[(-1, -1)] * cols for _ in range(rows)]
 
    while queue:
        x, y = queue.popleft()
        
        
        if (x, y) == (rows - 1, cols - 1):
            break
      
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and matrix[nx][ny] == 0:
                visited[nx][ny] = True
                parent[nx][ny] = (x, y)
                queue.append((nx, ny))
   
    path = []
    x, y = rows - 1, cols - 1 
    while (x, y) != (0, 0):  
        path.append((x+1, y+1))
        x, y = parent[x][y] 
    
    path.append((1, 1))  
    path.reverse()  
    
    return path


path = shortest_path(arr)
print("Shortest path:", path)


def draw_lines(image, lines, color=(0, 0, 255), thickness=2):
    
    for line in lines:
        start, end = line
        cv2.line(image, start, end, color, thickness)
    return image


lines=[]
for i in range(len(path)-1):
    a=int(r_centre[path[i][1]-1]  )
    b=int(c_centre[path[i][0]-1])
    c=int(r_centre[path[i+1][1]-1])
    d=int(c_centre[path[i+1][0]-1])
    lines.append(((a,b),(c,d)))



a=int(r_centre[path[0][1]-1] )
b=int(c_centre[path[0][0]-1])
point=(a,b)


result_image = draw_lines(image, lines)

cv2.arrowedLine(image,point, point, (0, 0, 255), thickness=20)
a=int(r_centre[path[-1][1]-1]  )
b=int(c_centre[path[-1][0]-1])
start=(a-10,b-23)
end=(a,b)
color=(0,0,255)
thickness=6
cv2.line(image, start, end, color, thickness)
start=(a+10,a-10)
cv2.line(image, start, end, color, thickness)



# Save the result
cv2.imwrite("finalanswer_python.png", image)












