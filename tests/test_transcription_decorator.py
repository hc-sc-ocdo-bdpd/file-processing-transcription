import pytest
from unittest.mock import patch, MagicMock
from file_processing_transcription.transcription_decorator import TranscriptionDecorator
from file_processing_transcription.errors import TranscriptionProcessingError


@pytest.mark.parametrize("transcribed_text, language", [
    ('Transcribed text 1', 'en'),
    ('Transcribed text 2', 'es'),
    ('Transcribed text 3', 'fr'),
])
def test_transcription_processing(mock_audio_processor, transcribed_text, language):
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
def test_transcription_processing_error(mock_audio_processor, exception_message):
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
