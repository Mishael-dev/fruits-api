from fastapi import FastAPI

api = FastAPI()

@api.get("/")
def index():
    return {"message": "welcome to the fruits app! Visit /docs for documentation"}

fruits = [
    {"fruit_id": 1, "name": "Mango", "price": 100},
    {"fruit_id": 2, "name": "Apple", "price": 150},
    {"fruit_id": 3, "name": "Orange", "price": 80},
    {"fruit_id": 4, "name": "Avocado", "price": 200}
]

#to get one fruit
@api.get("/fruits/{fruit_id}")
def get_one_friut(fruit_id: int):
    for fruit in fruits:
        if (fruit["fruit_id"] == fruit_id):
            return {"result": {fruit}}

#to get a list of all the fruits
@api.get("/fruits")
def get_fruits_list(first_n: int = None):
    if (first_n):
        return {"result": fruits[:first_n]}
    else:
        return {"result": fruits}

#to add another fruit to the list
@api.post("/fruits")
def add_fruit(fruit: dict):
    new_fruit_id = max(fruit["fruit_id"] for fruit in fruits) + 1
    new_fruit = {
        "fruit_id": new_fruit_id,
        "name": fruit["name"],
        "price": fruit["price"]
    }

    fruits.append(new_fruit)
    return {"result": new_fruit}

#to update an existing fruit
@api.put("/fruits/{fruit_id}")
def update_a_fruit(fruit_id: int, fruit: dict):
    for fruit_item in fruits:
        if fruit_item["fruit_id"] == fruit_id:
            fruit_item["name"] = fruit["name"]
            fruit_item["price"] = fruit["price"]
            return fruit_item
    # only return error after loop completes
    raise HTTPException(status_code=404, detail="Fruit not found")

#to delete a fruit
@api.delete("/fruits/{fruit_id}")
def delete_a_fruit(fruit_id: int):
    for fruit in fruits:
        if fruit["fruit_id"]==fruit_id:
            fruits.remove(fruit)

    return {"result": fruits}