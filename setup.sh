cd yolov9
python3 -m pip install -U -r requirements.txt
mkdir weights
cd weights
curl -LO https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-c.pt
curl -LO https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-e.pt
curl -LO https://github.com/WongKinYiu/yolov9/releases/download/v0.1/gelan-c.pt
curl -LO https://github.com/WongKinYiu/yolov9/releases/download/v0.1/gelan-e.pt
cd ..
