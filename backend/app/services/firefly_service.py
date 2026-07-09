# backend/app/services/firefly_service.py
import httpx
import base64
import os
import logging
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

class FireflyService:
    """Service for interacting with Adobe Firefly API"""
    
    def __init__(self):
        self.api_key = os.getenv("ADOBE_API_KEY")
        self.api_url = "https://firefly-api.adobe.io/v2/images/generate"
        self.timeout = 30.0
        
        if not self.api_key or self.api_key == "your_adobe_api_key_here":
            logger.warning("⚠️ Adobe API key not configured")
    
    async def generate_interior(
        self, 
        image_data: bytes, 
        style: str,
        style_prompts: Dict[str, str],
        num_variations: int = 4
    ) -> List[str]:
        """Generate interior design variations"""
        
        if not self.api_key or self.api_key == "your_adobe_api_key_here":
            raise ValueError("Adobe API key not configured")
        
        if style not in style_prompts:
            raise ValueError(f"Invalid style: {style}")
        
        # Convert image to base64
        base64_image = base64.b64encode(image_data).decode('utf-8')
        
        # Prepare request
        payload = {
            "prompt": style_prompts[style],
            "image": base64_image,
            "numVariations": num_variations,
            "size": "2048x2048",
            "quality": "high"
        }
        
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    self.api_url,
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json",
                        "X-Api-Key": self.api_key
                    },
                    json=payload
                )
            
            if response.status_code != 200:
                error_detail = "Unknown error"
                try:
                    error_data = response.json()
                    error_detail = error_data.get('message', error_data.get('error', 'Unknown error'))
                except:
                    error_detail = response.text[:200]
                
                raise Exception(f"Adobe API error: {error_detail}")
            
            result = response.json()
            outputs = result.get("outputs", [])
            
            image_urls = []
            for output in outputs:
                if "image" in output and "url" in output["image"]:
                    image_urls.append(output["image"]["url"])
            
            if not image_urls:
                raise Exception("No image URLs in response")
            
            return image_urls
            
        except httpx.TimeoutException:
            raise Exception("Request timeout")
        except httpx.RequestError as e:
            raise Exception(f"Network error: {str(e)}")
        except Exception as e:
            raise Exception(f"Generation failed: {str(e)}")
    
    async def generate_inspiration(self, style: str, style_prompts: Dict[str, str]) -> List[str]:
        """Generate inspiration images"""
        
        if not self.api_key or self.api_key == "your_adobe_api_key_here":
            raise ValueError("Adobe API key not configured")
        
        if style not in style_prompts:
            raise ValueError(f"Invalid style: {style}")
        
        payload = {
            "prompt": f"{style_prompts[style]}, wide angle view, professional interior design photography, 8k resolution, highly detailed, award-winning design",
            "numVariations": 4,
            "size": "2048x2048",
            "quality": "high"
        }
        
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    self.api_url,
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json",
                        "X-Api-Key": self.api_key
                    },
                    json=payload
                )
            
            if response.status_code != 200:
                error_detail = "Unknown error"
                try:
                    error_data = response.json()
                    error_detail = error_data.get('message', error_data.get('error', 'Unknown error'))
                except:
                    error_detail = response.text[:200]
                
                raise Exception(f"Adobe API error: {error_detail}")
            
            result = response.json()
            outputs = result.get("outputs", [])
            image_urls = []
            
            for output in outputs:
                if "image" in output and "url" in output["image"]:
                    image_urls.append(output["image"]["url"])
            
            return image_urls
            
        except Exception as e:
            raise Exception(f"Inspiration generation failed: {str(e)}")
