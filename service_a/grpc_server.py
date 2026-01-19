import grpc
from concurrent import futures
import user_pb2
import user_pb2_grpc


# ข้อมูล BTS (ข้อมูลจำลอง)
# เก็บข้อมูลเมมเบอร์ BTS โดยใช้ ID เป็น key
BTS_MEMBERS = {
    1: {
        "name": "RM",
        "birthday": "1994-09-12",
        "province": "Goyang"
    },
    2: {
        "name": "Jin",
        "birthday": "1992-12-04",
        "province": "Gwacheon"
    },
    3: {
        "name": "SUGA",
        "birthday": "1993-03-09",
        "province": "Daegu"
    },
    4: {
        "name": "j-hope",
        "birthday": "1994-02-18",
        "province": "Gwangju"
    },
    5: {
        "name": "Jimin",
        "birthday": "1995-10-13",
        "province": "Busan"
    },
    6: {
        "name": "V",
        "birthday": "1995-12-30",
        "province": "Daegu"
    },
    7: {
        "name": "Jungkook",
        "birthday": "1997-09-01",
        "province": "Busan"
    }
}

# Class สำหรับ gRPC Service
# สืบทอดมาจาก BTSServiceServicer ที่ถูก generate มาจาก proto
class BTSServiceServicer(user_pb2_grpc.BTSServiceServicer):
    def GetMember(self, request, context):
        member = BTS_MEMBERS.get(request.id)

        if not member:
            return user_pb2.MemberReply()

        return user_pb2.MemberReply(
            name=member["name"],
            birthday=member["birthday"],
            province=member["province"]
        )

# ฟังก์ชันสำหรับรัน gRPC Server
def serve_grpc():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    user_pb2_grpc.add_BTSServiceServicer_to_server(
        BTSServiceServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print("gRPC Service A running on port 50051")
    server.wait_for_termination()
