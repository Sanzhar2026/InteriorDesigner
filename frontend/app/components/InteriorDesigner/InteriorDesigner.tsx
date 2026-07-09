'use client';

import { useState, useRef } from 'react';
import Image from 'next/image';
import { 
  Upload, 
  Sparkles, 
  Download, 
  RefreshCw, 
  X, 
  Image as ImageIcon,
  Loader2
} from 'lucide-react';

const STYLES = [
  { id: 'modern', name: 'Modern', description: 'Clean & contemporary', icon: '🏛️' },
  { id: 'classic', name: 'Classic', description: 'Elegant & timeless', icon: '👑' },
  { id: 'minimalist', name: 'Minimalist', description: 'Simple & clean', icon: '⬜' },
  { id: 'loft', name: 'Loft', description: 'Industrial chic', icon: '🏭' },
  { id: 'scandinavian', name: 'Scandinavian', description: 'Cozy & natural', icon: '❄️' },
  { id: 'bohemian', name: 'Bohemian', description: 'Eclectic & free', icon: '🌺' },
  { id: 'artdeco', name: 'Art Deco', description: 'Luxurious & geometric', icon: '💎' },
  { id: 'japandi', name: 'Japandi', description: 'East meets West', icon: '🎋' },
];

export default function InteriorDesigner() {
  const [uploadedImage, setUploadedImage] = useState<string | null>(null);
  const [uploadedFile, setUploadedFile] = useState<File | null>(null);
  const [selectedStyle, setSelectedStyle] = useState('modern');
  const [results, setResults] = useState<string[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [selectedResult, setSelectedResult] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleImageUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      setUploadedFile(file);
      const reader = new FileReader();
      reader.onload = (event) => {
        setUploadedImage(event.target?.result as string);
      };
      reader.readAsDataURL(file);
      setError(null);
    }
  };

  const handleGenerate = async () => {
    if (!uploadedFile) {
      setError('Пожалуйста, загрузите фото');
      return;
    }

    setIsLoading(true);
    setError(null);
    setResults([]);
    
    const formData = new FormData();
    formData.append('file', uploadedFile);
    formData.append('style', selectedStyle);
    
    try {
      const response = await fetch('/api/interior/generate', {
        method: 'POST',
        body: formData,
      });
      
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Generation failed');
      }
      
      const data = await response.json();
      
      if (data.images && data.images.length > 0) {
        setResults(data.images);
      } else {
        throw new Error('No images generated');
      }
    } catch (error) {
      console.error('Generation error:', error);
      setError(error instanceof Error ? error.message : 'Failed to generate design');
    } finally {
      setIsLoading(false);
    }
  };

  const handleDownload = (url: string) => {
    window.open(url, '_blank');
  };

  const handleReset = () => {
    setUploadedImage(null);
    setUploadedFile(null);
    setResults([]);
    setSelectedResult(null);
    setError(null);
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  };

  return (
    <div className="max-w-7xl mx-auto p-6">
      <div className="text-center mb-12">
        <h1 className="text-4xl md:text-5xl font-bold mb-4">
          <span className="bg-gradient-to-r from-cyan-400 via-purple-400 to-pink-400 bg-clip-text text-transparent">
            AI Interior Designer
          </span>
        </h1>
        <p className="text-gray-400 max-w-2xl mx-auto">
          Загрузите фото комнаты и получите 4 варианта дизайна
        </p>
        <div className="mt-4 inline-block px-4 py-2 bg-green-500/20 border border-green-500/50 rounded-lg text-green-400 text-sm">
          ✅ Работает через Stable Diffusion (облачный GPU)
        </div>
      </div>

      <div className="grid lg:grid-cols-5 gap-8">
        <div className="lg:col-span-2 space-y-6">
          <div className="bg-[#111113] rounded-xl border border-white/10 p-6">
            <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
              <ImageIcon className="w-5 h-5 text-cyan-400" />
              Загрузите фото
            </h3>
            
            <div
              onClick={() => fileInputRef.current?.click()}
              className={`relative border-2 border-dashed rounded-xl p-8 text-center cursor-pointer transition-all ${
                uploadedImage 
                  ? 'border-cyan-400/50 bg-cyan-400/5' 
                  : 'border-white/20 hover:border-white/40 bg-white/5 hover:bg-white/10'
              }`}
            >
              {uploadedImage ? (
                <div className="relative aspect-square max-w-[200px] mx-auto">
                  <Image
                    src={uploadedImage}
                    alt="Uploaded room"
                    fill
                    className="object-cover rounded-lg"
                  />
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      handleReset();
                    }}
                    className="absolute -top-2 -right-2 p-1 bg-red-500 rounded-full hover:bg-red-600 transition"
                  >
                    <X className="w-4 h-4" />
                  </button>
                </div>
              ) : (
                <>
                  <Upload className="w-12 h-12 mx-auto text-gray-500 mb-4" />
                  <p className="text-gray-400">Нажмите чтобы загрузить фото</p>
                  <p className="text-gray-500 text-sm mt-2">JPG, PNG, WEBP (до 10MB)</p>
                </>
              )}
              <input
                ref={fileInputRef}
                type="file"
                accept="image/*"
                onChange={handleImageUpload}
                className="hidden"
              />
            </div>
          </div>

          <div className="bg-[#111113] rounded-xl border border-white/10 p-6">
            <h3 className="text-lg font-semibold mb-4">Выберите стиль</h3>
            <div className="grid grid-cols-2 gap-2">
              {STYLES.map((style) => (
                <button
                  key={style.id}
                  onClick={() => setSelectedStyle(style.id)}
                  className={`p-3 rounded-xl text-left transition-all duration-200 ${
                    selectedStyle === style.id
                      ? 'bg-gradient-to-r from-cyan-500/30 to-purple-500/30 border-2 border-cyan-400 shadow-lg shadow-cyan-500/20 scale-[1.02]'
                      : 'bg-white/5 border border-white/10 hover:border-white/30 hover:bg-white/10 hover:scale-[1.01]'
                  }`}
                >
                  <div className="text-2xl mb-1">{style.icon}</div>
                  <div className={`font-medium text-sm transition-colors ${
                    selectedStyle === style.id ? 'text-cyan-400' : 'text-white'
                  }`}>
                    {style.name}
                  </div>
                  <div className="text-xs text-gray-400">{style.description}</div>
                  {selectedStyle === style.id && (
                    <div className="mt-1 w-full h-0.5 bg-gradient-to-r from-cyan-400 to-purple-400 rounded-full animate-pulse" />
                  )}
                </button>
              ))}
            </div>
          </div>

          <div className="space-y-3">
            <button
              onClick={handleGenerate}
              disabled={!uploadedImage || isLoading}
              className="w-full bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-600 hover:to-purple-700 disabled:opacity-50 disabled:cursor-not-allowed text-white font-medium py-4 px-6 rounded-xl transition-all flex items-center justify-center gap-2 shadow-lg shadow-cyan-500/20"
            >
              {isLoading ? (
                <>
                  <Loader2 className="w-5 h-5 animate-spin" />
                  Генерация...
                </>
              ) : (
                <>
                  <Sparkles className="w-5 h-5" />
                  Сгенерировать дизайн
                </>
              )}
            </button>

            <button
              onClick={handleReset}
              disabled={!uploadedImage && results.length === 0}
              className="w-full border border-white/10 hover:bg-white/5 disabled:opacity-50 disabled:cursor-not-allowed text-gray-400 font-medium py-3 px-6 rounded-xl transition-all flex items-center justify-center gap-2"
            >
              <RefreshCw className="w-4 h-4" />
              Начать заново
            </button>
          </div>

          {error && (
            <div className="bg-red-500/10 border border-red-500/50 text-red-400 p-4 rounded-xl">
              {error}
            </div>
          )}
        </div>

        <div className="lg:col-span-3">
          <div className="bg-[#111113] rounded-xl border border-white/10 p-6 min-h-[500px]">
            {isLoading ? (
              <div className="flex flex-col items-center justify-center h-full">
                <div className="relative">
                  <div className="w-24 h-24 border-4 border-cyan-400/20 border-t-cyan-400 rounded-full animate-spin" />
                  <Sparkles className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-8 h-8 text-cyan-400 animate-pulse" />
                </div>
                <p className="text-gray-400 mt-4">Создаём ваш дизайн...</p>
                <p className="text-gray-500 text-sm">Генерация на облачном GPU может занять 30-60 секунд</p>
              </div>
            ) : results.length > 0 ? (
              <div>
                <div className="flex items-center justify-between mb-4">
                  <h3 className="text-lg font-semibold">Варианты дизайна</h3>
                  <span className="px-3 py-1 bg-cyan-400/10 text-cyan-400 text-sm rounded-full">
                    {results.length} вариантов
                  </span>
                </div>
                <div className="grid grid-cols-2 gap-4">
                  {results.map((url, index) => (
                    <div
                      key={index}
                      className="relative group aspect-square rounded-xl overflow-hidden border border-white/10 hover:border-cyan-400/50 transition-all cursor-pointer"
                      onClick={() => setSelectedResult(url)}
                    >
                      <Image
                        src={url}
                        alt={`Вариант ${index + 1}`}
                        fill
                        className="object-cover group-hover:scale-105 transition-transform duration-300"
                      />
                      <div className="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity" />
                      <div className="absolute bottom-2 left-2 right-2 flex justify-between items-center opacity-0 group-hover:opacity-100 transition-opacity">
                        <span className="px-2 py-1 bg-black/60 backdrop-blur-sm text-xs rounded-full">
                          #{index + 1}
                        </span>
                        <button
                          onClick={(e) => {
                            e.stopPropagation();
                            handleDownload(url);
                          }}
                          className="p-2 bg-white/20 backdrop-blur-sm rounded-full hover:bg-white/30 transition"
                        >
                          <Download className="w-4 h-4" />
                        </button>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            ) : (
              <div className="flex flex-col items-center justify-center h-full text-gray-500">
                <ImageIcon className="w-16 h-16 mb-4 opacity-20" />
                <p>Загрузите фото и выберите стиль</p>
                <p className="text-sm">Нажмите &quot;Сгенерировать дизайн&quot;</p>
              </div>
            )}
          </div>
        </div>
      </div>

      {selectedResult && (
        <div
          className="fixed inset-0 bg-black/80 backdrop-blur-sm flex items-center justify-center z-50 p-4"
          onClick={() => setSelectedResult(null)}
        >
          <div
            className="relative max-w-4xl w-full bg-[#111113] rounded-xl overflow-hidden"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="relative aspect-video">
              <Image
                src={selectedResult}
                alt="Просмотр"
                fill
                className="object-contain"
              />
            </div>
            <div className="absolute top-4 right-4 flex gap-2">
              <button
                onClick={() => handleDownload(selectedResult)}
                className="p-2 bg-cyan-500 hover:bg-cyan-600 rounded-full transition"
              >
                <Download className="w-5 h-5" />
              </button>
              <button
                onClick={() => setSelectedResult(null)}
                className="p-2 bg-black/60 backdrop-blur-sm hover:bg-black/80 rounded-full transition"
              >
                <X className="w-5 h-5" />
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
