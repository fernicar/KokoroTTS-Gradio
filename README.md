# Kokoro Project

This project is designed to process voice data using Python and various supporting files. It includes capabilities for voice data analysis and audio processing.

## Installation

1. Ensure you have Python installed (check the required Python version in the `.python-version` file).
2. Clone or download the repository to your local machine.
3. Run the `install.bat` file to set up any required dependencies and environment configurations.
4. Verify that all the necessary files are present, including:
   - Python scripts: `kokoro-Gradio.py`, `hello.py`
   - Model file: `kokoro-v1.0.onnx`
   - Voice configuration: `voices-v1.0.bin` and `voice-data.json`
   - Batch scripts: `install.bat`, `run-cli.bat`

## Running the Application

You can run the application in several ways:

- **CLI Mode:**  
  Execute `run-cli.bat` from the command line to start the application in command-line mode.

- **Gradio UI Mode:**  
  Run the `kokoro-Gradio.py` script to launch the application with a graphical user interface powered by Gradio.

- **Testing:**  
  For initial tests, you can run `hello.py` to check that the basic functionality is working.

## User Functions

- **Voice Processing and Analysis:**  
  The application utilizes the `kokoro-v1.0.onnx` model for voice processing and leverages the configuration in `voices-v1.0.bin` along with `voice-data.json` to manage voice data.

- **Audio Handling:**  
  Processed audio outputs are saved in the `output/` directory. Check this folder for generated audio files after processing.

- **General Workflow:**  
  Follow the installation steps, run the appropriate script or batch file, and interact with the UI or CLI as per your requirements.

## Troubleshooting

- Ensure that you have a compatible Python version installed.
- Make sure that `install.bat` has been executed successfully to set up the environment.
- Check the console output for any error messages if the app does not start as expected.
- Verify file integrity and paths if issues persist.

For further support or to report issues, please refer to the project documentation or contact the development team.
