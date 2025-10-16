import grpc
import quote_pb2
import quote_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = quote_pb2_grpc.QuoteServiceStub(channel)

    category = input("Enter quote category (motivational/life/funny): ").strip()
    response = stub.GetQuote(quote_pb2.QuoteRequest(category=category))
    
    print("\n💬 Quote of the Day 💬")
    print(f"\"{response.quote}\" — {response.author}")

if __name__ == '__main__':
    run()
