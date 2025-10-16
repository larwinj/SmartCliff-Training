import grpc
from concurrent import futures
import time
import random
import quote_stream_pb2
import quote_stream_pb2_grpc

QUOTES = {
    "motivational": [
        ("The best way to get started is to quit talking and begin doing.", "Walt Disney"),
        ("Don’t let yesterday take up too much of today.", "Will Rogers"),
        ("It’s not whether you get knocked down, it’s whether you get up.", "Vince Lombardi")
    ],
    "life": [
        ("Life is what happens when you’re busy making other plans.", "John Lennon"),
        ("Get busy living or get busy dying.", "Stephen King")
    ],
    "funny": [
        ("I am so clever that sometimes I don’t understand a single word of what I am saying.", "Oscar Wilde"),
        ("I used to think I was indecisive, but now I'm not so sure.", "Unknown")
    ]
}

class QuoteStreamerServicer(quote_stream_pb2_grpc.QuoteStreamerServicer):
    
    def StreamQuotes(self, request, context):
        category = request.category.lower()
        if category not in QUOTES:
            category = "motivational"
        for i in range(5): 
            quote, author = random.choice(QUOTES[category])
            print(f"📡 Streaming quote {i+1} ({category})")
            yield quote_stream_pb2.QuoteResponse(quote=quote, author=author)
            time.sleep(2) 

    def ChatQuotes(self, request_iterator, context):
        for req in request_iterator:
            category = req.category.lower()
            if category not in QUOTES:
                category = "motivational"
            for i in range(3):
                quote, author = random.choice(QUOTES[category])
                yield quote_stream_pb2.QuoteResponse(quote=quote, author=author)
                time.sleep(1)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    quote_stream_pb2_grpc.add_QuoteStreamerServicer_to_server(QuoteStreamerServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC Quote Stream Server running on port 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
