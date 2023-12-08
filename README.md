# Chat Application with Speech Recognition and Translation

https://translateflaskapp.azurewebsites.net/

## Project Overview

This project is a Flask-based chat application that allows users to join chat rooms, send text and voice messages, and have messages automatically translated into their preferred language. It leverages Azure App Service for deployment and Docker for containerization.

## Dependencies

To run this application, you'll need the following dependencies:

- Python 3.8
- Flask
- SpeechRecognition
- [Docker](https://www.docker.com/get-started)



## How to Run the Program

Follow these steps to run the chat application:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/nicholasconterno/TranslateNet
   ```

2. Navigate to the project directory:

   ```bash
   cd TranslateNet
   ```

3. Build the Docker container by running the following command:

   ```bash
   docker build -t my-chat-app .
   ```

4. Run the Docker container:

   ```bash
   docker run -p 80:80 my-chat-app
   ```

5. Access the chat application in your web browser by going to [http://localhost](http://localhost).

6. Enter a room name, username, and select the input language and translation language.

7. You can start a voice recording by clicking the "Record" button. Your speech will be transcribed and sent as a message.

8. Messages in the chat room will be automatically translated into the selected language.

## Using the Makefile

The Makefile included in this project simplifies several routine tasks associated with the development and maintenance of the Flask chat application. Below is a guide on how to use the Makefile effectively.

### Prerequisites

Ensure that you have `make` installed on your system. You can check its presence by running `make --version` in your terminal. If it's not installed, you can typically install it via your operating system's package manager.

### Available Commands

The Makefile provides the following commands:

1. **`make lint`**: This command runs a linter (flake8) over the project's codebase to identify and report on stylistic or programming errors. It's essential for maintaining code quality and consistency.

2. **`make run`**: This command launches the Flask application. It's a quick way to start your server without needing to remember or type out the full command.

3. **`make test`**: This command runs the test suite for the application. It's crucial for ensuring that your application's functionality remains intact and that new changes don't break existing features.

### How to Use

1. **Linting the Code**:
   ```bash
   make lint
   ```
   Use this command to check the code for potential errors and style issues.

2. **Running the Application**:
   ```bash
   make run
   ```
   This command starts the Flask server, making the application accessible on your local machine.

3. **Running Tests**:
   ```bash
   make test
   ```
   Use this command to execute the application's test suite. It’s important to run this before making changes to the codebase or pushing new updates to ensure everything is functioning as expected.

## Github Actions

All testing linting and downloading of requirements are done via the ci.yml file and are done automatically on push via github actions.

## Flask Application
The flask app we made can be seen in s2s_model.py and is integraded with index.html. The endpoints can all be seen there. This works with our docker image seamlessly, and is hosted on Azure. Hosting on azure also gives some added security allowing use of google chrome's microphone, which is an added bonus. The application uses google translate's LLM to translate phrases from text-to-text. 


## Dockerhub

To deploy this image on Azure we used a docker image. To do this, we first created a Dockerfile, with commands that choose the specific python environment, install requirements, and run the flask app. We then use the following commands to set up the Docker Image properly for use in Azure.

```
docker build -t nconterno1/my-flask-app:latest .
```
This builds the docker image and must be done anytime changes to the codebase are made

```
docker run -p port1:port2 my-flask-app
```
This is not strictly necessary but runs the docker image locally and is good practice to test that the app works before spending the time to host it. 

```
docker tag nconterno1/my-flask-app:latest
```
and finally to push to dockerhub

```
docker push nconterno1/my-flask-app:latest
```
This image can then be used to deploy the app within Azure.

## Azure Web App

https://translateflaskapp.azurewebsites.net/

The link to to the publicly hosted web application is above. It is hosted with a basic instance as high amounts of traffic can't be supported due to API limits currently in place. 

## Recommendations to Management

### Scalability and Performance

- Consider monitoring the application's resource usage on Azure App Service, especially if it experiences heavy traffic or usage. Ensure that resources are appropriately scaled to handle demand.

### User Engagement

- Implement user engagement features such as notifications for new messages or voice messages to enhance user experience.

### Data Privacy and Security

- Ensure that any data collected or stored, especially chat messages, complies with data privacy regulations and is stored securely.

### Maintenance and Updates

- Regularly update the application dependencies, Docker image, and Azure services to keep the application secure and up-to-date.

### User Feedback

- Collect user feedback to make continuous improvements to the chat application, considering features and usability enhancements.

### Cost Optimization

- Periodically review the Azure App Service costs, especially if the application is paused during periods of inactivity, to optimize expenses.

