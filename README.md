# EECE5639
EECE 5639 NEU

Computer Vision - EECE 5639
Professor Octavia Camps

## Table of Contents
| Project                          | Description                            |
|----------------------------------|----------------------------------------|
| [Project1][1]                    | Motion Detection                       |
| [Project2][2]                    | Homographies                           |
| [Project3][3]                    | Stereo                                 |
| [Project4][4]                    | Term Project (Structure from Motion)   |


[1]: https://github.com/vegetablesB/EECE5639/tree/main/Project1
[2]: https://github.com/vegetablesB/EECE5639/tree/main/Project2
[3]: https://github.com/vegetablesB/EECE5639/tree/main/Project3
[4]: https://github.com/vegetablesB/EECE5639/tree/main/Project4

## Abstract
### Project1(Motion Detection)
The purpose of this project is to explore different filters that can be used to detect motion in image sequences captured by a stationary camera. The images mostly contain a stationary background with small moving objects passing in front of the camera. The main goal is to compare the effectiveness of various algorithms and filters in detecting motion by analyzing the differences in intensity between the background and the moving objects **through time**. The findings, including the most effective algorithms and threshold cutoffs, are available in the project’s Github code repository.
### Project2(Homographies)
In this project, we will be exploring a method for creating a mosaic of a sequence of images that have a significant overlap between consecutive frames. The overlap between frames allows for common features to be identified and correlated, giving us information about how the image planes transform between frames. We will be using the Harris Corner Feature detector algorithm to extract **corner features**, normalized cross correlation to **match features** across images, Random Sample Consensus (**RANSAC**) and least squares fitting to **estimate homographies** between images. Additionally, we will investigate **blending** techniques to address color differences between image frames and distortions in the final mosaic.
### Project3
In this project, we investigate methods for stereo vision in a camera setup with unspecified parameters. Under these circumstances, we work with two concurrently captured images that exhibit almost identical features. Nevertheless, slight distortions exist between the images due to variations in camera positions. We commence by applying the SIFT Detector and Normalized Cross Correlation algorithms, previously utilized in Project 2, to this novel context. Subsequently, we expand upon these techniques by employing the identified correspondences to estimate the Fundamental Matrix and incorporating the RANSAC algorithm to exclude outliers. The project culminates in an examination of dense disparity maps from our experiments, which serves as a final goal towards genuine 3D reconstruction.
### Project4
This report presents the implementation and results of the Structure from Motion (SfM) algorithm using the factorization method on the CMU Hotel Sequence dataset. The algorithm involves feature extraction, tracking across frames, and the recovery of the 3D structure. We discuss the challenges faced, optimizations made, and possible improvements to the algorithm.



## Contributors

<a href="https://github.com/vegetablesB">
  <img src="https://avatars.githubusercontent.com/u/44360183?v=4" height = 100/>
</a>

<a href="https://github.com/kairos-cmd">
  <img src="https://avatars.githubusercontent.com/u/114029504?v=4" height = 100/>
</a>
