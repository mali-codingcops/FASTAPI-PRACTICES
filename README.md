# FAST API PRACTICES Project

![Project FASTAPI](./assets/images/logo.png)

## The following operation and command are used while creating this project.
## 1. Creating and setting up the github repository
###### git config --global user.email "you@example.com"
###### git config --global user.name "Your Name"
###### git init
###### git add README.md
###### git commit -m "Adding the README.md file"
###### git branch -M main
###### git status //checking the branch and content
###### git remote add origin https://github.com/mali-codingcops/FASTAPI-PRACTICES.git
###### git push -u origin main 
###### Adding the .gitignore file to ignore the unwanted file push to repository
###### git pull
## 2. Creating the virtual environment
###### apt install python3.8-venv 
###### python3 -m venv venv
## 3. Activating the virtual enviroment 
###### source venv/bin/activate
## 4. Adding the requirements.txt file to install the requrire packages as needed
###### pip install requirements.txt
## 5. Creating a main.py file with a simple path operation fun
## 6. Runing the FASTAPI Application locally
###### uvicorn main:app --reload or python3 main.py
###### http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redoc
###### Creating Schema to send a POST Request
###### Adding database.py file to build the connection for sqlalchemy
###### Creating models.py file for database model respectively.
## 7. Creating a separate branch for products router e.g. product_branch
## 8. Modifying the Project Structure. Created folder like Curd, Models, Schemas, Routers Using APIRouter and include_router functionality.
## 9. Creating the Product Entity:
###### 9.1 Path Operation e.g. 
###### POST /product/products/
###### GET /product/get_products/
###### GET /product/get_products/{product_id}/

###### 9.2 Performaning the CURD Operation like Create, READ, UPdate, Delete
###### 9.3 Handling the status code with HTTPException.
###### 9.4 validating the Required Schema as needed. such Product_name Shouldn't empty, stock can't be negative number 9.5 using pydantic field_validator

## 10. Creating the Category Entity:
###### 10.1 Path Operation and cateogry schemas, models, APIRouter, include router
###### GET /category/get_category
###### POST /category/create_category/
###### DELETE /category/delete_category/

## 11. Creating Building the ORM Relations ONE To Many between Product and Category table.

## Key Features
###### Learning the path operation (routes) like get, post
###### Daynamic routes paths e.g /item/{id}
###### Query routes parametter path e.g def items(limited = 10, is_active: Optional[bool] = None)  /items/limited=10&is_active=Flase