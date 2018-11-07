# 6.0 Software Design Description

#### Outline of Software Development Plan

6.1 Introduction

6.1.1 System Objectives

6.1.2 Hardware, Software and Human Interfaces

6.2 Architectural Design

6.2.1 Major Software Components

6.2.2 Major Software Interactions

6.2.3 Architectural Design Diagrams

6.3 CSC and CSU Descriptions



## 6.1 Introduction

This document presents the architecture and detailed design for the software for Deeper Insights. The department of Civil Engineering and Environmental Sciences at LMU seeks an deep learning solution for the better prediction of El Niño and climate change. Climate change predictions are currently being made by statiscial models which are not accurate. Scientists need a more efficient system to make such predictions. Through Deeper Insights three main functions: Harness the powrt of big data, defeat the accuracy of current statiscial and dynamical models and producing an algorithm that is fast and simple, users are enabled to effectively use this algorithm and create better predictions.

### 6.1.1 System Objectives

### 6.1.2 Hardware, Software and Human Interfaces



## 6.2 Architectural Design

The Deeper insights system architecture is comprised of a web-browser-based user interface (front-end), a RNN algorithm (backend). The front end consists of a single webpage which allows users to see the predictions being made by the algorithm. The backend will be designed to allow fast predictions as new data is available.



### 6.2.1 Major Software Components

* **Front End CSC** 
  * About Page
  * Header
  * Climate Display
  * Navigation bar
    * Button linkind to the about page
    * El Niño predictions
    * Chimate Change
* **RNN algorithm CSC**
  * torch libraries
  * 20 hidden layers of dimension 100 neuron
  * 10 convolutional layers
  * Model Class
  * Loss Class
  * Cross Entropy loss