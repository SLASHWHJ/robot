# coding=utf-8
import turing
import baiduApi


if __name__ == "__main__":
    api_id = "9241847"
    api_key = "wxNGGTpSQTKYjROe5gpgBKDO"
    api_secert = "f4a44a0f4c5d12173c34e5b258ef1f98"
    bdr = baiduApi.BaiduRest(api_id, api_key, api_secert)
    while True:
        input("按下回车开始说话，自动停止")
        print('开始录音')
        bdr.recorder("output.wav")
        print("结束")
        ask = bdr.getText('output.wav')
        print('你：', ask)
        robot = turing.Turing()
        ans = robot.anser(ask)
        print('机器人：', ans)
        bdr.getVoice(ans, "output.mp3")
        bdr.speakMac("output.mp3")
