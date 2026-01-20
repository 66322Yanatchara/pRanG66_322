import grpc
import user_pb2
import user_pb2_grpc

# ฟังก์ชันเรียกข้อมูลจาก Service A ผ่าน gRPC
def get_bts_member(member_id: int):
    # เชื่อมต่อกัับ gRPC server ที่ localhost:50051 (Service A)
    # Note: In docker-compose, use the service name 'service_a' instead of localhost
    with grpc.insecure_channel('service_a:50051') as channel:
        stub = user_pb2_grpc.BTSServiceStub(channel)
        request = user_pb2.MemberRequest(id=member_id)
        response = stub.GetMember(request)

        return {
            "name": response.name,
            "birthday": response.birthday,
            "province": response.province
        }
