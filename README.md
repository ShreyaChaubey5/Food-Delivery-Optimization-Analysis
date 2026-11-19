**Food Delivery Operations & Delivery Time Optimization Analysis**

Project Overview

Food delivery platforms operate in dynamic environments where traffic congestion, weather conditions, vehicle characteristics, and delivery partner operations can influence delivery performance.

This project analyzes food delivery operational data to identify factors associated with longer delivery times, investigate delivery delays, and recommend data-driven operational improvements.

The primary objective is to help operations teams understand where, when, and under what conditions delivery delays are concentrated, so they can prioritize potential interventions.

This is an exploratory and decision-support analytics project focused on solving operational business problems rather than building another conventional dashboard.

Business Problems

The analysis focuses on three business problems:

1. Traffic and Weather-Related Delivery Delays

Business question: How do traffic and weather conditions relate to delivery-time performance, and where should operational improvements be prioritized?

Key findings:

Orders under Jam traffic had an average delivery time of approximately 31.18 minutes.

The delay rate under Jam traffic was 50.63%, compared with 7.87% under Low traffic.

Foggy and Cloudy conditions had delay rates of approximately 43.8%.

Metropolitan orders under Jam traffic accounted for 5,969 delayed orders.

The 19:00–21:00 period in Metropolitan areas under Jam traffic contained 5,655 delayed orders.

Business recommendation:

Evaluate congestion-aware dispatch and route planning.

Improve delivery-time estimates during heavy traffic.

Investigate weather-aware delivery planning.

Prioritize evening operations in Metropolitan areas.

Illustrative impact scenario:

Reducing the delay rate from 53.77% to 48% for 10,517 Metropolitan evening orders under Jam traffic could potentially reduce delayed orders by approximately 607, assuming unchanged order volume.

This is a hypothetical scenario, not a measured or guaranteed intervention outcome.

2. Vehicle and Delivery Partner Performance

Business question: Are vehicle characteristics and delivery partner performance associated with differences in delivery times?

Key findings:

Motorcycle deliveries represented the largest order volume: 26,429 orders.

Motorcycles had an observed delay rate of 33.94%.

Electric scooters and scooters had lower observed delay rates of 23.44% and 24.33%, respectively.

Vehicle condition code 0 had a delay rate of 41.69%, compared with approximately 23.9% for condition codes 1 and 2.

An analysis of 720 delivery partners with at least 20 orders showed a moderate negative correlation (-0.354) between partner-level average ratings and average delivery time.

Business recommendation:

Investigate vehicle condition codes and maintenance records.

Examine motorcycle delivery assignments and operating conditions.

Review delivery partner workload distribution.

Identify consistently high-delay patterns for further operational investigation.

Vehicle condition codes have not yet been mapped to their actual meanings, so no assumptions about good or poor condition are made.

3. Delivery Partner Age-Group Performance Differences

Business question: Do delivery-time differences across age groups persist across traffic conditions, city categories, and vehicle types?

Key findings:

The 30–40 age group had an observed delay rate of 41.72%.

The 20–30 age group had a delay rate of 21.04%.

The higher delay rate for the 30–40 group persisted across major traffic categories.

The same pattern appeared across Metropolitan and Urban city categories.

The 30–40 group also showed higher delay rates across motorcycle, scooter, and electric scooter categories.

Business recommendation:

Investigate workload allocation and delivery assignment patterns.

Examine differences in route difficulty and order complexity.

Validate age data and repeat the analysis using originally observed ages.

Avoid age-based performance decisions without further investigation.

These findings are observational and do not establish that age causes delivery delays.

Dataset Information

Dataset: Zomato Food Delivery Dataset

Records: Approximately 45,584 orders

Features: 20 original columns, with additional analytical features created during preprocessing.

Analytical delay benchmark: Delivery time greater than 30 minutes.

The 30-minute threshold is an analytical benchmark used in this project, not a verified company service-level agreement.

Tools & Technologies

Python — Data analysis and business problem investigation

Pandas — Data cleaning, transformation, grouping, and aggregation

NumPy — Numerical operations

Analytical Approach

Data Understanding: Examined dataset structure, features, missing values, and data types.

Data Cleaning: Removed duplicate records, handled missing values, standardized time fields, and investigated anomalous values.

Exploratory Analysis: Evaluated delivery-time distributions and delay patterns.

Operational Segmentation: Compared delivery performance across traffic, weather, city, vehicle, and delivery partner segments.

Business Impact Estimation: Developed hypothetical improvement scenarios using observed order volumes and delay rates.

Decision Support: Identified operational priorities and proposed interventions with measurable outcomes.

Project Limitations

The dataset is observational; correlations and group differences do not establish causation.

The 30-minute delay threshold is an analytical choice, not an official SLA.

Missing values and imputed observations may influence certain findings.

The meanings of vehicle condition codes require confirmation.

Delivery partner ratings are not customer satisfaction ratings.

The hypothetical improvement scenarios require real-world pilot validation.

Some age-group comparisons may be affected by median-imputed age values.

Expected Business Value

This analysis aims to support food delivery operations teams in:

Identifying high-delay operational segments.

Improving traffic-aware dispatch decisions.

Investigating fleet and vehicle performance.

Reviewing delivery partner allocation.

Developing measurable delivery-time improvement initiatives.
