from applications.app import app

with app.test_request_context() as context:
    pass
