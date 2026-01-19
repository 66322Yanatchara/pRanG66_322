from fastapi import FastAPI
import uvicorn

# สร้าง FastAPI application
app = FastAPI()

# ข้อมูลจำลองสำหรับตอบกลับ HTTP request
PROVINCE_REGION = {
    "Goyang": "Gyeonggi-do",
    "Gwacheon": "Gyeonggi-do",
    "Daegu": "North Gyeongsang",
    "Gwangju": "South Jeolla",
    "Busan": "South Gyeongsang"
}

# Endpoint หลัก
@app.get("/")
def root():
    return {"service": "C", "status": "ok"}


# Endpoint ค้นหาภูมิภาคจากชื่อจังหวัด
@app.get("/region/{province}")
def get_region(province: str):
    return {
        "province": province,
        "region": PROVINCE_REGION.get(province, "Unknown")
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
