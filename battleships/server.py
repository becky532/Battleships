from concurrent import futures
import time
import grpc
import battleship_pb2_grpc
import battleship_pb2


class GreeterServicer(battleships_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        print("SayHello Request Made:")
        print(request)
        hello_reply = battleships_pb2.HelloReply()
        hello_reply.message = f"{request.greeting} {request.name}"

        return hello_reply


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    battleships_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()