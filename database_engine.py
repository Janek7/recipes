import logging
import datetime
import typing

from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database setup
DATABASE_URL = "sqlite:///recipes.db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


# Define ORM entity classes
class Recipe(Base):
    __tablename__ = "Recipe"
    recipe_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    date = Column(Date, nullable=False)
    description = Column(String(255))
    source = Column(String(255), nullable=False)
    source_link = Column(String(255))
    categorie = Column(String(255), nullable=False)
    web_domain = Column(String(255))
    web_title = Column(String(255))
    instagram_account_name = Column(String(255))
    content_structured = Column(Text)
    content_freetext = Column(Text)
    ingredients = relationship("Ingredient", back_populates="recipe")
    instructions = relationship("Instruction", back_populates="recipe")
    images = relationship("Image", back_populates="recipe")
    tags = relationship("Tag", back_populates="recipe")

    def __repr__(self):
        return f"Recipe {self.recipe_id}: {self.title}"


class Ingredient(Base):
    __tablename__ = "Ingredient"
    ingredient_id = Column(Integer, primary_key=True, autoincrement=True)
    recipe_id = Column(Integer, ForeignKey("Recipe.recipe_id"), nullable=False)
    name = Column(String(255), nullable=False)
    quantity = Column(String(255))
    recipe = relationship("Recipe", back_populates="ingredients")


class Instruction(Base):
    __tablename__ = "Instruction"
    instruction_id = Column(Integer, primary_key=True, autoincrement=True)
    recipe_id = Column(Integer, ForeignKey("Recipe.recipe_id"), nullable=False)
    instruction = Column(Text, nullable=False)
    order_number = Column(Integer)
    recipe = relationship("Recipe", back_populates="instructions")


class Image(Base):
    __tablename__ = "Image"
    foto_id = Column(Integer, primary_key=True, autoincrement=True)
    recipe_id = Column(Integer, ForeignKey("Recipe.recipe_id"), nullable=False)
    file_name = Column(String(255), nullable=False)
    recipe = relationship("Recipe", back_populates="images")


class Tag(Base):
    __tablename__ = "Tag"
    tag_id = Column(Integer, primary_key=True, autoincrement=True)
    recipe_id = Column(Integer, ForeignKey("Recipe.recipe_id"), nullable=False)
    tag = Column(String(255), nullable=False)
    recipe = relationship("Recipe", back_populates="tags")


# Create database tables
def create_database():
    logging.info("Creating database and tables.")
    Base.metadata.create_all(engine)
    logging.info("Database and tables created successfully.")


# Insert dummy data
def insert_dummy_data():
    logging.info("Truncating tables before inserting dummy data.")
    session = SessionLocal()
    session.query(Tag).delete()
    session.query(Image).delete()
    session.query(Instruction).delete()
    session.query(Ingredient).delete()
    session.query(Recipe).delete()
    session.commit()
    
    logging.info("Inserting dummy data into tables.")
    recipe = Recipe(title="Spaghetti Carbonara", date=datetime.date(2024, 2, 6), description="Classic Italian pasta dish", 
                    source="Cookbook", source_link="http://example.com", categorie="Pasta")
    session.add(recipe)
    session.commit()
    
    ingredient1 = Ingredient(recipe_id=recipe.recipe_id, name="Spaghetti", quantity="200g")
    ingredient2 = Ingredient(recipe_id=recipe.recipe_id, name="Eggs", quantity="2")
    session.add_all([ingredient1, ingredient2])
    
    instruction1 = Instruction(recipe_id=recipe.recipe_id, instruction="Boil the spaghetti.", order_number=1)
    instruction2 = Instruction(recipe_id=recipe.recipe_id, instruction="Mix eggs with cheese.", order_number=2)
    session.add_all([instruction1, instruction2])
    
    image = Image(recipe_id=recipe.recipe_id, file_name="carbonara.jpg")
    session.add(image)
    
    tag = Tag(recipe_id=recipe.recipe_id, tag="Italian")
    session.add(tag)
    
    session.commit()
    session.close()
    logging.info("Dummy data inserted successfully.")

# Read methods
def get_all_recipes():
    logging.info("Fetching all recipes.")
    session = SessionLocal()
    recipes = session.query(Recipe).all()
    session.close()
    return recipes

def get_all_ingredients():
    logging.info("Fetching all ingredients.")
    session = SessionLocal()
    ingredients = session.query(Ingredient).all()
    session.close()
    return ingredients

def get_all_instructions():
    logging.info("Fetching all instructions.")
    session = SessionLocal()
    instructions = session.query(Instruction).all()
    session.close()
    return instructions

def get_all_images():
    logging.info("Fetching all images.")
    session = SessionLocal()
    images = session.query(Image).all()
    session.close()
    return images

def get_all_tags():
    logging.info("Fetching all tags.")
    session = SessionLocal()
    tags = session.query(Tag).all()
    session.close()
    return tags


if __name__ == "__main__":
    create_database()
    insert_dummy_data()

    recipes = get_all_recipes()
    for r in recipes:
        print(r)