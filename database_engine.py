import logging
import datetime
import typing

from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import pandas as pd

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
        return f"<Recipe(id={self.recipe_id}, title='{self.title}', date={self.date}, source='{self.source}')>"


    @classmethod
    def insert(cls, session, obj):
        session.add(obj)
        session.commit()

    @classmethod
    def get_by_id(cls, session, recipe_id):
        return session.query(cls).filter_by(recipe_id=recipe_id).first()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def update(cls, session, recipe_id, **kwargs):
        recipe = session.query(cls).filter_by(recipe_id=recipe_id).first()
        if recipe:
            for key, value in kwargs.items():
                setattr(recipe, key, value)
            session.commit()
        return recipe

    @classmethod
    def delete(cls, session, recipe_id):
        recipe = session.query(cls).filter_by(recipe_id=recipe_id).first()
        if recipe:
            session.delete(recipe)
            session.commit()
        return recipe


class Ingredient(Base):
    __tablename__ = "Ingredient"
    ingredient_id = Column(Integer, primary_key=True, autoincrement=True)
    recipe_id = Column(Integer, ForeignKey("Recipe.recipe_id"), nullable=False)
    name = Column(String(255), nullable=False)
    quantity = Column(String(255))
    recipe = relationship("Recipe", back_populates="ingredients")

    def __repr__(self):
        return f"<Ingredient(id={self.ingredient_id}, name='{self.name}', quantity='{self.quantity}', recipe_id={self.recipe_id})>"

    @classmethod
    def insert(cls, session, obj):
        session.add(obj)
        session.commit()

    @classmethod
    def get_by_id(cls, session, ingredient_id):
        return session.query(cls).filter_by(ingredient_id=ingredient_id).first()

    @classmethod
    def get_by_recipe_id(cls, session, recipe_id):
        return session.query(cls).filter_by(recipe_id=recipe_id).all()

    @classmethod
    def update(cls, session, ingredient_id, **kwargs):
        ingredient = session.query(cls).filter_by(ingredient_id=ingredient_id).first()
        if ingredient:
            for key, value in kwargs.items():
                setattr(ingredient, key, value)
            session.commit()
        return ingredient

    @classmethod
    def delete(cls, session, ingredient_id):
        ingredient = session.query(cls).filter_by(ingredient_id=ingredient_id).first()
        if ingredient:
            session.delete(ingredient)
            session.commit()
        return ingredient


class Instruction(Base):
    __tablename__ = "Instruction"
    instruction_id = Column(Integer, primary_key=True, autoincrement=True)
    recipe_id = Column(Integer, ForeignKey("Recipe.recipe_id"), nullable=False)
    instruction = Column(Text, nullable=False)
    order_number = Column(Integer)
    recipe = relationship("Recipe", back_populates="instructions")

    def __repr__(self):
        return f"<Instruction(id={self.instruction_id}, order_number={self.order_number}, instruction='{self.instruction[:50]}...')>"

    @classmethod
    def insert(cls, session, obj):
        session.add(obj)
        session.commit()

    @classmethod
    def get_by_id(cls, session, instruction_id):
        return session.query(cls).filter_by(instruction_id=instruction_id).first()

    @classmethod
    def get_by_recipe_id(cls, session, recipe_id):
        return session.query(cls).filter_by(recipe_id=recipe_id).all()

    @classmethod
    def update(cls, session, instruction_id, **kwargs):
        instruction = session.query(cls).filter_by(instruction_id=instruction_id).first()
        if instruction:
            for key, value in kwargs.items():
                setattr(instruction, key, value)
            session.commit()
        return instruction

    @classmethod
    def delete(cls, session, instruction_id):
        instruction = session.query(cls).filter_by(instruction_id=instruction_id).first()
        if instruction:
            session.delete(instruction)
            session.commit()
        return instruction


