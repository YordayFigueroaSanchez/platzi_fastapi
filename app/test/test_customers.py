from fastapi import status

def test_create_customer(client):
    response = client.post(
        "/customer", 
        json={
            "name": "John Doe", 
            "email": "john.doe@example.com", 
            "age": 30,
            "description": "Customer description"
        }
    )
    assert response.status_code == status.HTTP_201_CREATED
    
def test_read_customer(client):
    response = client.post(
        "/customer", 
        json={
            "name": "John Doe", 
            "email": "john.doe@example.com", 
            "age": 30,
            "description": "Customer description"
        }
    )
    assert response.status_code == status.HTTP_201_CREATED
    customer_id = response.json()["id"]
    response_read = client.get(f"/customer/{customer_id}")
    assert response_read.status_code == status.HTTP_200_OK
    assert response_read.json()["name"] == "John Doe"
    assert response_read.json()["email"] == "john.doe@example.com"
    assert response_read.json()["age"] == 30
    assert response_read.json()["description"] == "Customer description"
    