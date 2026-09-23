import requests

# Switched to JSONPlaceholder - an industry-standard, reliable dummy API for testing
BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_users_list_success():
    """Verify that the API successfully returns a list of users"""
    
    response = requests.get(f"{BASE_URL}/users")
    
    assert response.status_code == 200, f"Error: Expected status code 200, but got {response.status_code}"
    
    response_body = response.json()
    
    assert isinstance(response_body, list), "Response body is not a valid list"
    assert len(response_body) > 0, "The users list is empty"
    
    first_user_email = response_body[0]['email']
    print(f"\nFirst user's email: {first_user_email}")