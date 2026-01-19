from fastapi import FastAPI
import uvicorn
import threading # ใช้ threading เพื่อรัน gRPC ควบคู่กับ HTTP
from grpc_server import serve_grpc, BTS_MEMBERS

# สร้าง instance ของ FastAPI

app = FastAPI()

# Endpoint หลัก ตรวจสอบสถานะ service
@app.get("/")
def root():
    return {"service": "A", "status": "ok"}

@app.get("/bts")
def get_all_bts():
    return BTS_MEMBERS

# ฟังก์ชันสำหรับเริ่ม gRPC ใน thread แยก
def start_grpc():
    serve_grpc()

if __name__ == "__main__":
    # แยก thread รัน gRPC server เพื่อไม่ให้ block main thread
    t = threading.Thread(target=start_grpc)
    t.start()
    uvicorn.run(app, host="0.0.0.0", port=8000)
