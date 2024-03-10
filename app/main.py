from fastapi import FastAPI

app = FastAPI()


@app.get("/cv_services/hello")
async def hello():
    # TODO: Find out how to read all or part of this data from a config file or DB.
    ENDPOINT_INFO = {
        "author": "Alejandro Gutiérrez",
        "description": "Endpoint that fetches information about my profesional profile and career history. All data is retrieved from a Mongo data base hosted in AWS.",
        "name": "CV Services",
        "version": "0.0.1"
    }
    return ENDPOINT_INFO


@app.get("/cv_services/profile")
async def profile_information():
    # TODO: This information will be fetched from Mongo.
    PROFILE_INFO = {
        "birth": "11/11/1970",
        "country_name": "United States",
        "email": "jsmith@example.com",
        "marital_status": "married",
        "name": "Jonh",
        "last_name": "Smith",
        "phone": "8888-8888",
        "social_media": {
            "git_hub": "",
            "linkedin": "",
            "instagram": "",
            "you_tube": ""
        }
    }
    return PROFILE_INFO
