<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grid Transformation with Interactive Sliders</title>
</head>
<body>
    <h1>Grid Transformation with Interactive Sliders</h1>
    <p>
        This project demonstrates a dynamic grid transformation using sliders to adjust parameters in real-time. It uses Python libraries like Matplotlib and NumPy to visualize and interact with a 2D transformation grid.
    </p>

  <h2>Features</h2>
    <ul>
        <li><b>Interactive Slider:</b> Modify transformation parameters dynamically to observe real-time changes.</li>
        <li><b>Grid Visualization:</b> A 2D grid of points is displayed, highlighting transformations with original and transformed points.</li>
        <li><b>Customizable Parameters:</b> The transformation is governed by user-defined mathematical functions.</li>
        <li><b>Arrows and Lines:</b> Visualize transformation vectors and important references in the grid.</li>
    </ul>

  <h2>Installation</h2>
    <ol>
        <li>Clone this repository:
            <pre><code>git clone https://github.com/yourusername/grid-transformation.git
cd grid-transformation
            </code></pre>
        </li>
        <li>Install the required libraries:
            <pre><code>pip install numpy matplotlib</code></pre>
        </li>
    </ol>

   <h2>Usage</h2>
    <ol>
        <li>Run the script:
            <pre><code>python grid_transformation.py</code></pre>
        </li>
        <li>Use the slider at the bottom to change the transformation frame and watch the grid dynamically update.</li>
    </ol>

  <h2>Explanation of Key Components</h2>
    <ul>
        <li><b>Transform Function:</b> Computes new positions of grid points based on the transformation matrix, which updates dynamically with the slider value.</li>
        <li><b>Interactive Plotting:</b> The <code>matplotlib.widgets.Slider</code> component enables interactive control.</li>
        <li><b>Visual Elements:</b>
            <ul>
                <li><b>Blue Points:</b> Original grid positions.</li>
                <li><b>Red Points:</b> Transformed grid positions.</li>
                <li><b>Arrows:</b> Represent transformation vectors.</li>
            </ul>
        </li>
    </ul>

  <h2>Visualization Example</h2>
   Here is an example as an png but the full potential of this code can be unleashed only by using the matplotlib slider !
   
![delete](https://github.com/user-attachments/assets/36f77c10-5eff-4bf7-93eb-ca2c251bbe82)

   <h2>Acknowledgemnt</h2>
    <p>
The concept of visualizing matrix transformations and their effects on points first came to me from Grant Sanderson's (3Blue1Brown) legendary Linear Algebra video series. The Lorentz Transformation was demonstrated by Henry Reich of MinutePhysics with his sophisticated mechanical grid system, which he used in his Special Relativity Basics series. This code is simply the Python edition of his mechanical grid (obviously excluding some features like length contraction, which I am willing to add in the future)..
    </p>
</body>
</html>
