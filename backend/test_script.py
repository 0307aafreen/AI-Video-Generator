from services.script_service import generate_script
from services.image_service import generate_image
from services.voice_service import generate_voice
from services.video_service import build_video

# generate ai script
result = generate_script(
    "30 second motivational cinematic video about consistency"
)

print(result)

# generate images for all scenes
for index, scene in enumerate(result["scenes"]):

    image_path = generate_image(
        scene["visual_prompt"],
        index + 1
    )

    # save image path into scene
    scene["image_path"] = image_path

# combine all narration text
all_narration = " ".join(
    scene["narration"]
    for scene in result["scenes"]
)

# generate voice
voice_path = generate_voice(all_narration)

# build final video
video_path = build_video(
    result["scenes"],
    voice_path
)

print("Final Video:", video_path)