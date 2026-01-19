import grpc
from concurrent import futures
import user_pb2
import user_pb2_grpc

# ข้อมูลจังหวัดและภูมิภาค (Mock Data)
PROVINCE_INFO = {
    "Goyang": "Gyeonggi-do",
    "Gwacheon": "Gyeonggi-do",
    "Daegu": "North Gyeongsang"
}

# Class สำหรับ gRPC (Service C)

class ProvinceServiceServicer(user_pb2_grpc.ProvinceServiceServicer):

    # ฟังก์ชันสำหรับให้บริการข้อมูล Province
    def GetProvince(self, request, context):
        region = PROVINCE_INFO.get(request.province, "Unknown")
        return user_pb2.ProvinceReply(region=region)

# ฟังก์ชันรัน Server gRPC
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    user_pb2_grpc.add_ProvinceServiceServicer_to_server(
        ProvinceServiceServicer(), server
    )
    server.add_insecure_port("[::]:8002")
    server.start()
    print("Service C running on port 8002")
    server.wait_for_termination()