class Image(Base):
    __tablename__ = "Image"
    foto_id = Column(Integer, primary_key=True, autoincrement=True)
    recipe_id = Column(Integer, ForeignKey("Recipe.recipe_id"), nullable=False)
    file_name = Column(String(255), nullable=False)
    image_number = Column(Integer)
    recipe = relationship("Recipe", back_populates="images")

    def __repr__(self):
        return f"<Image(id={self.foto_id}, image_number='{self.image_number}', file_name='{self.file_name}', recipe_id={self.recipe_id})>"

    @classmethod
    def insert(cls, session, obj):
        session.add(obj)
        session.commit()

    @classmethod
    def get_by_id(cls, session, foto_id):
        return session.query(cls).filter_by(foto_id=foto_id).first()

    @classmethod
    def get_by_recipe_id(cls, session, recipe_id):
        return session.query(cls).filter_by(recipe_id=recipe_id).all()

    @classmethod
    def update(cls, session, foto_id, **kwargs):
        image = session.query(cls).filter_by(foto_id=foto_id).first()
        if image:
            for key, value in kwargs.items():
                setattr(image, key, value)
            session.commit()
        return image

    @classmethod
    def delete(cls, session, foto_id):
        image = session.query(cls).filter_by(foto_id=foto_id).first()
        if image:
            session.delete(image)
            session.commit()
        return image


class Tag(Base):
    __tablename__ = "Tag"
    tag_id = Column(Integer, primary_key=True, autoincrement=True)
    recipe_id = Column(Integer, ForeignKey("Recipe.recipe_id"), nullable=False)
    tag = Column(String(255), nullable=False)
    recipe = relationship("Recipe", back_populates="tags")

    def __repr__(self):
        return f"<Tag(id={self.tag_id}, tag='{self.tag}', recipe_id={self.recipe_id})>"

    @classmethod
    def insert(cls, session, obj):
        session.add(obj)
        session.commit()

    @classmethod
    def get_by_id(cls, session, tag_id):
        return session.query(cls).filter_by(tag_id=tag_id).first()

    @classmethod
    def get_by_recipe_id(cls, session, recipe_id):
        return session.query(cls).filter_by(recipe_id=recipe_id).all()

    @classmethod
    def update(cls, session, tag_id, **kwargs):
        tag = session.query(cls).filter_by(tag_id=tag_id).first()
        if tag:
            for key, value in kwargs.items():
                setattr(tag, key, value)
            session.commit()
        return tag

    @classmethod
    def delete(cls, session, tag_id):
        tag = session.query(cls).filter_by(tag_id=tag_id).first()
        if tag:
            session.delete(tag)
            session.commit()
        return tag



# Create database tables
def create_database():
    logging.info("Creating database and tables.")
    Base.metadata.create_all(engine)
    logging.info("Database and tables created successfully.")


def truncate_tables(tables: typing.List) -> None:
    """
    truncate a given list of tables
    """
    logging.info(f"Truncate {len(tables)} tables: {' '.join([str(t) for t in tables])}")
    session = SessionLocal()
    for table in tables:
        session.query(table).delete()
    session.commit()
    session.close()
    logging.info("Successfully truncated!")


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
    
    image = Image(recipe_id=recipe.recipe_id, image_number=1, file_name="carbonara.jpg")
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


# util methods
def insert_recipe_from_dataframe(session, idx: int, recipe_row: pd.Series) -> None:
    """
    inserts a recipe row from excel data into the tables Recipe, Tag and Image
    """
    tags = [Tag(tag=recipe_row["Source"])] + ([Tag(tag="Top")] if pd.notna(recipe_row['Top']) else [])
    images = [Image(file_name=recipe_row[f"Image {i}"], image_number=i) 
              for i in range(1,4) if pd.notna(recipe_row[f"Image {i}"])]

    recipe = Recipe(
        # recipe_id=idx,
        title=recipe_row["Recipe"],
        date=recipe_row["Date"],
        description=recipe_row["Description"],
        source=recipe_row["Source"],
        source_link=recipe_row["Source Link"],
        categorie=recipe_row["Category"],
        tags=tags,
        images=images
    )
    Recipe.insert(session, recipe)


if __name__ == "__main__":
    create_database()
    # insert_dummy_data()

    recipes = get_all_recipes()
    for r in recipes:
        print(r)