# CS-340: Client/Server Development

## Project Overview

This repository contains my coursework from CS-340: Client/Server Development at Southern New Hampshire University (SNHU). The main project involved developing a database-driven dashboard for Grazioso Salvare, an organization that identifies and trains rescue dogs for search-and-rescue operations.

Using Python, MongoDB, and Dash, I developed an interactive dashboard that allows users to filter animal shelter records, view the results in a data table, and explore information through charts and a geolocation map. The project also involved creating a reusable CRUD Python module to handle communication between the database and the dashboard.

## Project Files

- **CRUD_Python_Module.py:** Python module used to connect to MongoDB and perform database operations.
- **ProjectTwoDashboard.ipynb:** Jupyter Notebook containing the interactive Grazioso Salvare dashboard.
- **CS-340 Project Two README.docx:** Project documentation explaining the dashboard, its functionality, and the tools used.
- **Grazioso Salvare Logo.png:** Organization logo used in the dashboard.

## Reflection

### 1. How do you write programs that are maintainable, readable, and adaptable?

When writing programs, I try to keep my code organized, readable, and easy to modify without having to rewrite everything. One example from this course was the CRUD Python module I developed in Project One and reused in Project Two. Instead of writing MongoDB connection and database operations directly into the dashboard, I kept that functionality in a separate module.

This approach made the dashboard code easier to manage because I could focus on building the interface, filters, charts, and callbacks without constantly dealing with database connection details. It also made troubleshooting easier since I could identify whether an issue was coming from the database operations or the dashboard itself. In the future, I could reuse this module in other applications that need to retrieve, insert, update, or delete MongoDB records, such as inventory management systems or other data-driven applications.

### 2. How do you approach a problem as a computer scientist?

My approach to solving problems starts with understanding what needs to be accomplished and breaking the requirements into smaller, manageable tasks. For the Grazioso Salvare project, I needed to understand how the organization would use animal shelter data to identify dogs that could potentially qualify for different rescue training programs. From there, I worked on connecting the database, retrieving the correct records, and displaying that information through an interactive dashboard.

This project was different from some of my previous programming assignments because I had to bring several components together rather than focus on a single program or feature. I worked with MongoDB queries, Python database operations, dashboard widgets, and callbacks to make everything function together. I also had to test the dashboard and troubleshoot issues as they came up. For future projects, I would continue breaking down client requirements, planning the database structure, testing queries independently, and making sure each part of the application works before integrating everything.

### 3. What do computer scientists do, and why does it matter?

Computer scientists solve problems by developing software and systems that make information easier to access, organize, and use. Their work goes beyond writing code because they also have to understand what users need and find practical ways to meet those needs.

The Grazioso Salvare dashboard is a good example of how software can help an organization work more efficiently. Instead of manually searching through thousands of animal shelter records, users can filter the information based on rescue training requirements and review the results through tables, charts, and a map. This helps the organization identify potential rescue dogs more efficiently and make decisions using the available data. Working on this project helped me better understand how database development and software engineering can come together to solve real-world problems.

## Technologies Used

- **Python:** Database operations, application logic, and dashboard development.
- **MongoDB:** Storage and retrieval of animal shelter records.
- **PyMongo:** Communication between Python and MongoDB.
- **Dash:** Interactive dashboard development.
- **Plotly:** Data visualization and chart creation.
- **Pandas:** Data processing and manipulation.
- **Jupyter Notebook:** Dashboard development and testing.

## What I Learned

Through this course, I gained more experience working with NoSQL databases, developing reusable Python modules, and connecting backend database operations to a user interface. I also learned how important it is to organize code properly, test individual components, and build applications around the needs of the people using them.

This project gave me a better understanding of how client/server development works in practice and how database-driven applications can turn large amounts of information into something useful.
