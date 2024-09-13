import pytest
from unittest.mock import patch, MagicMock
from file_processing_transcription.transcription_decorator import TranscriptionDecorator
from file_processing_transcription.errors import TranscriptionProcessingError


def test_transcription_processing(mock_audio_processor):
    """Test transcription processing with an audio file."""
    transcription_decorator = TranscriptionDecorator(mock_audio_processor)

    # Mocking the whisper model and its transcribe method
    with patch('whisper.load_model') as mock_load_model:
        mock_model = MagicMock()
        mock_model.transcribe.return_value = {
            'text': 'Transcribed text',
            'language': 'en'
        }
        mock_load_model.return_value = mock_model

        transcription_decorator.process()

        assert 'transcribed_text' in transcription_decorator.metadata
        assert 'transcribed_language' in transcription_decorator.metadata
        assert transcription_decorator.metadata['transcribed_text'] == 'Transcribed text'
        assert transcription_decorator.metadata['transcribed_language'] == 'en'


def test_transcription_processing_error(mock_audio_processor):
    """Test transcription processing failure scenario."""
    transcription_decorator = TranscriptionDecorator(mock_audio_processor)

    # Simulate transcription processing error
    with patch('whisper.load_model') as mock_load_model:
        mock_model = MagicMock()
        mock_model.transcribe.side_effect = Exception('Transcription error')
        mock_load_model.return_value = mock_model

        with pytest.raises(TranscriptionProcessingError):
            transcription_decorator.process()
