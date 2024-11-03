#!/bin/bash

# 指定你想要處理的 Python 文件目錄，這裡假設是當前目錄
DIRECTORY="./game_api"

for file in $(find $DIRECTORY -type f -name "*.py"); do
  echo "Processing $file"
  
  # 執行 black 格式化
  black $file && isort $file
done

echo "Formatting complete!"
