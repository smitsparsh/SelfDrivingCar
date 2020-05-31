# SelfDrivingCar
----
This repository contains my solution code to the assignments and capstone project of all the modules to complete the [Self-Driving Cars Specialization](https://www.coursera.org/specializations/self-driving-cars?).

Modules are divided into:


*   [Introduction to Self-Driving Cars](https://github.com/smit585/SelfDrivingCar/tree/master/Course%201%20Introduction%20to%20Self%20Driving%20Car)
      *  This module introduces to the overview of the Complete Autonomous Driving Stack
      *  Explains standards and Protocols that should be followed while designing Autonomous Driving Stack
      * Designs Vehicle Kinematic ([Bicycle](https://github.com/smit585/SelfDrivingCar/blob/master/Course%201%20Introduction%20to%20Self%20Driving%20Car/%20Week%204%20Vehicle%20Dynamimc%20Modeling/%20Kinematic%20Bicycle%20Model.ipynb)) and Dynamic Model
      * Design [Vehicle Longitudinal](https://github.com/smit585/SelfDrivingCar/blob/master/Course%201%20Introduction%20to%20Self%20Driving%20Car/%20Week%204%20Vehicle%20Dynamimc%20Modeling/LongitudinalControl.ipynb) and Lateral Control
      
      #### In the [Capstone project](https://github.com/smit585/SelfDrivingCar/tree/master/Course%201%20Introduction%20to%20Self%20Driving%20Car/Week%207%20Putting%20it%20All%20Together), I creeated a Bicycle Model controller with De-Coupled Lateral and Longitdunal Control. This controller is expected to trace the provided waypoints and velocity with the highest accuracy. I implemented a **PID Controller** to manipulate the longitudinal control and **Stanely Controller** to implement lateral control. I completed the course with 98%, with 100% grade in the Final Project 

*   [State Estimation and Localization for Self-Driving Cars](https://github.com/smit585/SelfDrivingCar/tree/master/Course%202%20State%20Estimation%20and%20Localization)
      * Introduces [Least Squares](https://github.com/smit585/SelfDrivingCar/blob/master/Course%202%20State%20Estimation%20and%20Localization/Week%201%20Least%20Squared%20Error/C2M1L1.ipynb) to find a best fit line to a linar model. Augmented Least Squares to a [Recursive approach](https://github.com/smit585/SelfDrivingCar/blob/master/Course%202%20State%20Estimation%20and%20Localization/Week%201%20Least%20Squared%20Error/C2M1L2.ipynb) so the former can be deployed on a data stream and fit being calculated on the fly.
      * Unfolds the [Kalman Filters](https://github.com/smit585/SelfDrivingCar/blob/master/Course%202%20State%20Estimation%20and%20Localization/Week%202%20Karman%20Filters/Extended%20Karman%20Filters%20Solution.ipynb) and how to calculate estimate with a stream of data
      * Introduces Linearization of Non-Linear Models and using Extended Kalman Filters to find the estimate using a predictive model and a measurement model. Enhances Vanilla EKF to estimate error instead of the complete Non linear model and establishes the concept of Error State Extended Kalman Filters (ES-EKF)
      * Conceptualizes Unscented Transform and establishes concept of Unscented Kalman filter that obviates the need of Linearization and thus giving a better estimate
      * Introduces IMU, GNSS, [Lidar](https://github.com/smit585/SelfDrivingCar/blob/master/Course%202%20State%20Estimation%20and%20Localization/Week%202%20Karman%20Filters/Estimation%20with%20Lidar.ipynb) and use them as motion and measurement models to predict the state of Vehicles.

      #### The [Capstone project](https://github.com/smit585/SelfDrivingCar/tree/master/Course%202%20State%20Estimation%20and%20Localization/Week%205%20Putting%20it%20All%20Together) demands a good grip on Jacobian Matrices, Covariance, and Motion model of IMU with Measurement model of GNSS and IMU. It also requires basic understanding of Quaternions. In this project I implemented both the models and used ES-EKF to find the state of vehicle at each time step. Completed the course with 99% grade and a 100% in Capstone Project. 


*   [Visual Perception for Self-Driving Carst](https://)
*   [Motion Planning for Self-Driving Cars](https://)
