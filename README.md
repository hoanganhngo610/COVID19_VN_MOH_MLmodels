# Prediction of COVID-19 outbreak in Vietnam using Machine Learning and mathematical models

## *Courtesy of Vietnam Ministry of Health*

### Introduction

On March 21st, a group of specialist teams in modelling and predicting the outbreak of COVID-19 in Vietnam is founded, under the management of the Vietnam Ministry of Health (MOH). This group consists of specialists working around the world in different fields, including medicine, epidemiology, pharmacy, computer science, mathematics, etc. Its purpose is to provide meaningful models and insight results in assisting officials on applying suitable policies to control the outbreak.

### About this repository

This repository contains all the ML/maths model that have been implemented by the group, which has also been reported to the Ministry of Health for consideration. 

Currently, this repository include models which can predict:

- Total number of cases in Vietnam by day from data on previous days, using univariate models
- Predicting Length of Stay (LOS) in hospital of COVID-19 patients in Vietnam, based on pre-admission characteristics.

The structure of this repository is as follows:

```
+---predict-LOS(length-of-stay)
|   +---assets                              // completed data to be proceessed
|   +---data_processing                     // raw data and raw processing scripts
|   +---GetData 1.1                         // executable program to separate data into training and testing datasets 
|   +---models                              // ML models 
|   +---visualization                       // model visualisation
+---predict-total-VN(univariate)
|   +---assets                              // completed data to be proceessed
|   +---Grey models GM(1,1) and extensions  // implementing Grey models using R
|   +---Traditional ML models               // ML models
|   +---Reports                             // final report in PDF
```

### Team members

The team members include:

- NGO Hoang Anh:
    - Department of Mathematics and Department of Economics, École Polytechnique, Institut Polytechnique de Paris, France
    - Email: hoang-anh.ngo@polytechnique.edu
- HOANG Thai Nam:
    - Department of Mathematics and Computer Science, Beloit College, USA
    - Email: hoangnt@beloit.edu
- NGUYEN Tuan Khoi:
    - Melbourne School of Engineering, The University of Melbourne, Australia
    - Email: tuankhoin@student.unimelb.edu.au

The group's work is under the supervision of Dr. HA Anh Duc (Ministry of Health). Moreover, Dr. NGUYEN Thu Anh (The University of Sydney) serves as the epidemiological supervior and data provider for the group. 

