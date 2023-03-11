# WezaCare Challenge Backend API

This is the documentation for the WezaCare Backend API. The API provides functionality for users to register, log in, post questions, answer questions, retrieve questions and answers, and view their own questions.

The base URL for the API is: `https://wezacare-backend-challenge.vercel.app/api/`.

## Technologies Used

- Django
- Django Rest Framework
- Simple JWT

## Authentication

To use the API, users must first register an account and then log in to obtain a JWT token. JWT tokens should be included in the Authorization header of all requests to the API.

### Register

Endpoint: `POST /auth/register`

This endpoint allows users to register for an account.

#### Request Parameters

- `username`: The username of the user (string, required)
- `password`: The password of the user (string, required)

#### Response

- `message`: A message indicating the success or failure of the request (string)
- `token`: A JWT token that can be used to authenticate the user in subsequent requests (string)

### Login

Endpoint: `POST /auth/login`

This endpoint allows users to log in to their account.

#### Request Parameters

- `username`: The username of the user (string, required)
- `password`: The password of the user (string, required)

#### Response

- `message`: A message indicating the success or failure of the request (string)
- `token`: A JWT token that can be used to authenticate the user in subsequent requests (string)

## Questions

### Fetch All Questions

Endpoint: `GET /questions`

This endpoint returns all questions posted on the platform.

#### Request Parameters

None

#### Response

- `questions`: An array of all questions posted on the platform

### Post a Question

Endpoint: `POST /questions`

This endpoint allows authenticated users to post a question to the platform.

#### Request Parameters

- `title`: The title of the question (string, required)
- `body`: The body of the question (string, required)

#### Response

- `message`: A message indicating the success or failure of the request (string)
- `question`: The question that was posted (object)

### Fetch a Specific Question

Endpoint: `GET /questions/<questionId>`

This endpoint returns a specific question and all answers provided so far for the question.

#### Request Parameters

- `questionId`: The ID of the question to fetch (string, required)

#### Response

- `question`: The question that was fetched (object)
- `answers`: An array of all answers provided for the question

### Delete a Question

Endpoint: `DELETE /questions/<questionId>`

This endpoint allows the authenticated author of a question to delete the question.

#### Request Parameters

- `questionId`: The ID of the question to delete (string, required)

#### Response

- `message`: A message indicating the success or failure of the request (string)

### Post an Answer to a Question

Endpoint: `POST /questions/<questionId>/answers`

This endpoint allows authenticated users to provide answers to a question.

#### Request Parameters

- `body`: The body of the answer (string, required)

#### Response

- `message`: A message indicating the success or failure of the request (string)
- `answer`: The answer that was posted (object)

### Update an Answer

Endpoint: `PUT /questions/<questionId>/answers/<answerId>`

This endpoint allows the authenticated author of an answer to update the answer.

#### Request Parameters

- `answerId`: The ID of the answer to update (string, required)
- `body`: The new body of the answer (string)
