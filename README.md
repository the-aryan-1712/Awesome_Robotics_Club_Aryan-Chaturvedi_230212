<h1>AUTONOMOUS NAVIGATION OF MARS ROVER</h1>

<h3>Description for task 7 :</h3>
<p>This  <a href="https://github.com/the-aryan-1712/Awesome_Robotics_Club_Aryan-Chaturvedi_230212/blob/main/task7/partA.py">taskA</a> aims to remove noise from a given image grid and then  <a href="https://github.com/the-aryan-1712/Awesome_Robotics_Club_Aryan-Chaturvedi_230212/blob/main/task7/partB.py">taskB</a> find the shortest path within the grid. Given code in task 7 folder provides functionality to preprocess an image grid, removing noise and enhancing clarity, followed by algorithms to find the shortest path between two points within the grid and finaally drawing path on the image using open cv functionality.</p>
<h2>Usage</h2>
<h3>Part A : Image Grid Noise Removal</h3>
<p>

Input for image<br><br>
image = cv2.imread("Screenshot 2024-04-08 205039.png")<br><br>

Remove noise result<br><br>
cv2.imwrite("answer_python.png", image)</p>
<h3>Part B : Shortest Path Finding and Drawing </h3>
<p><br>
Input for image<br><br>
image = cv2.imread("answer_python.png")<br><br>
Save the result<br><br>
cv2.imwrite("finalanswer_python.png", image)
</p>

<h2>Functioning</h2>
<p> Firstly load image and then iterate over each row and column, separately, on pixels and find its average. If average color is black of near to it we make that particular row or column black.
Thus we manage to find coordinates of contour lines. Now it will iterate on each contour to find centre of block and find average color of block and fill whole block with that color. thus we get reduced noise grid image.</p><br><br>
<p>For finding shortest path it will again iterate on all centre point of blocks and assign value 1 to blue and 0 to yellow and make a 2d nparray. then using Breadth-First Search (BFS) algorithm it found cooordinate of shortest path,if possible. then it uses line drawing tool of open CV and draw line between the coordinate found in BFS algorithm. At last printing some dot and arrow ;).</p>
