from fastapi import FastAPI, Depends
import models
from database import engine, SessionLocal
from routers import todos,users,address,auth
from company import companyapis



app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(address.router)
app.include_router(companyapis.router,
                   prefix="/companyapis",
                   tags=["companyapis"],
                   responses={418:{"description":"Internal Use Only"}})
app.include_router(users.router)
app.include_router(address.router)
