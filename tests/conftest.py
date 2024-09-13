import pytest
from file_processing_transcription.transcription_decorator import TranscriptionDecorator


@pytest.fixture
def mock_audio_processor():
    """Fixture to set up a mock audio processor."""
    class MockProcessor:
        def __init__(self):
            self.file_path = "path/to/audio.mp3"
            self.extension = ".mp3"
            self.metadata = {}

        def process(self):
            pass

    return MockProcessor()

@pytest.fixture
def transcription_decorator(mock_audio_processor):
    """Fixture to set up TranscriptionDecorator with a mock processor."""
    return TranscriptionDecorator(mock_audio_processor)
