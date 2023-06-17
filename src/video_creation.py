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
    Make video based on background videos and overlay video.

    :param bg_path: list: List of paths to background videos.
    :param overlay_path: str: Path to overlay video.
    :param output_path: str: Output video path.
    :param video_length: int: Output video length in seconds.
    :param opacity: int: Overlay video opacity
    :param thread_count: int: Threads used for rendering video.

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
    bg_clips = (
        concatenate_videoclips(bg_clips_paths)
        .fx(vfx.loop, duration=video_length)
        .subclip(0, video_length)
    )

    # Set overlay videoclip opacity to given opacity,
    # resize it to normal width, and center it
    overlay_clip = (
        overlay_clip.set_opacity(opacity)
        .fx(vfx.resize, width=resolution[1])
        .set_position(("center", 327))
    )

    # Make composition of background clips and overlay clip, and cut it to video length
    video = CompositeVideoClip([bg_clips, overlay_clip]).subclip(0, video_length)

    # Write composition to output path
    video.write_videofile(
        output_path,
        fps=60,
        threads=thread_count,
        temp_audiofile="temp-audio.m4a",
        remove_temp=True,
        codec="libx264",
        audio_codec="aac",
    )
