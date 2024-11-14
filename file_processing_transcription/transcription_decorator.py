import whisper
import torch
from file_processing_transcription.errors import TranscriptionProcessingError

class TranscriptionDecorator:
    """
    A decorator class that adds transcription capabilities to file processors.

    This class wraps around a file processor to provide audio and video transcription
    using OpenAI's Whisper model, allowing spoken content to be converted to text.

    Attributes:
        _processor: The underlying file processor to which transcription is added.
        model_name (str): The name of the Whisper model to use for transcription.
    """

    def __init__(self, processor, model_name: str = 'base') -> None:
        """
        Initializes the TranscriptionDecorator with a given file processor.

        Args:
            processor: The file processor to which transcription functionality will be added.
            model_name (str): The Whisper model to use (e.g., 'base', 'small', etc.).
        """
        self._processor = processor
        self.model_name = model_name

    def process(self) -> None:
        """
        Processes the file using the wrapped processor and then applies transcription.

        The transcription is performed on audio and video files, and the transcribed
        text and detected language are added to the file's metadata.
        """
        self._processor.process()
        transcribed_text, language = self.extract_text_with_whisper()
        self._processor.metadata['transcribed_text'] = transcribed_text
        self._processor.metadata['transcribed_language'] = language

    def extract_text_with_whisper(self) -> tuple:
        """
        Extracts text from the file using OpenAI's Whisper model.

        Returns:
            tuple: A tuple containing the transcribed text and the detected language.

        Raises:
            TranscriptionProcessingError: If an error occurs during transcription processing.
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

    @property
    def file_name(self) -> str:
        """Returns the file name."""
        return self._processor.file_name

    @property
    def extension(self) -> str:
        """Returns the file extension."""
        return self._processor.extension

    @property
    def owner(self) -> str:
        """Returns the file owner."""
        return self._processor.owner

    @property
    def size(self) -> str:
        """Returns the file size in bytes."""
        return self._processor.size

    @property
    def modification_time(self) -> str:
        """Returns the file modification time."""
        return self._processor.modification_time

    @property
    def access_time(self) -> str:
        """Returns the file access time."""
        return self._processor.access_time

    @property
    def creation_time(self) -> str:
        """Returns the file creation time."""
        return self._processor.creation_time

    @property
    def parent_directory(self) -> str:
        """Returns the file's parent directory path."""
        return self._processor.parent_directory

    @property
    def permissions(self) -> str:
        """Returns the file permissions."""
        return self._processor.permissions

    @property
    def is_file(self) -> bool:
        """Returns True if the path is a file."""
        return self._processor.is_file

    @property
    def is_symlink(self) -> bool:
        """Returns True if the path is a symbolic link."""
        return self._processor.is_symlink

    @property
    def absolute_path(self) -> str:
        """Returns the absolute path of the file."""
        return self._processor.absolute_path

    @property
    def metadata(self) -> dict:
        """Returns the metadata dictionary of the file."""
        return self._processor.metadata
