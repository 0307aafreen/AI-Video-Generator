import os
import time
import requests
import urllib.parse

# function to generate image
def generate_image(prompt, scene_number):

    print(f"Generating image for scene {scene_number}...")

    # convert prompt into url-safe text
    encoded_prompt = urllib.parse.quote(prompt)

    # pollinations image url
    image_url = (
        f"https://image.pollinations.ai/prompt/{encoded_prompt}"
    )

    # create outputs folder
    os.makedirs("outputs", exist_ok=True)

    # image save path
    image_path = f"outputs/scene_{scene_number}.png"

    # retry system
    for attempt in range(3):

        try:

            print(f"Attempt {attempt + 1}")

            response = requests.get(

                image_url,

                timeout=90
            )

            # check success
            if response.status_code == 200:

                with open(image_path, "wb") as file:

                    file.write(response.content)

                print(f"Image saved: {image_path}")

                return image_path

            else:

                print(
                    f"API Error: {response.status_code}"
                )

        except Exception as e:

            print(f"Retry Error: {e}")

        # wait before retry
        time.sleep(5)

    # if all retries fail
    raise Exception(
        "Image generation failed after retries"
    )