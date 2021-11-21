import ormar
from ormar.fields.model_fields import Boolean
from sqlalchemy.sql.expression import table
from config import database, metadata

class Animal(ormar.Model):
    class Meta:
        tablename = "animais"
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True)
    nome: str = ormar.String(min_length=3, max_length=150, nullable=False)
    nomecientifico: str = ormar.String(max_length=150, nullable=False)
    especie: str = ormar.String(max_length=150, nullable=False)
    subclasse: str = ormar.String(max_length=150, nullable=False)
    expectativavida: str = ormar.String(max_length=150, nullable=False)
    alimentacao: str = ormar.String(max_length=150, nullable=True)
    reino: str = ormar.String(max_length=150, nullable=False)
    habitat: str = ormar.String(max_length=150, nullable=False)
    nativo: str = ormar.String(max_length=150, nullable=True)
    extincao: bool = ormar.Boolean(nullable=False)
