import grpc
import helloworld_pb2
import helloworld_pb2_grpc

def run():
    # Connect to server
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        name = input("Enter your name: ")
        response = stub.SayHello(helloworld_pb2.HelloRequest(name=name))
    print("Server replied:", response.message)

if __name__ == '__main__':
    run()
