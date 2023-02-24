"""
The Abstract Factory Pattern provides an interface for creating families of
related or dependent objects without specifying their concrete classes.
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


class ExporterFactory(ABC):
    @abstractmethod
    def get_video_exporter(self) -> VideoExporter:
        pass

    @abstractmethod
    def get_audio_exporter(self) -> AudioExporter:
        pass


class MasterQualityExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return MasterQualityVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return MasterQualityAudioExporter()


class HighQualityExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return HighQualityVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return HighQualityAudioExporter()


class LowQualityExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return LowQualityVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return LowQualityAudioExporter()


def read_factory():
    factories =  {
        "master": MasterQualityExporter(),
        "high": HighQualityExporter(),
        "low": LowQualityExporter()
    }
    while True:
        export_quality = input("Enter desired output quality (low, high, master): ")
        if export_quality in factories:
            return factories[export_quality]
        print(f"Unknown output quality option: {export_quality}.")


def main() -> None:
    factory = read_factory()

    # get the video and audio exporters
    video_exporter = factory.get_video_exporter()
    audio_exporter = factory.get_audio_exporter()

    # prepare the export
    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")

    # do the export
    folder = "/usr/tmp/video"
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    main()