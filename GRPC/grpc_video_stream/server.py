import grpc
from concurrent import futures
import video_pb2
import video_pb2_grpc
import time
import base64
import json
import os

CHUNK_SIZE = 1024 * 64  # 64KB per chunk
CHUNK_DUMP_FILE = "video_chunks.json"

class VideoStreamerServicer(video_pb2_grpc.VideoStreamerServicer):
    def StreamVideo(self, request, context):
        filename = request.filename
        print(f"Streaming video: {filename}")
        chunks_data = {}
        chunk_counter = 0

        try:
            with open(filename, "rb") as f:
                while True:
                    chunk = f.read(CHUNK_SIZE)
                    if not chunk:
                        break

                    chunk_counter += 1
                    chunk_key = f"chunk_{chunk_counter}"

                    chunks_data[chunk_key] = base64.b64encode(chunk).decode('utf-8')

                    yield video_pb2.VideoChunk(content=chunk)

                    print(f"sent {chunk_key} ({len(chunk)} bytes)")
                    time.sleep(0.01)

            with open(CHUNK_DUMP_FILE, "w") as jf:
                json.dump(chunks_data, jf, indent=2)
                print(f"Saved {chunk_counter} chunks to {CHUNK_DUMP_FILE}")

        except FileNotFoundError:
            print("File not found:", filename)
            return

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    video_pb2_grpc.add_VideoStreamerServicer_to_server(VideoStreamerServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC Video Server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    if os.path.exists(CHUNK_DUMP_FILE):
        os.remove(CHUNK_DUMP_FILE)
    serve()
