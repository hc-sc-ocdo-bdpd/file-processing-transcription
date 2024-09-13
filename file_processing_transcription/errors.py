class TranscriptionError(Exception):
    """Base exception for transcription related issues."""


class TranscriptionProcessingError(TranscriptionError):
    """Raised when there's an issue during transcription processing."""


class NotTranscriptionApplicableError(TranscriptionError):
    """Raised when attempting transcription on a file type that doesn't support it."""
