export interface DesignStyle {
  id: string;
  name: string;
  description: string;
  icon: string;
}

export interface GenerationResponse {
  success: boolean;
  images: string[];
  style: string;
  count: number;
  generated_at: string;
}

export interface StyleResponse {
  styles: DesignStyle[];
  count: number;
}
