@echo off
REM When users clone this repository, git does not know which files to ignore from third_party submodule.
REM This batch script creates a sparse-checkout file in the third_party submodule, which tells Git which files to ignore.
REM Example: README.md files will not be downloaded when running git read-tree -mu HEAD in the third_party submodule.
REM Alternatively, you can ignore this recommendation and keep all unnecessary files in the third_party submodule.

REM Change directory to the parent directory of the third_party submodule, the root directory of the repository.
cd ..

REM Create a sparse-checkout file in the third_party submodule
echo !/* > .git\modules\third_party\info\sparse-checkout
REM The !/* pattern tells Git to exclude all files in the submodule

REM Add the src/kokoro_onnx directory to the sparse-checkout file
echo src/kokoro_onnx/ >> .git\modules\third_party\info\sparse-checkout
REM The src/kokoro_onnx/ pattern tells Git to include only the src/kokoro_onnx directory and its contents

REM Reminder: Run these commands in the console after executing this batch script
REM Apply the sparse-checkout settings to the third_party submodule
REM -m: Allows Git to merge the sparse-checkout settings with the existing index
REM -u: Updates the index with the sparse-checkout settings
REM HEAD: Specifies the commit to apply the sparse-checkout settings from
echo.
echo To apply the sparse-checkout settings, please run the following commands:
echo cd third_party
echo git read-tree -mu HEAD