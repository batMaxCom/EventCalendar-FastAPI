from fastapi import APIRouter

router = APIRouter(
    prefix='/event',
    tags=['Events']
)


@router.get('')
async def list_events():
    """
    Показать все события
    """
    pass


@router.get('/{event_id}')
async def retrieve_event(event_id: int):
    """
    Показать событие по ID
    """
    pass


@router.post('')
async def create_event():
    """
    Создать событие
    """
    pass


@router.put('/{event_id}')
async def edit_event(event_id: int):
    """
    Изменить событие
    """
    pass


@router.delete('/{event_id}')
async def delete_even(event_id: int):
    """
    Удалить событие
    """
    pass
