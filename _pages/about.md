---
permalink: /about/
title: "About"
author_profile: true
layout: single
last_modified_at: 2019-09-13
toc: true
toc_label: "Outline"
---

Just got the master degree in civil engineering from National Taiwan University in July, 2019. Professional with image processing, image-based hydrologic remote monitoring. A machine learning enthusiastic and experienced in programming with Python using Tensorflow and Keras. Landscape Photographer.  

## Quick Facts
- **Programming Languages**: Python, MATLAB, SQL.  

### Machine Learning
- **Frameworks**: Tensorflow, Keras.  
- **NN**: Logistic Regression, CNN, RNN, Deep Auto-encoder, Genetic Algorithm.
- **Model**: R-CNN based object detection models, YOLO v1~v3.
- **Image Processing**: OpenCV, MATLAB.  
- **Version Control**: Git.  

### Data Science
- **Library**: pandas, matplotlib.  
- **Statistic**: ANOVA, Regression, Uncertainty analysis, Reliability analysis, Time series, Kriging method.  

### Civil Engineering  
- **Knowledge**: Fluid Mechanics, Open Channel Flow.
- **Numerical Model**: HEC-HMS, HEC-RAS, SWMM.
- **GIS**: Arc-GIS, QGIS, UAV, Agi PhotoScan 3D Terrain Reconstruction.
- **Construction Management**: MS Project. 
- **Technical Drawing**: AutoCAD.

### Personally
- Photography.
- Adobe Photoshop, Lightroom. 


## Projects
### Mask R-CNN for Cookies Detection and Segmentation
[Github repo](https://github.com/yuweichiu/Cookies-Detections-Mask-R-CNN)  
This is a tiny project to use Mask R-CNN for detecting two brands of cookies "Lays" and "Doritos". Most of the code is based on the implementation of Mask R-CNN by matterport on Python 3, Keras, and TensorFlow. Where we modified is change the backbone network from ResNet-101 to ResNet-50 and the batch size from 2 to 1 image. This setting is will use 97~98% memory of NVIDIA RTX2060 6GB.  

### pyPIV - A Particle Image Velocimetry GUI toolkit
[Github repo](https://github.com/yuweichiu/pyPIV)  
This is the project dealing with Particle Image Velocimetry based on two algorithm:
1. Direct Cross Correlation (DCC)
2. Convolutional Neural Network (CNN)  

The GUI files built with **PyQt** helps user to modify the parameters in the algorithm more easily.

**Note**: CNN method is not open to public. See the section [Master's Thesis](#masters-thesis) below.


## Master's Thesis
**< The Application of Convolutional Neural Network on Large-Scale Particle Image Velocimetry >**  
The research made an effort on improving the river measurments results on the field by conventional LSPIV technique. We implement a tiny self-build CNN model to replace the direct cross-correlation algorithm (DCC) in the conventional one. We found out that CNN-based LSPIV can keep the decrease of performance below 1% which is 18% and much more unsteady by DCC-based under the noise of illumination. The method we proposed is robust and can give an excellent velocity field with stability and accuracy then DCC gives.  

------
歡迎來到我基於Github pages建置的部落格，而樣式則採用Michael Rose所發表的Jekyll主題"[Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/)"。   
Welcome to my blog built on Github pages. The theme is [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) designed, developed, and maintained by Michael Rose.  

------
本部落格主要語言為中文、英文。  
Primary languages here: Chinese, English.