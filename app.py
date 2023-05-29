from flask import Flask, render_template, request
import speedtest

app = Flask(__name__)
s = speedtest.Speedtest()

@app.route("/", methods=["GET"])
def home():
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    
    res = s.results.dict()
    download = round(res["download"] / 1000000, 2)
    upload = round(res["upload"] / 1000000, 2)
    ping = round(res["ping"])
    client = res["client"]["isp"]
    country = res["client"]["country"]
    print(
        "-->Download Speed: {} Mb/s\n-->Upload Speed: {} Mb/s\n-->Ping: {}\n-->ISP: {}, {}".format(
            download, upload, ping, client, country
        )
    )
    result = {
        "download_speed": download,
        "upload_speed": upload,
        "ping": ping,
    }

    return result

if __name__ == "__main__":
    app.run()
