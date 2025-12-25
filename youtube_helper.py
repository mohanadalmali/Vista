import yt_dlp
import requests

def ms_to_time(ms):
    """Milisaniyeyi [DK:SN] formatına çevirir"""
    seconds = int(ms) / 1000
    m, s = divmod(seconds, 60)
    return f"[{int(m):02d}:{int(s):02d}]"

def get_transcript_with_timestamps(video_url, lang_code=None):
    """
    Verilen URL'den transkripti çeker.
    Döndürdüğü: (full_content_string, selected_language_code)
    Hata durumunda: (None, error_message)
    """
    ydl_opts = {
        'skip_download': True,
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitlesformat': 'json3',
        'quiet': True,
    }

    if lang_code:
        ydl_opts['subtitleslangs'] = [lang_code]
    else:
        ydl_opts['subtitleslangs'] = ['all']

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            
            subtitle_url = None
            selected_lang = "Bilinmiyor"

            # --- Altyazı Seçme Mantığı ---
            if 'requested_subtitles' in info and info['requested_subtitles']:
                subs = info['requested_subtitles']
                
                if lang_code:
                    if lang_code in subs:
                        subtitle_url = subs[lang_code]['url']
                        selected_lang = lang_code
                    else:
                        return None, f"HATA: '{lang_code}' dili bulunamadı."
                else:
                    available_langs = list(subs.keys())
                    video_lang = info.get('language')
                    # Öncelik: Video dili -> İlk bulunan dil
                    if video_lang and video_lang in subs:
                        subtitle_url = subs[video_lang]['url']
                        selected_lang = video_lang
                    else:
                        selected_lang = available_langs[0]
                        subtitle_url = subs[selected_lang]['url']
            
            if subtitle_url:
                # JSON3 verisini çek
                if "fmt=json3" not in subtitle_url:
                    subtitle_url += "&fmt=json3"
                    
                response = requests.get(subtitle_url)
                data = response.json()
                
                lines_with_time = []
                
                if 'events' in data:
                    for event in data['events']:
                        start_ms = event.get('tStartMs', 0)
                        time_str = ms_to_time(start_ms)
                        
                        seg_text = ""
                        if 'segs' in event:
                            for seg in event['segs']:
                                if 'utf8' in seg and seg['utf8'] != '\n':
                                    seg_text += seg['utf8']
                        
                        if seg_text.strip():
                            # Format: [00:15] Metin
                            lines_with_time.append(f"{time_str} {seg_text}")
                
                full_content = "\n".join(lines_with_time)
                return full_content, selected_lang
            
            else:
                return None, "HATA: Bu videoda altyazı bulunamadı."

    except Exception as e:
        return None, f"SİSTEM HATASI: {e}"