cat README.md
realVNC→SSH

ssh接続
```
ssh pi@raspberrypi.local
```
python仮想環境作成
```
python -m venv myenv
```

scpファイル転送
```
scp -r ../iot*  pi@raspberrypi.local:~/
```sudo apt-get install libsdl2-mixer-2.0-0