from util.aip_project.aip import AipSpeech
from util.aip_project.auto_audio import Monitor

class My_aip:
    def __init__(self):
        """ 你的 APPID AK SK """
        self.APP_ID = '11325283'
        self.API_KEY = '73Wn9EWhcnxYCC3xwcLkBGrg'
        self.SECRET_KEY = 'ek8hWAp9H9eGO5kTYLDQq2v4xtKz2eAf'

    def __call__(self, L_type): #1536为中文 1637为粤语
        client = AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)
        filename = Monitor()
        type_num = {'中文':1536,'粤语':1637,'英语':1737,'四川话':1837}
        num = type_num.get(L_type)
        if num == None:
            raise '语言类型错误'

        # 识别录音文件
        s = client.asr(self.get_file_content(filename), 'pcm', 16000, {
            'dev_pid': num,
        })
        return s

    # 读取文件
    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

def startaip():
    a = My_aip()
    return a('中文')['result'][0]

if __name__ == '__main__':
    startaip()