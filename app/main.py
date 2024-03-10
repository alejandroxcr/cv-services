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
        "birth": "16/06/1986",
        "country_name": "Costa Rica",
        "email": "alejandroxcr@gmail.com",
        "marital_status": "married",
        "name": "Alejandro",
        "last_name": "Gutiérrez Mata",
        "phone": "8316-2066",
        "social_media": {
            "git_hub": "",
            "linkedin": "",
            "instagram": "",
            "you_tube": ""
        }
    }
    return PROFILE_INFO
