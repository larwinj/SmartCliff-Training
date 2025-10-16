import grpc
import quote_stream_pb2
import quote_stream_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = quote_stream_pb2_grpc.QuoteStreamerStub(channel)

    category = input("Enter quote category (motivational/life/funny): ").strip()
    print(f"Streaming quotes from category '{category}'...\n")

    for response in stub.StreamQuotes(quote_stream_pb2.QuoteRequest(category=category)):
        print(f"💬 {response.quote} — {response.author}")

if __name__ == "__main__":
    run()
