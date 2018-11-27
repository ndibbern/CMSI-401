# 5.0 Requirements Specification

## Outline of Requirements Specifications

##### 5.1 Introduction

##### 5.2 Functional Requirements

##### 5.3 Performance Requirements

##### 5.4 Project Environment Requirements

##### 5.4.1 Development Environment Requirements 

##### 5.4.2 Execution Environment Requirements

## 5.1 Introduction

This Software Requirements Specification (SRS) documents the requirements for the Deeper Insights Deep Learning Algorithm. Deeper Insights is a private deep learning algorithm aimed to be used by the government and non-profit organizations. The algorithm was developed with the aim to predict climate change and El Niño, although flexibility in the algorithm implementation allows for the possible extension of this algorithm to be used to predict other natural disasters such as the trajectory of a hurricane and earthquakes.

The core of the efficiency of the algorithm is the availability of high-quality data, which contains all the information needed for the algorithm to be trained efficiently and to produce accurate predictions. Deeper Insights has 3 main focus points: simplicity to use for people who are not familiar with deep learning algorithms, accurate predictions, and flexibility to allow scalability to larger amounts of data as more is collected over time.

The Deeper Insights algorithm is composed of a Recurrent Neural Network (RNN), a Convolutional Neural Network (CNN) and a user interface to present the results of the algorithm in real time as new data is obtained. The RNN is used to make accurate predictions on data that is obtained over a time period (ours is from 1982 - present), and the CNN is to process data that has many "layers" (like in pictures); such layers in our algorithm would be climate change-related features such as air temperature, sea temperature, pressure, and humidity. Such features are measured on an area, and thus can be represented as a grid, hence each of these will represent a layer to be input in the CNN.

## 5.2 CSCI Component Breakdown

### 5.2.1 Frontend CSC --web-based GUI for Deeper Insights

#### 5.2.1.1 About Page CSU -- page to display information about Deeper Insights to the public

#### 5.2.1.2 Predictions Page CSU -- page to display the climate change predictions made my Deeper Insight Algorithm

#### 5.2.1.3 Header CSU -- top menu to display each of the previously pages

##### 5.2.1.3.1 Home module -- displays the about page

##### 5.2.1.3.2 Predictions module -- displays the predictions

### 5.2.2 Server CSC -- Description

#### 5.2.2.1 Google Cloud CSU - modules for handling the data and algorithm



## 5.3 Functional Requirements by CSC

The Deeper Insights algorithm will allow governments from countries like the United States to better predict climate change and natural disasters in order to take early actions to prevent damage. In the requirements that follow, "user" is understood to be customers of the service (such as these governments). Users will be able to see climate change and el Niño predictions in real time.

### 5.3.1 Frontend

#### 5.3.1.1 The frontend shall display an about page to provide information about Deeper Connections to potential users.

#### **5.3.1.2 Frontend Climate Display**

##### **5.3.1.2.1 The Frontend shall display climate change predictions.**

##### 		 The **Frontend** will display the predictions in a graph.

##### **5.3.1.2.2  The** **Frontend** **shall provide an option to view predictions from at least                          two sources.**

#####                 **Source options will include but not be limited to “El Niño” or “Climate Change”.**

**5.3.1.2.3 The Front end shall display climate change predictions for the next one year period.**

#### 5.3.1.3 The Frontend shall display the Earth Systems Research Laboratory Logo

#### 5.3.1.4 The Frontend shall restrict users without adim access from the admin console page.

#### 5.3.1.5 The Frontend shall have a navigation bar to switch between pages.

##### 		5.2.1.5.1 The navigation bar shall display a button linking to the about page, el Niño prediction and Climate Change prediction tabs

### 5.3.2 Convolutional Recurrent Neural Network (CRNN) Algorithm

##### 5.3.2.1 The CRNN algorithm shall import the correct libraries.  

##### The correct libraries will include but not be limited to:

* ##### torch library

* ##### torch.nn library

* ##### torchvision library

