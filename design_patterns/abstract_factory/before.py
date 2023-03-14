"""
The Abstract Factory Pattern provides an interface for creating families of
related or dependent objects without specifying their concrete classes.
"""
"""
In the example below, the main function has to know about all the video and
audio exporter classes, and has the logic to decide which classes to
instantiate.
"""
from abc import ABC, abstractmethod


class VideoExporter(ABC):
    @abstractmethod
    def prepare_export(self, video_data):
        pass

    @abstractmethod
    def do_export(self, folder):
        pass


class AudioExporter(ABC):
    @abstractmethod
    def prepare_export(self, audio_data):
        pass

    @abstractmethod
    def do_export(self, folder):
        pass


class MasterQualityVideoExporter(VideoExporter):
    def prepare_export(self, video_data):
        print("Preparing video data for master quality export.")

    def do_export(self, folder):
        print(f"Exporting video data in master quality to {folder}.")


class HighQualityVideoExporter(VideoExporter):
    def prepare_export(self, video_data):
        print("Preparing video data for high quality export.")

    def do_export(self, folder):
        print(f"Exporting video data in high quality to {folder}.")


class LowQualityVideoExporter(VideoExporter):
    def prepare_export(self, video_data):
        print("Preparing video data for low quality export.")

    def do_export(self, folder):
        print(f"Exporting video data in low quality to {folder}.")


class MasterQualityAudioExporter(AudioExporter):
    def prepare_export(self, audio_data):
        print("Preparing audio data for master quality export.")

    def do_export(self, folder):
        print(f"Exporting audio data in master quality to {folder}.")


class HighQualityAudioExporter(AudioExporter):
    def prepare_export(self, audio_data):
        print("Preparing audio data for high quality export.")

    def do_export(self, folder):
        print(f"Exporting audio data in high quality to {folder}.")


class LowQualityAudioExporter(AudioExporter):
    def prepare_export(self, audio_data):
        print("Preparing audio data for low quality export.")

    def do_export(self, folder):
        print(f"Exporting audio data in low quality to {folder}.")


def read_export_quality():
    export_quality: str
    while True:
        export_quality = input("Enter desired output quality (low, high, master): ")
        if export_quality in {"low", "high", "master"}:
            return export_quality
        print(f"Unknown output quality option: {export_quality}.")


def main() -> None:
    export_quality = read_export_quality()

    # create the video and audio exporters
    video_exporter: VideoExporter
    audio_exporter: AudioExporter
    if export_quality == "low":
        video_exporter = LowQualityVideoExporter()
        audio_exporter = LowQualityAudioExporter()
    elif export_quality == "high":
        video_exporter = HighQualityVideoExporter()
        audio_exporter = HighQualityAudioExporter()
    else:
        # default: master quality
        video_exporter = MasterQualityVideoExporter()
        audio_exporter = MasterQualityAudioExporter()

    # prepare the export
    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")

    # do the export
    folder = "/usr/tmp/video"
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    main()
