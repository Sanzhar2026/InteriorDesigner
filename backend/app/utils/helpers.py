# backend/app/utils/helpers.py
import base64
from PIL import Image
import io
import logging
from typing import Tuple, Optional

logger = logging.getLogger(__name__)

def validate_image(image_data: bytes, max_size_mb: int = 10) -> Tuple[bool, Optional[str]]:
    """
    Validate image data
    
    Args:
        image_data: Image bytes
        max_size_mb: Maximum file size in MB
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    try:
        # Check size
        max_size_bytes = max_size_mb * 1024 * 1024
        if len(image_data) > max_size_bytes:
            return False, f"Image too large. Maximum size: {max_size_mb}MB"
        
        # Try to open with PIL to validate image
        try:
            image = Image.open(io.BytesIO(image_data))
            image.verify()  # Verify it's a valid image
            return True, None
        except Exception as e:
            logger.error(f"Invalid image: {str(e)}")
            return False, "Invalid image file"
            
    except Exception as e:
        logger.error(f"Image validation error: {str(e)}")
        return False, f"Image validation failed: {str(e)}"

def image_to_base64(image_data: bytes) -> str:
    """Convert image bytes to base64 string"""
    return base64.b64encode(image_data).decode('utf-8')

def get_image_info(image_data: bytes) -> dict:
    """Get image information"""
    try:
        image = Image.open(io.BytesIO(image_data))
        return {
            "width": image.width,
            "height": image.height,
            "format": image.format,
            "mode": image.mode,
            "size_bytes": len(image_data),
            "size_mb": round(len(image_data) / (1024 * 1024), 2)
        }
    except Exception as e:
        logger.error(f"Failed to get image info: {str(e)}")
        return {}

def format_style_name(style_id: str) -> str:
    """Format style ID to display name"""
    return style_id.replace('_', ' ').title()

def sanitize_filename(filename: str) -> str:
    """Sanitize filename for safe usage"""
    import re
    # Remove any path separators
    filename = os.path.basename(filename)
    # Remove any non-ASCII characters
    filename = re.sub(r'[^a-zA-Z0-9._-]', '', filename)
    return filename
