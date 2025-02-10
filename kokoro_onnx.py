"""
avoid installing kokoro-onnx
pip install sounddevice

wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
python examples/with_phonemes.py
"""
import sys
import os
import importlib.util

# Load the module from the specific file location
module_name = 'kokoro_onnx'
file_path = os.path.join('third_party/src/kokoro_onnx/__init__.py')

spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = module
spec.loader.exec_module(module)

import importlib.metadata

def mock_version(package_name):
    if package_name == 'kokoro-onnx':
        return 'local-dev'
    return importlib.metadata.version(package_name)
# Replace the version function in the module with the mock function
module.importlib.metadata.version = mock_version

# Now you can import from kokoro_onnx locally without installing it
Kokoro = getattr(module, 'Kokoro') # equivalent for `from kokoro_onnx import Kokoro`

from third_party.src.kokoro_onnx.tokenizer import Tokenizer
from third_party.src.kokoro_onnx.config import KoKoroConfig, MAX_PHONEME_LENGTH, VOCAB, EspeakConfig
from third_party.src.kokoro_onnx.log import log

# Re-export the imported classes
__all__ = ['Kokoro', 'Tokenizer', 'KoKoroConfig', 'log', 'MAX_PHONEME_LENGTH', 'VOCAB', 'EspeakConfig']