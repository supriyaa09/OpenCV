# OpenCV Lab Experiments

## Overview
This repository contains Jupyter notebook labs for learning OpenCV and basic computer vision techniques. Each notebook in the `experiments/` folder demonstrates a focused topic with runnable code and example images.

## Requirements
- Python 3.8+ (3.10 recommended)
- OpenCV (`opencv-python`)
- Jupyter Notebook or JupyterLab
- NumPy
- Matplotlib

Install required packages:
```bash
pip install opencv-python jupyter numpy matplotlib
```

## Quick Start
1. Open a terminal in the repository root.
2. Start Jupyter:
```bash
jupyter notebook
```
3. Open a notebook from the `experiments/` folder and run the cells.

## Experiments (notebooks)
1. [01_Read_and_display.ipynb](experiments/01_Read_and_display.ipynb) - Read and display images with OpenCV
2. [02_Image_Resolution.ipynb](experiments/02_Image_Resolution.ipynb) - Image resolution and properties
3. [03_Grayscale.ipynb](experiments/03_Grayscale.ipynb) - Convert images to grayscale
4. [04_line.ipynb](experiments/04_line.ipynb) - Draw lines on images
5. [05_Rectangle.ipynb](experiments/05_Rectangle.ipynb) - Draw rectangles
6. [06_Circle.ipynb](experiments/06_Circle.ipynb) - Draw circles
7. [07_text.ipynb](experiments/07_text.ipynb) - Add text to images
8. [08_resize.ipynb](experiments/08_resize.ipynb) - Resize images (scaling, interpolation)
9. [09_rotate.ipynb](experiments/09_rotate.ipynb) - Rotate images and affine transforms
10. [10_rgb2hsv.ipynb](experiments/10_rgb2hsv.ipynb) - Convert RGB to HSV
11. [11_rgb2lab.ipynb](experiments/11_rgb2lab.ipynb) - Convert RGB to LAB
12. [12_rgb2yuv.ipynb](experiments/12_rgb2yuv.ipynb) - Convert RGB to YUV
13. [13_Full_Circle.ipynb](experiments/13_Full_Circle.ipynb) - Full circle drawing examples
14. [14_Ellipse.ipynb](experiments/14_Ellipse.ipynb) - Draw ellipses
15. [15_Blur_Image.ipynb](experiments/15_Blur_Image.ipynb) - Blurring and smoothing filters
16. [16_flip_an_image_horizontally.ipynb](experiments/16_flip_an_image_horizontally.ipynb) - Flip images horizontally
17. [17_Blending_2_Images.ipynb](experiments/17_Blending_2_Images.ipynb) - Blend two images using weighting
18. [18_Changing_Contrast_and_Brightness.ipynb](experiments/18_Changing_Contrast_and_Brightness.ipynb) - Contrast and brightness adjustments
19. [19_Adding_Text_To_Image.ipynb](experiments/19_Adding_Text_To_Image.ipynb) - Text overlays and font options
20. [20_Smmothing_Image.ipynb](experiments/20_Smmothing_Image.ipynb) - Smoothing examples (typo preserved from notebook name)
21. [21_Median_Filter.ipynb](experiments/21_Median_Filter.ipynb) - Median filtering for noise reduction
22. [22_Gausian_Filter.ipynb](experiments/22_Gausian_Filter.ipynb) - Gaussian blur and parameters
23. [23_Bilateral_Filter.ipynb](experiments/23_Bilateral_Filter.ipynb) - Bilateral filter for edge-preserving smoothing
24. [24_Changing_the_Shape_of_Images.ipynb](experiments/24_Changing_the_Shape_of_Images.ipynb) - Morphological transforms and shape changes
25. [25_Effecting_Image_Thresholding.ipynb](experiments/25_Effecting_Image_Thresholding.ipynb) - Thresholding techniques

## Notes & Tips
- Each notebook is self-contained; run cells sequentially.
- Update image paths at the top of a notebook if you store sample images elsewhere.
- Use small sample images for faster iteration while experimenting.

## Next steps (suggested)
- Add a `requirements.txt` with pinned versions for reproducibility.
- Add small sample images in an `assets/` folder and update notebooks to reference them.

---
**Subject**: Computer Vision / Digital Image Processing
**Course Type**: Lab Experiments