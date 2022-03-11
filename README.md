# Ask Confluence
Welcome! This application consists of a back-end solution wit
h API, and a front-end connected to this API.

## Prerequisites
1. Clone this repository
2. Install `Python >3.8`
3. Install [Node.js](https://nodejs.org/en/)
3. Install [poetry](https://python-poetry.org/)
4. Run ``poetry shell``
5. Run ``poetry install``

## Back-end
Back-end solution downloads data from a specified Confluence space, transforms this data, and uploads the data to the [Open AI Answer API](https://beta.openai.com/docs/api-reference/answers) together with a question where its answer can be found among the downloaded Confluence pages.

To download and transform data from Confluence, add your credentials to the file `configs/.secrets.yml`. See [this](https://developer.atlassian.com/cloud/confluence/basic-auth-for-rest-apis/#supplying-basic-auth-headers) guide from Atlassian for how to generate your auth token in Confluence. Then, run the following command
```
python -m ask_confluence.pipeline
```

## POST API /askConfluence/
This API takes in a question and retrieves answer based on the downloaded and transformed data now located in `data/interim`. To run the API application, run
```
uvicorn ask_confluence.app.resource.main:app --reload
```
Now, the API should be available with Swagger in http://127.0.0.1:8000/docs. 

## Front-end
To run a simple front-end application that is connected to the `/askConfluence/` API, run
```
cd frontend_app
npm install
npm run dev
```
Now, the front-end should be available at [localhost:3000](localhost:3000).