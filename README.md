
1. 連上需要 Driver (https://www.youtube.com/watch?v=JmDxP4O4Trk&feature=emb_logo)
2. 開 python 虛擬環境（esp-env）: ampy、esptool
3. 硬體安裝 micropython (https://medium.com/@pyliaorachel/用-python-玩硬體-micropython-簡介與實作-6fb9a799699b)
4. 更改 config.py wifi 密碼 / mqtt 資料
5. 上傳 config.py、其他檔案
```shell
ampy --port ${portname} put ${filename}
```