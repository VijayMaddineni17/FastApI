1. We can start server by using "uvicorn main:app --reload"
2. Connections to databases present in 'database.py' in this project i have used SQLite3 and Postgresql
3. All the table schemas were created in 'models.py' file
4. All related new users and creating todos functions were present in todos.py
5. Alembic is a data migration tool where we can upgrade and downgrade our database using "alembic upgrade ref_no", "alembic downgrade -1"
6. 