import grpc
from concurrent import futures
import random
import time
import quote_pb2
import quote_pb2_grpc

QUOTES = {
    "motivational": [
        ("The best way to get started is to quit talking and begin doing.", "Walt Disney"),
        ("Don't let yesterday take up too much of today.", "Will Rogers"),
        ("It's not whether you get knocked down, it's whether you get up.", "Vince Lombardi")
    ],
    "life": [
        ("Life is what happens when you're busy making other plans.", "John Lennon"),
        ("Get busy living or get busy dying.", "Stephen King")
    ],
    "funny": [
        ("I am so clever that sometimes I don't understand a single word of what I am saying.", "Oscar Wilde"),
        ("I used to think I was indecisive, but now I'm not so sure.", "Unknown")
    ]
}

class QuoteServiceServicer(quote_pb2_grpc.QuoteServiceServicer):
    def GetQuote(self, request, context):
        category = request.category.lower()
        if category not in QUOTES:
            category = "motivational" 
        quote, author = random.choice(QUOTES[category])
        print(f"Sent quote from category '{category}': {quote} — {author}")
        return quote_pb2.QuoteResponse(quote=quote, author=author)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    quote_pb2_grpc.add_QuoteServiceServicer_to_server(QuoteServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC Quote Server running on port 50051...")
    try:
        while True:
            time.sleep(60)
            # None
    except KeyboardInterrupt:
        print("Server stopped.")
        server.stop(0)

if __name__ == '__main__':
    serve()