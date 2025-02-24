from fastapi import FastAPI
from app.database import engine, Base
from app.routes import student_routes, topic_routes, image_routes#,ocr_routes

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(student_routes.router, prefix="/api")
app.include_router(topic_routes.router, prefix="/api")
#app.include_router(ocr_routes.router, prefix="/api")
app.include_router(image_routes.router, prefix="/api") 