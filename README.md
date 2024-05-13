# Video to SRT Converter

## Overview

This Python script extracts audio from video files and uses Google's speech recognition API to transcribe the audio to text. The transcribed text is then formatted into an SRT file, with each subtitle chunk representing a 3-second interval of speech.

## Note

To get more accurate results change the voice recognition model 

## Prerequisites

- Python 3.x
- `moviepy` library
- `SpeechRecognition` library
- `google-api-python-client` (for Google Speech Recognition API)
- An internet connection for the Speech Recognition API

## Installation

1. **Python Installation:**
   Ensure that Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Library Installation:**
   Install the required Python libraries using pip:

   ```bash
   pip install moviepy SpeechRecognition google-api-python-client
   ```

## Usage

To use this script, you need to have a video file in MP4 format. Run the script from the command line by specifying the path to the video file:

```bash
python video_to_srt.py <path_to_video_file>
```

### Example

```bash
python video_to_srt.py example_video.mp4
```

This command will process the specified video file and generate an SRT file in the same directory with the same filename as the video.

## Features

- **Audio Extraction:** Extracts audio from video files.
- **Speech Recognition:** Utilizes Google's speech recognition service to transcribe audio.
- **SRT Formatting:** Converts transcriptions into the SRT file format with accurate timing.

## Limitations

- The accuracy of the transcription may vary based on the quality of the audio in the video file.
- The script requires an active internet connection for the speech recognition service.

## Cleaning Up

The script automatically removes the temporary WAV file created during the conversion process.

## Troubleshooting

- **Audio Extraction Errors:** Make sure the video file is not corrupted and is in a supported format.
- **Speech Recognition Errors:** Check your internet connection and ensure that the Google API is not down.

## Contributing

Feel free to fork the repository and submit pull requests. You can also send us feedback or feature requests by opening an issue in the repository.

## License

This script is released under the MIT License.
