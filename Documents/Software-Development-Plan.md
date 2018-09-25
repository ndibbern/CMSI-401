# 4.0 Software Development Plan

## Outline of Software Development Plan

##### 4.1 Plan Introduction

##### 4.1.1 Plan Deliverables

##### 4.2 Project Resources

##### 4.2.1 Hardware Resources

##### 4.2.2 Software Resources

##### 4.3 Project Organization

##### 4.4 Project Schedule

##### 4.4.1 GANTT Chart

##### 4.4.2 Task/ Resource Table

### 4.1 Plan Introduction

This Software Development Plan provides the detail of the projected development for Deeper Insights, a new deep learning algorithm that aims to better predict natural disasters, such as El Niño and Climate Change phenomena.

The Department of Environmental Science and Civil Engineering at Loyola Marymount University seeks a deep learning algorithm that can be trained on climate change data that has been collected since 1986 in order to predict accurate results. They seek for a better prediction model than the currently statistical models that are being used today. They believe that deep learning is the solution to such issues.

#### 4.1.1 Project Deliverables

##### Alpha Beta        Week 14

Per course requirements, The Deeper Insights Alpha Beta release will occur on Week 14

##### 1.0.                       Week 16

Deeper Insights v 1.0 will be demonstrated to the Department of Environmental Sciences and Civil Engineering as an improvement to the statistical models.

### 4.2 Project Resources

Resources involved in project development are organized into hardware and software resources. Within those categories, involvement in the development process and/or application execution is indicated.



#### 4.2.1 Hardware Resources

| Resource                             | Development | Execution |
| ------------------------------------ | ----------- | --------- |
| Macbook Pro Computer (2011 or newer) | X           | X         |
| 8GB RAM                              | X           | X         |
| Wifi Connection                      | X           | X         |
| GPU                                  | X           | X         |
| Ethernet Connection                  | X           | X         |
| Windows Computer                     |             | X         |

#### 4.2.1 Hardware Resources

| Resource         | Application                                                | Development | Execution |
| ---------------- | ---------------------------------------------------------- | ----------- | --------- |
| Atom             | Text editor                                                | X           |           |
| Python           | Programming language                                       | X           | X         |
| Pytorch          | Deep learning Library for Python                           | X           | X         |
| Pandas           | Data Analysis Library for Python                           | X           |           |
| GitHub           | Version Control                                            | X           |           |
| Google Chrome    | End user web browser                                       | X           | X         |
| Mozilla Firefox | End user web browser                                       | X           | X         |
| macOs            | Development operating system and end user operating system | X           | X         |
| Google Cloud     | Data hosting                                               | X           | X         |

### 4.3 Project Organization

This section will outline Deeper Insights project organization, including team member roles and team responsibility.

##### 4.3.1 Organization Structure

We have organized our project members into three teams: data, algorithm and front-end.

| Name            | Team      | Role                             |
| --------------- | --------- | -------------------------------- |
| Natalia Dibbern | Data      | Data analysis and management     |
| Juan Neri       | Algorithm | Algorithm Development and Design |
| Natalia Dibbern | Algorithm | Algorithm Development and Design |
| Juan Neri       | Front-End | Front-End Designer               |

##### 4.3.2 Data Team

The Data team is responsible for cleaning and managing the data. This includes selecting training set and test set as well as the normalization of the data, managing missing entries and managing parameters to avoid overfitting. Refer to 5.3.3 for detailed functional requirements for the data.

##### 4.3.3 Algorithm Team

The Algorithm team is responsible for designing, writing, training and testing the Convolutional Recurrent Neural Network (CRNN) algorithm. Refer to 5.3.2 for detailed functional requirements for the CRNN algorithm.

##### 4.3.4 Front-End team

The Front-End team is responsible for developing the interfaces between users and the Deeper Insights algorithm predictions. They will design interface mockups, design web pages and test across several platforms. Refer to 5.3.1 for detailed functional requirements for the front end

##### 4.3.4 Roles and Responsibilities

Weekly development meetings are held on Tuesday's from 8:00 AM to 12:00 PM, and Scrum meetings are held biweekly on Thursday mornings from 10:00 AM - 11:00 AM. Meetings with the Department of Environmental Sciences and Civil Engineering are held every 2-3 weeks on Thursday mornings, during the scrum meeting block.

Weekly task for all teams will be documented, tracked, and updated via the Github Issues system (stories and epics). This allows for all team members to be informed about the project progress and encourage collaborative development.

### 4.4 Project Schedule

This section will detail the Deeper Insights project schedule including the people and resources necessary for each step.



#### 4.4.1 GANTT Chart

The following GANTT Chart visualizes the duration of the subtasks for Deeper Insights in relationship with each other.



ADD



#### 4.4.2 Task/Resources

| Task                              | People                     | Hardware | Software                                 |
| --------------------------------- | -------------------------- | -------- | ---------------------------------------- |
| Obtaining the data                | Natalia Dibbern            | Macbook  | -                                        |
| Data cleaning                     | Natalia Dibbern            | Macbook  | Python, Pandas, Jupyter Notebook, MATLAB |
| Data normalization                | Natalia Dibbern            | Macbook  | Python, Pandas, Jupyter Notebook, MATLAB |
| Feature reduction (if needed)     | Natalia Dibbern            | Macbook  | Python, Pandas, Jupyter Notebook, MATLAB |
| RNN on small dataset              | Juan Neri, Natalia Dibbern | Macbook  | Pytorch, Pytorch vision, pip, python3    |
| CNN on small dataset              | Juan Neri, Natalia Dibbern | Macbook  | Pytorch, Pytorch vision, pip, python3    |
| RCNN on small dataset             | Juan Neri, Natalia Dibbern | Macbook  | Pytorch, Pytorch vision, pip, python3    |
| RCNN on complete training dataset | Juan Neri, Natalia Dibbern | Macbook  | Pytorch, Pytorch vision, pip, python3    |
| About, predictions UI pages       | Juan Neri                  | Macbook  | Bootstrap 4, Jinja 2                     |
| User Manual Documentation         | Juan Neri, Natalia Dibbern | Macbook  | LaTex                                    |


