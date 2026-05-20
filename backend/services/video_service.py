from moviepy.editor import (
    ImageClip,
    AudioFileClip,
    concatenate_videoclips,
    vfx
)

# function to create final video
def build_video(scenes, audio_path):

    clips = []

    print("Starting video rendering...")

    # loop through all scenes
    for scene in scenes:

        print("Processing scene...")

        # create cinematic image clip
        image_clip = (
            ImageClip(scene["image_path"])

            # vertical reel size
            .resize((1080, 1920))

            # scene duration
            .set_duration(scene["duration_sec"])

            # smooth fade transition
            .crossfadein(1)

            # cinematic zoom effect
            .fx(vfx.resize, lambda t: 1 + 0.02 * t)
        )

        # add clip to list
        clips.append(image_clip)

    # combine all scenes
    final_video = concatenate_videoclips(
        clips,
        method="compose"
    )

    # load generated voice audio
    audio = AudioFileClip(audio_path)

    # make video duration equal to audio duration
    final_video = final_video.set_duration(audio.duration)

    # attach audio to video
    final_video = final_video.set_audio(audio)

    # output path
    output_path = "outputs/final.mp4"

    print("Writing final video...")

    # export final video
    final_video.write_videofile(

        output_path,

        fps=24,

        codec="libx264",

        audio_codec="aac"
    )

    print("Video rendering completed!")

    # return final video path
    return output_path