##### 5.3.2.2.1 The CRNN algorithm shall have at least 20 hidden layers, following the equation Nh=Ns/(α∗(Ni+No)) were Ni is number of inputs, No number of outputs Ns it the number of items in sampling training set and α the learning rate.

##### 		5.3.2.2.2 The CRNN algorithm's hidden layers shall each have a dimension of 100 neurons

##### 		5.3.2.2.3 The CRNN algorithm shall contain at least 10 convolutional layers

##### 5.3.2.2.4 The CRNN algorithm shall instantiate a Model Class

##### 5.3.2.2.5 The CRNN algorithm shall instantiate a Loss Class

##### 	5.3.2.2.6 The CRNN algorithm's Loss Class instance shall include the cross-entropy loss

##### 	5.3.2.2.7 The CRNN algorithm's Loss Class instance shall include a SoftMax in it

##### 5.3.2.2.8 The CRNN algorithm shall Instantiate an Optimizer Class

##### 	5.3.2.2.9 The RNN algorithm's Optimizer Class shall include an Stochastic Gradient Descent  (SGD) optimizer

##### 5.3.2.2.10 The CRNN algorithm shall be trained

#### The CRNN algorithm will be trained with at least 4 years worth of data

##### 		5.3.2.6.1 The CRNN algorithm shall be trained with batches of size 200

##### 		5.3.2.6.2 The CRNN algorithm shall be trained in at least 3000 iterations

##### 		5.3.2.6.3 The CRNN algorithm shall have epochs which are determined by the equation: number of epochs = number_iterations / (train_set_length/ batch_size)

#### 5.3.2.7 The CRNN algorithm shall predict with an accuracy of at least 90%.

#### 5.3.2.8 The CRNN algorithm shall include a Loss vs Nb of Iterations graph

#### 5.3.2.9 The CRNN algorithm shall include an Accuracy vs Nb of Iterations graph



### 5.3.3 Data Requirements

#### 5.3.3.1 The data shall include information about climate change and El Niño features.

#### The data will include but is not limited to the following features:

* ##### Sea Surface Temperature (SST)

* ##### Pressure

* ##### Humidity

* ##### Wind

* ##### Air Temperature

#### 5.3.3.2 The data shall be separated into training data and testing data

#### 	The training data will be used to train the algorithnm

#### 	The testing data will be used to test the efficiency of the 	algorithm

#### 5.3.3.3 The data shall be cleaned using Python library Pandas

#### 	Cleaning will involve the process of replacing any missing entries with the mean value of the feature that entry belongs to

#### 	Cleaning will involve the process of normalizing the data according to each feature

#### 	Cleaning will involve the process of removing unneeded features

#### 	Cleaning will involve centering the values around zero	

#### 5.3.3.4 The data shall be stored in Google Cloud

## 5.4 Performance Requirements by CSC

#### 5.4.1 Fast Navigation. Users should be able to access any of the navigation items within 2 seconds of submitting the request.

#### 5.4.2 Modular System Design. The system design should allow for incorporation for use in equivalent scenarios such that it takes the user less than 10 minutes to do so 

#### 5.4.3 Modular System Design. The system design should allow for modification for use in equivalent scenarios such that it takes the user less than 10 minutes to do so 

#### 5.4.4 Network Crash Recovery. The system should be able to deal with network crashes.

#### 5.4.5 Accessibility. The system will meet the minimum requirements for software accessibility.

## 5.5 Project Environment Requirements

### 5.5.1 Development Environment Requirements

| Category        | Requirement                                            |
| --------------- | ------------------------------------------------------ |
| Frontend        | Bootstrap 4, Jinja 2                                   |
| Algorithms      | Pytorch, Pytorch vision, pip, python3                  |
| Data Management | Cloud-hosted, Pandas, Python, MATLAB, Jupyter Notebook |

### 5.5.2 Excecution Environment Requirements

| Category   | Requirement                           |
| ---------- | ------------------------------------- |
| Frontend   | Web Browser                           |
| Algorithms | Pytorch, Pytorch vision, pip, python3 |
