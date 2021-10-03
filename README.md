# Data Science Project Overview 
* Developed an application tool that use deep learning to predict the weld quality of resistance spot welding. 
* The data that has been used for this project based on [this research paper.](https://www.sciencedirect.com/science/article/pii/S0261306908001301)
* This application tool consist of 6 tab which each tab have their own puposes.
* This project used only open-source software and packages.
* This application tool can only be used on windows platform.
* Some of the ANN model hyperparameter can be tuned, and some of it have been set to default.

## Code and Resources Used 
**Python Version:** 3.7  
**Packages:** pandas, numpy, sklearn, matplotlib, pyqt5, tensorflow
**GUI development tool:** Qt Designer

## Data collection
The RSW dataset used in this study selected from [this research paper](https://www.sciencedirect.com/science/article/pii/S0261306908001301). There are 36 data consists of three inputs with their corresponding output (label). The three input parameters are weld time (cycle), and weld current (kA), electrode force (N). The class value based on input parameters is either Bad, Good, or Worst, with a TSLBC for each data point.
