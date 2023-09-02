# API Intelieye 

<p align="center">
  <img src="https://i.postimg.cc/ht8PCZys/logo-intelieye.png" alt="Diger Logos" width="30%">
</p>

Intelieye is a Discover the truth about eye health with our website dedicated to checking facts or myths surrounding various aspects of ocular well-being. Welcome to our fact-checking hub for everything related to your precious vision. 

This repository serves as the home for the development of the Intelieye API, constructed with Python Programming Language.

To see our API application please visit the following link [API Intelieye](https://api.intelieye.my.id/)

To see our Application Website Repository visit the following link [Repo Web App Intelieye](https://github.com/arifsptra/intelieye-web)

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

Make sure you have the following software installed on your machine:
- Python (minimal version 3.0)

## Installation

```
# Clone the repository to your local machine:
$ git clone https://github.com/arifsptra/intelieye-api.git

# Change to the project directory
$ cd intelieye-api

# Create a virtual environment in Python
$ python3 -m venv venv

# Activated your virtual environment
$ source venv/bin/activate

# Install the project dependencies
$ pip install Flask
$ pip install Flask-SQLAlchemy
$ pip install Flask-Cors
$ pip install python-dotenv
$ pip install numpy
$ pip install gensim
$ pip install keras
$ pip install requests
$ pip install scikit-learn
$ pip install mysqlclient
$ pip install tensorflow

# Run the Flask app with the following command:
$ python3 app.py

# Visit http://127.0.0.1:5000/ in your web browser to see the application.
```

## Technology Stack

- Python (Programming Language)
- Flask (Python Framework)

## Contributors

- [Arif Saputra](https://github.com/arifsptra)
- [Muhammad Hafizh Dzaky](https://github.com/haf-izh)
- [Vander Mulya Putra](https://github.com/vandermulya)

## API Endpoints

URL : [https://api.intelieye.my.id](https://api.intelieye.my.id)

### Get All Sentences

- **URL**: `/sentences`
- **Method**: GET
- **Description**: Get all sentences.
- **Response**: `200`
  ```json
  {
    "reads":[
      {
        "0": [
          "Cannot Read 1",
          "Cannot Read 2"
        ]
      },
      {
        "1": [
          "Readed 1",
          "Readed 2"
        ]
      }
    ],
    "contents":[
      {
        "0": [
          "Not about the eyes 1",
          "Not about the eyes 2"
        ]
      },
      {
        "1": [
          "About the eyes 1",
          "About the eyes 2"
        ]
      }
    ],
    "categories":[
      {
        "0": [
          "Content mitos 1",
          "Content mitos 2"
        ]
      },
      {
        "1": [
          "Content fakta 1",
          "Content fakta 2"
        ]
      }
    ],
  }
  ```

### Create Sentence

- **URL**: `/sentences`
- **Method**: POST
- **Description**: Create a new sentence.
- **Request Body**:
  ```json
  {
    "sentence": "Melihat matahari dapat merusak mata",
    "read": 1,
    "content": 1,
    "category": 1
  }
  ```
- **Response**: `200`
  ```json
  {
    "sentence": "Sentence created successfully"
  }
  ```

### Delete All Sentences
- **URL**: `/sentences`
- **Method**: DELETE
- **Description**: Delete all sentences.
- **Response**: `200`
  ```json
  {
    "sentence": "All Sentence deleted successfully"
  }
  ```

### Get Sentence by Id
- **URL**: `/sentences/100`
- **Method**: GET
- **Description**: Get a sentence by its ID.
- **Response**: `200`
  ```json
  {
    "sentence": "Makan nasi dapat menyehatkan mata", 
    "read": "1", 
    "content": "1", 
    "category": "0"
  }
  ```

### Update Sentence by Id
- **URL**: `/sentences/3`
- **Method**: PUT
- **Description**: Update a sentence by its ID.
- **Request Body**:
  ```json
  {
    "sentence": "coba 10",
    "read": 1,
    "content": 1,
    "category": 0
  }
  ```
- **Response**: `200`
  ```json
  {
    "sentence": "Sentence updated successfully"
  }
  ```

### Delete Sentence by Id
- **URL**: `/sentences/1`
- **Method**: DELETE
- **Description**: Delete a sentence by its ID.
- **Response**: `200`
  ```json
  {
    "sentence": "Sentence deleted successfully"
  }
  ```

### Predict Sentence
- **URL**: `/predicts`
- **Method**: POST
- **Description**: Predict a sentence.
- **Request Body:
  ```json
  {
    "sentence": "Diabetes menyebabkan retinopati diabetik yang mengganggu penglihatan"
  }
  ```
- **Response**: `200`
  ```json
  {
    "result": "Fakta"
  }
  ```

### Get All Predict Results
- **URL**: `/predicts`
- **Method**: GET
- **Description**: Get all predict results.
- **Response**: `200`
  ```json
  {
    "data":[
      {
        "sentence": "Diabetes menyebabkan retinopati diabetik yang mengganggu penglihatan", 
        "result": "Fakta"
      },
      {
        "sentence": "Melihat bulan dapat menyehatkan mata", 
        "result": "Mitos"
      },
    ]
  }
  ```

### Train Model
- **URL**: `/train`
- **Method**: POST
- **Description**: Train the model.
- **Response**: `200`
  ```json
  {
    "result": "Read 1 Content 2"
  }
  ```

### Get Trained Sentences
- **URL**: `/trained`
- **Method**: GET
- **Description**: Get trained sentences.
- **Response**: `200`
  ```json
  [
    {
      "Mitos": [
        "Mitos sentence 1",
        "Mitos sentence 2"
      ]
    },
    {
      "Fakta": [
        "Fakta sentence 1",
        "Fakta sentence 2"
      ]
    }
  ]
  ```

## Licence

This project is licensed under the MIT license. Please see the LICENSE file for more information.
