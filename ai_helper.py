from openai import OpenAI

def analyze_transcript_with_deepseek(api_key, transcript_text):
    """
    DeepSeek API kullanarak metni analiz eder:
    1. Özet
    2. Konu Kümeleme (Topics)
    3. Önemli Cümleler (Highlights/Segmentation)
    """
    if not api_key:
        return "Lütfen geçerli bir API Anahtarı girin."
    
    # DeepSeek Client Tanımlama
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com"
    )

    # Prompt (AI'a ne yapması gerektiğini söylüyoruz)
    system_prompt = """
    Sen uzman bir video analiz asistanısın. Görevin verilen video transkriptini analiz etmektir.
    Çıktıyı şu formatta ve Türkçe olarak ver:
    
    ### 📝 ÖZET
    (Buraya videonun genel, kapsamlı bir özetini yaz.)

    ### 🗂️ KONU BAŞLIKLARI
    (Buraya videoda geçen ana konuları madde işaretleri ile kümele.)
    - Konu 1
    - Konu 2
    
    ### 🎯 ÖNEMLİ CÜMLELER
    (Buraya videodaki en vurucu, en önemli 3-5 cümleyi olduğu gibi alıntıla.)
    """

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"İşte analiz etmen gereken transkript:\n\n{transcript_text[:30000]}"} 
                # Not: Çok uzun videolar için ilk 30k karakteri aldık, token limitine takılmamak için.
            ],
            temperature=0.7
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"API Hatası: {str(e)}"