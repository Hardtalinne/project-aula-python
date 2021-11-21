from fastapi import APIRouter, HTTPException, status

from models.animal import Animal

router = APIRouter()

@router.get("")
async def list_animal(nome: str = None):
    resultado = await Animal.objects.filter(Animal.nome.icontains(nome)).all() if nome else await Animal.objects.all()

    if(resultado == []):
        raise HTTPException(status_code=404, detail="Não encontrado.")

    return resultado

@router.get("/extincao")
async def list_animal():
    extintos = await Animal.objects.filter(Animal.extincao.icontains(1)).all()
    nao_extintos = await Animal.objects.filter(Animal.extincao.icontains(0)).all()

    return {
        'extintos': {
            'total': len(extintos),
            'animais': extintos
        }, 
        'nao_extintos': {
            'total': len(nao_extintos),
            'animais': nao_extintos
        }
    }

@router.get("/{id}")
async def list_animal(id: str):
    return await Animal.objects.get(pk=id)


@router.post("", status_code=status.HTTP_201_CREATED)
async def store_animal(animal: Animal):
    if(len(animal.nome) <= 3):
        raise HTTPException(status_code=422, detail="Nome de animal inválido, mínino de 3 caracteres.")

    await animal.save()
    return animal

@router.patch("/{id}")
async def update_animal(id: str, animal: Animal):
    animal_db = await Animal.objects.get(pk=id)
    animal.id = animal_db.id
    return await animal_db.update(**animal.dict())

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_animal(id: str):
    animal_db = await Animal.objects.get(pk=id)
    return await animal_db.delete()
    
