import pytest
from Api.Common.my_Base import TestCom
from Api.Common.my_Excel import FileTools


class TestArt(TestCom):
    # 参数化数据
    file_data = [("上传jpg格式的图片.jpg", "../data/picture.jpg", "image/jpeg", 200, "OK"),
                 ("上传png格式的图片.png", "../data/icon.png", "image/png", 200, "OK"),
                 ("上传txt格式的文档.txt", "../data/新建文本文档.txt", "text/plain", 200, "OK"),
                 ("上传json格式的文件.json", "../data/art_data.json", "application/json", 200, "OK"),
                 ("上传yaml格式的文件.yaml", "../data/art_data.yaml", "application/octet-stream", 200, "OK"),
                 ("上传cer格式的证书.cer", "../data/Root.cer", "application/x-x509-ca-cert", 200, "OK"),
                 ("上传exe格式的程序.exe", "../data/geek.exe", "application/x-msdownload", 200, "OK"),
                 ("上传xlsx格式的文档.xlsx", "../data/art_data.xlsx",
                  "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", 200, "OK")]

    @pytest.mark.parametrize("filename,filepath,filetype,status_code,msg", file_data)
    def test_art(self, filename, filepath, filetype, status_code, msg):
        res_url = self.base_url + "/api/admin/attachments/upload"
        file_data = FileTools().upload_file(filename, filepath, filetype)  # 调用封装的文件解析函数
        header = {"Admin-Authorization": self.token}
        r_art = self.request(method="post", url=res_url, headers=header, files=file_data)
        assert r_art.json()["message"] == msg
        assert r_art.status_code == status_code


if __name__ == '__main__':
    pytest.main(["-sv", "test_art.py"])
