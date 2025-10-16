from flask import Flask, Response, send_file
import grpc
import video_pb2
import video_pb2_grpc

app = Flask(__name__)

@app.route('/')
def home():
    return send_file("client.html")

@app.route('/stream')
def stream_video():
    channel = grpc.insecure_channel('localhost:50051')
    stub = video_pb2_grpc.VideoStreamerStub(channel)
    response_stream = stub.StreamVideo(video_pb2.VideoRequest(filename="video.mp4"))
    
    def generate():
        for chunk in response_stream:
            yield chunk.content
    
    return Response(generate(), mimetype='video/mp4')

if __name__ == '__main__':
    print("Flask Web Server running on http://localhost:8080")
    app.run(port=8080, debug=True)
