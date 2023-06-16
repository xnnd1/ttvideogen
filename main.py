# pylint: disable=missing-module-docstring
import click
from src import video_creation

@click.command()
@click.option(
    '-bg', '--background', 'bg_path', multiple=True, required=True, help='Path to background videos'
)
@click.option(
    '-ol', '--overlay', 'overlay_path', required=True, help='Path to overlay video'
)
@click.option(
    '-o', '--output', 'output_path', required=True, help='Path to output video'
)
@click.option(
    '-l', '--length', 'video_length', default=180, help='Video length'
)
@click.option(
    '-oc', '--opacity', 'opacity', default=0.75, help='Opacity level'
)
@click.option(
    '-tds', '--threads', 'thread_count', default=4, help='Number of threads used for rendering'
)
def parse_cmd(
    bg_path: list,
    overlay_path: str,
    output_path: str,
    video_length: int,
    opacity: int,
    thread_count: int
) -> None:
    """
        Parse command-line arguments and start video creation
    """
    video_creation.make_video(
        bg_path, overlay_path, output_path, video_length, opacity, thread_count
    )

if __name__ == '__main__':
    parse_cmd() # pylint: disable=no-value-for-parameter
