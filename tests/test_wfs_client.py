from starlette.testclient import TestClient
from app.main import app


test_app = TestClient(app)
