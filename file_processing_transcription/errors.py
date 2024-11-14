class TranscriptionError(Exception):
    """Base exception for transcription-related issues in the file-processing-transcription library."""

class TranscriptionProcessingError(TranscriptionError):
    """
    Exception raised when an issue occurs during transcription processing.

    This could be due to file format issues, processing errors, or issues
    with the transcription model.
    """

class NotTranscriptionApplicableError(TranscriptionError):
    """
    Exception raised when transcription is attempted on a file type that does not support it.

    This error is useful for indicating that the file type does not contain
    audio or video content suitable for transcription.
    """
