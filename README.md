# Web_form_spotter is an endpoint which accepts forms and searches for suitable templates within database

## Description:
Accepts url_encoded forms if suitable form is found within db, the client 
will receive a request with json, which keeps template's name;
If no matching template was found, the endpoint will return such template.

### Additional notes:
- Post request endpoint path: /spot_form/
- the request must hold "Content-type": "x-www-form-urlencoded" header
- the form may be empty but corresponding status code and message will be 
  return (204)
- form field "name" is reserved after template's name, thus when searching for comparison this field is ignored
- populate_db.py provides a cli tool for pushing into db prebuilt templates
- for running on local machine you need to activate venv(wfs_venv) first
- file .env is being used for storing db_name
- to deploy this project you need to launch docker-compose file, thus 
  Dockerfile and compose files must be present in the same directory as app 
  directory, after launching the container application will start if no 
  conflicts will occur 
- /tests/test_wfs_client.py uses Starlette TestClient class to test 
  endpoint as whole, without launching app on either local machine or 
  container; /tests/test_spotter_endpoint.py holds basic tests themselves

## Requirements:
# Python:
- [Python 3.11.4](https://www.python.org/downloads/)
# Deployment and testing: 
- [docker 24.0.6](https://docs.docker.com/get-docker/)
- [Postman](https://www.postman.com/downloads/)
# Significant Libraries and Frameworks:
- [fastapi 0.104.1](https://fastapi.tiangolo.com)
- [python-decouple 3.8](https://pypi.org/project/python-decouple/)
- [httpx 0.25.1](https://www.python-httpx.org)
- [pytest 7.4.3](https://docs.pytest.org/en/7.4.x/)

# Notes on listed dependencies:
- pytest provides testing functionality, but for correct work with 
  coroutines pytest-asyncio should also be installed
- for the same reason httpx should be installed, without it Starlette 
  TestClient won't work with FasApi 
