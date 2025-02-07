@echo off
echo Starting installation process...

if exist ".venv" (
    echo Virtual environment found. Activating...
    call .venv\Scripts\activate.bat
    python -m pip install -r requirements.txt
) else (
    echo [ERROR] Virtual environment not found. Please create one first.
    pause
    exit /b 1
)

echo.
echo Downloading kokoro-v1.0.onnx...
if not exist "model\kokoro-v1.0.onnx" (
    curl -L -o model/kokoro-v1.0.onnx https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
    if errorlevel 1 (
        echo [ERROR] Failed to download kokoro-v1.0.onnx.
        pause
        exit /b 1
    )
) else (
    echo kokoro-v1.0.onnx already exists.
)

echo.
echo Downloading voices-v1.0.bin...
if not exist "model\voices-v1.0.bin" (
    curl -L -o model/voices-v1.0.bin https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
    if errorlevel 1 (
        echo [ERROR] Failed to download voices-v1.0.bin.
        pause
        exit /b 1
    )
) else (
    echo voices-v1.0.bin already exists.
)

echo.
echo Installation completed successfully.
pause
