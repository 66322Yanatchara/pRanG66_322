from fastapi import FastAPI
from grpc_client import get_bts_member

app = FastAPI()

@app.get("/bts/{member_id}")
def read_bts(member_id: int):
    # เรียกฟังก์ชัน get_bts_member เพื่อขอข้อมูลจาก Service A
    return get_bts_member(member_id)

if __name__ == "__main__":
    import uvicorn

app = FastAPI()

# Endpoint รับค่า member_id และไปเรียก gRPC client
