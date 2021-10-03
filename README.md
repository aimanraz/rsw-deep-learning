# Application Tools For Predicting Resistance Spot Welding Weld Quality Project Overview 
* Developed an application tool that use deep learning to predict the weld quality of resistance spot welding. 
* The data that has been used for this project based on [this research paper.](https://www.sciencedirect.com/science/article/pii/S0261306908001301)
* This application tool consist of 6 tab which each tab have their own puposes.
* This project used only open-source software and packages.
* This application tool can only be used on windows platform.
* Some of the ANN model hyperparameter can be tuned, and some of it have been set to default.

## Code and Resources Used 
**Python Version:** 3.7

**Packages:** pandas, numpy, sklearn, matplotlib, pyqt5, tensorflow, [Tensorflow Levenberg-Marquardt](https://github.com/fabiodimarco/tf-levenberg-marquardt), pyinstaller

**GUI development tool:** Qt Designer

## Introductary tab (Tab 1)
The first tab introduces the front page of the application tools as shown below:


## Data collection
The RSW dataset used in this study selected from [this research paper](https://www.sciencedirect.com/science/article/pii/S0261306908001301). There are 36 data consists of three inputs with their corresponding output (label). The three input parameters are weld time (cycle), and weld current (kA), electrode force (N). The class value based on input parameters is either Bad, Good, or Worst, with a TSLBC for each data point. Below shows the example of the extracted data.

## Data Preprocessing (Tab 2)
Data pre-processing transforms raw data into an understandable and readable format. According to the dataset, the features scaling method needs to be used since it has many different values between each feature. Feature scaling will normalize the independent variable of data. Since the machine learning model is based on a mathematical equation, categorical data such as BAD, GOOD, and WORST will be encoded into numbers. The TSLBC values must also be normalized to the regular scale without distorting the value ranges' variations.

The second tab where user is required to import the input file and pre-process dataset in the input file for further process. In pre-processing, the user can select which type of true value to be pre-processed before setup the ANN model.

## Machine learning modeler (Tab 3)
The third tab set up the model structures and other essential parameters to implement the ANN model. In this tab, user is required to set up all of the hyperparameter of deep learning model. To add the number of hidden layer, user can simply check (to add layer) or uncheck (to remove layer) the check boxes. 
The list of hyperparameter available in this tool:
* Number of neuron
* Number of hidden layer used
* Type of activation function
* Type of loss function
* Metrics
* Optimizer
* Epoch
* Learning rate
* Batch size

## Train and evaluate the model (Tab 4)
The fourth tab is used to train and evaluate model performance. The train size of the dataset can be set up on this tab and, the default value is set 80%. This tab shows the value of training and testing accuracy once ANN model completes the training process. The confusion matrix, loss and accuracy graph can be plotted in this tab. 

## Weights and biases (Tab 5)
The fifth tab used to display the current value of the weight and bias of the model. The weight and bias values for each layer of ANN model are shown and can be used for research purposes.

## Prediction (Tab 6)
The last tab is used to predict the weld quality and TSLBC of RSW with the corresponding input from the user. The user is required to insert the input parameters before the process of prediction that based on the developed training algorithm in previous tab.

