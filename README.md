# file-processing-transcription

The **file-processing-transcription** library is an extension of the [`file-processing`](https://github.com/hc-sc-ocdo-bdpd/file-processing/tree/main) library, designed to add transcription functionality to the core file processing capabilities. This library is built as a decorator, enabling it to wrap around relevant audio and video file types to transcribe spoken content to text using OpenAI's Whisper model.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features

- **Audio Transcription**: Converts spoken content in audio or video files to text.
- **Language Detection**: Automatically detects the language of transcribed content.
- **Decorator Pattern**: Seamlessly integrates with the `File` class from `file-processing` to add transcription functionality.

---

## Installation

To install the `file-processing-transcription` library and its dependencies, use the following command:

```bash
pip install -r requirements.txt
```

All required packages, including Whisper, are listed in the `requirements.txt` file.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**: Create your fork on GitHub.
2. **Create a Feature Branch**: Work on your feature in a separate branch.
3. **Write Tests**: Ensure any changes are covered by tests.
4. **Submit a Pull Request**: When ready, submit a PR for review.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

For questions or support, please contact:

- **Email**: [ocdo-bdpd@hc-sc.gc.ca](mailto:ocdo-bdpd@hc-sc.gc.ca)

--- 

*Enhance your file processing suite with transcription capabilities for audio and video content!*