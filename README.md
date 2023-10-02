# Gene Information API
<img src="https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white"> <img src="https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white"> <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white"> <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">

This FAST API application allows you to get the gene information from a mysql database. 

<img width="1408" alt="Screenshot 2023-10-02 at 12 31 07" src="https://github.com/sobia20/gene-info/assets/23616603/cb437fe1-a0b7-4947-aaa1-5f32b9638dd8">

## Table of contents

- [Getting started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Run the application](#run-the-application)
- [Alternative API docs](#alternative-api-docs)

### Getting started

#### Prerequisites

Before starting the application, make sure the docker daemon is running. 
To clone, 
```
git clone https://github.com/sobia20/gene-info.git
cd gene-info
```
#### Run the application
To start the application, 
```
docker-compose up -d
```
Visit http://localhost:8000/docs to access the interactive API documentation. 

You can get a list of genes matching the specified gene symbol, gene symbol, gene stable ID and a list of stable IDs of all the transcripts associated with the gene using the gene symbol for the `/gene` get api. 

An example of gene symbol would be 'JAG1'.  

<p align="center">
<img src="https://github.com/sobia20/gene-info/assets/23616603/d768f991-05d1-43cf-93f3-ba0b98bb6fb1">
</p>

To shutdown the application, 
```
docker-compose down
```
### Alternative API docs
Visit http://localhost:8000/redoc for alternative documentation.
