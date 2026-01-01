from moviepy.editor import *
from gtts import gTTS
import requests
from PIL import Image
from io import BytesIO

# Leer historia desde archivo
with open("historia.txt", "r", encoding="utf-8") as f:
    escenas = f.read().split("\n\n")  # cada párrafo = una escena

clips = []

# Generar escenas con narración y fondo
for i, texto in enumerate(escenas):
    # Voz narrada
    tts = gTTS(text=texto, lang="es")
    voz_file = f"voz{i}.mp3"
    tts.save(voz_file)

    # Imagen distinta para cada escena (ejemplo con picsum.photos)
    url = f"https://picsum.photos/640/480?random={i}"
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.save(f"fondo{i}.jpg")

    # Fondo con efecto
    bg = ImageClip(f"fondo{i}.jpg").set_duration(20).resize((640,480))
    bg_moving = bg.fx(vfx.zoom_in, 1.1)

    # Texto sobre la escena
    txt = TextClip(texto, fontsize=40, color='white',
                   size=(640,480), method="caption").set_duration(20)

    # Escena con narración
    scene = CompositeVideoClip([bg_moving, txt.set_position("center")]).set_audio(AudioFileClip(voz_file))
    clips.append(scene)

# Concatenar todas las escenas
final = concatenate_videoclips(clips)

# Agregar música de fondo (opcional)
try:
    musica_file = "musica.mp3"  # sube tu archivo de música con este nombre
    audio_musica = AudioFileClip(musica_file).subclip(0, final.duration)
    final = final.set_audio(CompositeAudioClip([final.audio, audio_musica.volumex(0.3)]))
except:
    print("No se encontró música, se usará solo narración.")

# Escena final con CTA
cta = TextClip("Si te gustó este relato, dale like y suscríbete 🙌",
               fontsize=50, color="yellow", size=(640,480),
               method="caption").set_duration(8)
final = concatenate_videoclips([final, cta])

# Exportar video
final.write_videofile("video_final.mp4", fps=24)

print("Video guardado como: video_final.mp4")
