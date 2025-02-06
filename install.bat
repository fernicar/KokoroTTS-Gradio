@echo off
echo Starting installation process...

echo.
echo Installing kokoro-onnx...
pip install -U kokoro-onnx
if errorlevel 1 (
    echo [ERROR] Failed to install kokoro-onnx.
    pause
    exit /b 1
)

echo.
echo Initializing uv with Python 3.12...
uv init -p 3.12
if errorlevel 1 (
    echo [ERROR] Failed to initialize uv with Python 3.12.
    pause
    exit /b 1
)

echo.
echo Adding kokoro-onnx and soundfile...
uv add kokoro-onnx soundfile gradio
if errorlevel 1 (
    echo [ERROR] Failed to add kokoro-onnx and soundfile.
    pause
    exit /b 1
)

echo.
echo Downloading kokoro-v1.0.onnx...
curl -L -o kokoro-v1.0.onnx https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
if errorlevel 1 (
    echo [ERROR] Failed to download kokoro-v1.0.onnx.
    pause
    exit /b 1
)

echo.
echo Downloading voices-v1.0.bin...
curl -L -o voices-v1.0.bin https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
if errorlevel 1 (
    echo [ERROR] Failed to download voices-v1.0.bin.
    pause
    exit /b 1
)

echo.
echo Installation completed successfully.
pause
