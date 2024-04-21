#Project Title
"Application to Read Custom PDFs and Answer Questions Using a Language Model"
## Give the Open-ai key

Open the config.py file and find the Config class. Replace 'your-key' with your OpenAI API key:
```bash
SECRET_KEY = 'your-key'
```



## Running the Backend Application

Before running the backend application, please make sure you have Python installed on your system. You can download and install Python from the official website: [Python Downloads](https://www.python.org/downloads/)

To run the backend application, follow these steps:

1. Open a new terminal and navigate to the project directory using the `cd` command:

    ```bash
    $ cd Backend/python-backend
    ```

2. Once you're in the project directory, install the required dependencies from the `requirements.txt` file. You can do this by running the following command:

    ```bash
    $ pip install -r requirements.txt
    ```

3. After installing the dependencies, you can then execute the backend application:

    ```bash
    $ python app.py
    ```




## Running the Frontend Application

Before running the frontend application, please make sure you have Node.js installed on your system. You can download and install Node.js from the official website: [Node.js Downloads](https://nodejs.org/en/download/)


To run the frontend application, follow these steps:

1. Open a new terminal and navigate to the project directory using the `cd` command:

    ```bash
    $ cd Frontend/pdf-frontend
    ```

2. Once you're in the project directory, install the required dependencies (node modules) by running:

    ```bash
    $ npm install
    ```
3. After installing the dependencies, you can then start the frontend application using the following command:

    ```bash
    $ npm start
    ```