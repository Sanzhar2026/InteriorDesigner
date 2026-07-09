# backend/app/routers/interior_designer.py
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse
import os
from datetime import datetime
import logging
from dotenv import load_dotenv
from app.services.sd_service import StableDiffusionService

load_dotenv()

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/interior", tags=["interior"])

# Инициализация сервиса Stable Diffusion
sd_service = StableDiffusionService()

# Стили интерьеров
STYLE_PROMPTS = {
    "modern": "Modern, clean lines, open space, minimalist decor, neutral colors",
    "classic": "Classic, elegant, traditional, rich colors, ornate details, timeless luxury",
    "minimalist": "Minimalist, simple, uncluttered, monochromatic, zen atmosphere",
    "loft": "Industrial loft, exposed brick, metal beams, urban style, open plan",
    "scandinavian": "Scandinavian, hygge, light wood, white walls, cozy textiles, natural light",
    "bohemian": "Bohemian, eclectic, colorful, patterned, vintage furniture, artistic",
    "artdeco": "Art Deco, luxurious, geometric patterns, bold colors, chrome accents",
    "japandi": "Japandi, Japanese-Scandinavian fusion, minimal, natural materials, wabi-sabi"
}

@router.post("/generate")
async def generate_interior(
    file: UploadFile = File(...),
    style: str = Form("modern")
):
    """Генерация интерьера через Stable Diffusion (Colab)"""
    try:
        # Проверка стиля
        if style not in STYLE_PROMPTS:
            valid_styles = ', '.join(STYLE_PROMPTS.keys())
            raise HTTPException(400, f"Неверный стиль. Доступны: {valid_styles}")
        
        # Проверка файла
        if not file.content_type or not file.content_type.startswith('image/'):
            raise HTTPException(400, "Файл должен быть изображением")
        
        # Чтение файла
        image_data = await file.read()
        if len(image_data) == 0:
            raise HTTPException(400, "Пустой файл")
        
        if len(image_data) > 10 * 1024 * 1024:
            raise HTTPException(400, "Файл слишком большой (макс 10MB)")
        
        logger.info(f"🔄 Генерация {style} для: {file.filename}")
        
        # Генерация через Stable Diffusion (Colab)
        image_urls = await sd_service.generate_interior(
            prompt=STYLE_PROMPTS[style],
            image_data=image_data,
            style=style,
            num_images=4
        )
        
        return {
            "success": True,
            "images": image_urls,
            "style": style,
            "count": len(image_urls),
            "generated_at": datetime.utcnow().isoformat()
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"❌ Ошибка: {str(e)}")
        raise HTTPException(500, f"Ошибка генерации: {str(e)}")

@router.get("/styles")
async def get_styles():
    """Получить список стилей"""
    styles = [
        {"id": key, "name": key.capitalize(), "description": value[:50] + "..."}
        for key, value in STYLE_PROMPTS.items()
    ]
    return {"styles": styles, "count": len(styles)}

@router.post("/inspire")
async def generate_inspiration(style: str = Form("modern")):
    """Генерация вдохновения без загрузки фото"""
    try:
        if style not in STYLE_PROMPTS:
            valid_styles = ', '.join(STYLE_PROMPTS.keys())
            raise HTTPException(400, f"Неверный стиль. Доступны: {valid_styles}")
        
        image_urls = await sd_service.generate_inspiration(style=style)
        
        return {
            "success": True,
            "images": image_urls,
            "style": style,
            "count": len(image_urls)
        }
        
    except Exception as e:
        logger.error(f"❌ Ошибка: {str(e)}")
        raise HTTPException(500, f"Ошибка: {str(e)}")
