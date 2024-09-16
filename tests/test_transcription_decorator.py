import pytest
from pathlib import Path
import shutil
from unittest.mock import patch, MagicMock
from file_processing_transcription.transcription_decorator import TranscriptionDecorator
from file_processing_transcription.errors import TranscriptionProcessingError
from file_processing_test_data import get_test_files_path


# Mocked Tests (retain these for speed and isolated testing)
@pytest.mark.parametrize("transcribed_text, language", [
    ('Transcribed text 1', 'en'),
    ('Transcribed text 2', 'es'),
    ('Transcribed text 3', 'fr'),
])
def test_mocked_transcription_processing(mock_audio_processor, transcribed_text, language):
    """Test transcription processing with different transcribed texts and languages."""
    transcription_decorator = TranscriptionDecorator(mock_audio_processor)

    # Mocking the whisper model and its transcribe method
    with patch('whisper.load_model') as mock_load_model:
        mock_model = MagicMock()
        mock_model.transcribe.return_value = {
            'text': transcribed_text,
            'language': language
        }
        mock_load_model.return_value = mock_model

        transcription_decorator.process()

        assert 'transcribed_text' in transcription_decorator.metadata
        assert 'transcribed_language' in transcription_decorator.metadata
        assert transcription_decorator.metadata['transcribed_text'] == transcribed_text
        assert transcription_decorator.metadata['transcribed_language'] == language


@pytest.mark.parametrize("exception_message", [
    ('Transcription error 1'),
    ('Transcription error 2'),
    ('Transcription error 3'),
])
def test_mocked_transcription_processing_error(mock_audio_processor, exception_message):
    """Test transcription processing failure scenarios."""
    transcription_decorator = TranscriptionDecorator(mock_audio_processor)

    # Simulate transcription processing error
    with patch('whisper.load_model') as mock_load_model:
        mock_model = MagicMock()
        mock_model.transcribe.side_effect = Exception(exception_message)
        mock_load_model.return_value = mock_model

        with pytest.raises(TranscriptionProcessingError) as exc_info:
            transcription_decorator.process()

        assert exception_message in str(exc_info.value)
        

# Confirm ffmpeg is not found in system PATH
def test_ffmpeg_in_path():
    """Test if 'ffmpeg' is in the system PATH."""
    ffmpeg_path = shutil.which('ffmpeg')
    assert ffmpeg_path is not None, "'ffmpeg' is not in the system PATH"


# Real File Tests (using actual files from file-processing-test-data)
@pytest.mark.parametrize("file_name", [
    'sample_speech.aiff',
    'sample_speech.flac',
    'sample_speech.mp3',
    'sample_speech.mp4',
    'sample_speech.ogg',
    'sample_speech.wav',
])
def test_real_file_transcription(file_name):
    """Test real file transcription using Whisper model on actual audio files."""
    test_files_path = get_test_files_path()
    audio_file_path = test_files_path / file_name

    # Create a simple mock processor to pass to the decorator
    class MockProcessor:
        def __init__(self, file_path):
            self.file_path = file_path
            self.extension = file_path.suffix
            self.metadata = {}

        def process(self):
            pass

    processor = MockProcessor(audio_file_path)
    transcription_decorator = TranscriptionDecorator(processor)

    # Process the file using the actual Whisper model
    transcription_decorator.process()

    # Check that transcription text was generated
    assert 'transcribed_text' in transcription_decorator.metadata
    assert len(transcription_decorator.metadata['transcribed_text']) > 0
