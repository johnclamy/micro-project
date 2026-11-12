from fastapi import FastAPI, Query, HTTPException
from typing import Optional
from .schema import MenuResponse
from .data import menu_items


app = FastAPI(title='Restaurant menu')


@app.get("/menu", response_model=MenuResponse)
async def get_menu(category: Optional[str] = Query(
    default=None,
    description="Filter by category"
)):
    # 01. Return the list of menu items if no category is specified
    # -------------------------------------------
    if category is None:
        return MenuResponse(items=menu_items, status='success', count=len(menu_items))
    # -------------------------------------------

    # 02. Filter the menu items by category if specified
    # -------------------------------------------
    filtered_items = [item for item in menu_items if item.category == category]

    # 03. Raise an HTTPException if no items are found for the specified category
    # -------------------------------------------
    if not filtered_items:
        raise HTTPException(
            status_code=404,
            detail="No items found for the specified category"
        )
    # -------------------------------------------
    
    return filtered_items


@app.get("/menu/{item_id}", response_model=MenuResponse)
async def get_menu_item(item_id: int):
    # 01. Find the menu item by ID
    # -------------------------------------------
    item = next((item for item in menu_items if item.id == item_id), None)

    # 02. Raise an HTTPException if the item is not found
    # -------------------------------------------
    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Menu item not found"
        )
    # -------------------------------------------

    return MenuResponse(items=[item], status='success', count=1)
