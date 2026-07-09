# backend/app/services/sd_service.py
import httpx
import base64
import logging
from typing import List
import os

logger = logging.getLogger(__name__)

class StableDiffusionService:
    """Сервис для работы с Stable Diffusion API (Colab)"""
    
    def __init__(self):
        # Используем ngrok URL из Colab
        self.api_url = os.getenv("SD_API_URL", "http://127.0.0.1:8000")
        self.timeout = 120.0
        logger.info(f"📡 SD API URL: {self.api_url}")
    
    async def generate_interior(
        self,
        prompt: str,
        image_data: bytes,
        style: str,
        num_images: int = 4
    ) -> List[str]:
        """Генерация интерьеров через Stable Diffusion"""
        try:
            files = {
                "file": ("image.jpg", image_data, "image/jpeg")
            }
            data = {"style": style}
            
            logger.info(f"🔄 Отправка запроса к SD API: {self.api_url}/generate")
            
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.api_url}/generate",
                    files=files,
                    data=data
                )
                
                if response.status_code != 200:
                    error_data = response.json()
                    logger.error(f"❌ SD API ошибка: {error_data}")
                    raise Exception(error_data.get("error", "Unknown error"))
                
                result = response.json()
                images = result.get("images", [])
                logger.info(f"✅ Получено {len(images)} изображений")
                return images
                
        except httpx.TimeoutException:
            logger.error("❌ Таймаут при запросе к SD")
            raise Exception("Stable Diffusion timeout. Попробуйте позже.")
        except Exception as e:
            logger.error(f"❌ Ошибка генерации: {str(e)}")
            raise Exception(str(e))
    
    async def generate_inspiration(self, style: str) -> List[str]:
        """Генерация вдохновения"""
        try:
            data = {"style": style}
            
            logger.info(f"🔄 Отправка запроса к SD API: {self.api_url}/inspire")
            
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.api_url}/inspire",
                    data=data
                )
                
                if response.status_code != 200:
                    error_data = response.json()
                    logger.error(f"❌ SD API ошибка: {error_data}")
                    raise Exception(error_data.get("error", "Unknown error"))
                
                result = response.json()
                images = result.get("images", [])
                logger.info(f"✅ Получено {len(images)} изображений")
                return images
                
        except Exception as e:
            logger.error(f"❌ Ошибка: {str(e)}")
            raise Exception(f"Inspiration generation failed: {str(e)}")
