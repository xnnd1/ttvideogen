# pylint: disable=missing-module-docstring
from moviepy.editor import (
    VideoFileClip,
    CompositeVideoClip,
    vfx,
    concatenate_videoclips,
)

# First element is height, second is width
resolution = (1920, 1080)


def make_video(
    bg_path: list,
    overlay_path: str,
    output_path: str,
    video_length: int,
    opacity: int,
    thread_count: int,
) -> None:
    """
    Basically cupcut template for tech savvy tiktok algorithm abusers like me :)
    Read comments to understand what it does.
    """
    # Empty list of background video clips' paths
    bg_clips_paths = []
    # Create overlay videoclip
    overlay_clip = VideoFileClip(overlay_path)

    # Append background videoclips to list with given resolution and without audio
    for i in bg_path:
        bg_clips_paths.append(
            VideoFileClip(i, target_resolution=resolution, audio=False)
        )

    # Make one big videoclip of all background videoclips
    # stored in list, and loop&cut it to video length
    bg_clips = concatenate_videoclips(bg_clips_paths)
    bg_clips = bg_clips.fx(vfx.loop, duration=video_length)  # pylint: disable=no-member
    bg_clips = bg_clips.subclip(0, video_length)

    # Set overlay videoclip opacity to given opacity,
    # resize it to normal width, and center it
    overlay_clip = overlay_clip.set_opacity(opacity)
    overlay_clip = overlay_clip.fx(vfx.resize, width=1080)  # pylint: disable=no-member
    overlay_clip = overlay_clip.set_position(("center", 327))

    # Make composition of background clips and overlay clip, and cut it to video length
    video = CompositeVideoClip([bg_clips, overlay_clip]).subclip(0, video_length)

    # Write composition to output path with 60 FPS, 4 threads and blah blah blah no one cares lmfao
    video.write_videofile(
        output_path,
        fps=60,
        threads=thread_count,
        temp_audiofile="temp-audio.m4a",
        remove_temp=True,
        codec="libx264",
        audio_codec="aac",
    )
