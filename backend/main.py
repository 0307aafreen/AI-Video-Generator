import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from models.request_models import PromptRequest

from services.script_service import generate_script
from services.image_service import generate_image
from services.voice_service import generate_voice
from services.video_service import build_video

# create fastapi app
app = FastAPI()

# allow frontend connection
app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

# create outputs folder automatically
os.makedirs("outputs", exist_ok=True)

# allow browser access to outputs folder
app.mount(

    "/outputs",

    StaticFiles(directory="outputs"),

    name="outputs"
)

# home route
@app.get("/")
def home():

    return {
        "message": "AI Video Generator Backend Running"
    }

# main video generation endpoint
@app.post("/generate-video")
def create_video(data: PromptRequest):

    try:

        print("\n==============================")
        print("Generating AI script...")

        # generate cinematic script
        result = generate_script(data.prompt)

        print("Script generated successfully")

        print("Generating images...")

        # generate images for all scenes
        for index, scene in enumerate(result["scenes"]):

            image_path = generate_image(

                scene["visual_prompt"],

                index + 1
            )

            # save generated image path
            scene["image_path"] = image_path

        print("Images generated successfully")

        print("Generating voice...")

        # combine all narration text
        all_narration = " ".join(

            scene["narration"]

            for scene in result["scenes"]
        )

        # generate voice audio
        voice_path = generate_voice(all_narration)

        print("Voice generated successfully")

        print("Building final video...")

        # generate final mp4 video
        video_path = build_video(

            result["scenes"],

            voice_path
        )

        print("Video generated successfully")
        print("==============================\n")

        # success response
        return {

            "success": True,

            "message": "Video generated successfully",

            "video_url":
            f"http://127.0.0.1:8000/{video_path}"
        }

    except Exception as e:

        print("\nBACKEND ERROR:")
        print(e)

        return JSONResponse(

            status_code=500,

            content={

                "success": False,

                "error": str(e)
            }
        )