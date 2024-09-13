import whisper
import torch
from file_processing_transcription.errors import TranscriptionProcessingError


class TranscriptionDecorator:
    def __init__(self, processor, model_name: str = 'base') -> None:
        """Initializes the TranscriptionDecorator with a given file processor."""
        self._processor = processor
        self.model_name = model_name

    def process(self) -> None:
        """Processes the file using the wrapped processor and then applies transcription."""
        self._processor.process()
        transcribed_text, language = self.extract_text_with_whisper()
        self._processor.metadata['transcribed_text'] = transcribed_text
        self._processor.metadata['transcribed_language'] = language

    def extract_text_with_whisper(self) -> tuple:
        """Extracts text from the file using Whisper by OpenAI.

        Returns:
            tuple: The extracted text and detected language.
        """
        try:
            has_gpu = torch.cuda.is_available()
            device = 'cuda' if has_gpu else 'cpu'

            model = whisper.load_model(self.model_name, device=device)

            result = model.transcribe(
                audio=str(self._processor.file_path),
                fp16=has_gpu
            )
            return result['text'], result['language']
        except Exception as e:
            raise TranscriptionProcessingError(
                f"Error during transcription processing: {e}"
            )

    # Properties to expose metadata for easier access
    @property
    def file_name(self) -> str:
        return self._processor.file_name

    @property
    def extension(self) -> str:
        return self._processor.extension

    @property
    def owner(self) -> str:
        return self._processor.owner

    @property
    def size(self) -> str:
        return self._processor.size

    @property
    def modification_time(self) -> str:
        return self._processor.modification_time

    @property
    def access_time(self) -> str:
        return self._processor.access_time

    @property
    def creation_time(self) -> str:
        return self._processor.creation_time

    @property
    def parent_directory(self) -> str:
        return self._processor.parent_directory

    @property
    def permissions(self) -> str:
        return self._processor.permissions

    @property
    def is_file(self) -> bool:
        return self._processor.is_file

    @property
    def is_symlink(self) -> bool:
        return self._processor.is_symlink

    @property
    def absolute_path(self) -> str:
        return self._processor.absolute_path

    @property
    def metadata(self) -> dict:
        return self._processor.metadata
