# Gene Information

This FAST API application allows you to get the gene information from a mysql database. 

<img width="1408" alt="Screenshot 2023-10-02 at 12 31 07" src="https://github.com/sobia20/gene-info/assets/23616603/cb437fe1-a0b7-4947-aaa1-5f32b9638dd8">

![ezgif com-video-to-gif](https://github.com/sobia20/gene-info/assets/23616603/d768f991-05d1-43cf-93f3-ba0b98bb6fb1)


## Table of contents

- [Getting started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Run the application](#run-the-application)

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
Visit http://localhost:8000/docs  to access the api to get gene information using the gene symbol. An example would be 'JAG1'.  

To shutdown the application, 
```
docker-compose down
```
