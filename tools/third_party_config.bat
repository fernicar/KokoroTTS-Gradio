@echo off
REM Set sparse-checkout for the third_party submodule
cd ..

REM Create the sparse-checkout file
echo !/* > .git\modules\third_party\info\sparse-checkout
echo src/kokoro_onnx/ >> .git\modules\third_party\info\sparse-checkout

REM Reminder: Run these commands in the console after executing this batch script
echo.
echo To apply the sparse-checkout settings, please run the following commands:
echo cd third_party
echo git read-tree -mu HEAD
echo cd ..
