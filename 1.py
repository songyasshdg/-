# import requests
# # from requests_toolbelt import MultipartEncoder
#
#
# class SendMsg():
#     def __init__(self, app_id, app_secret, web_hook_url):
#         self.app_id = app_id  # 发送图片时需要
#         self.app_secret = app_secret  # 发送图片时需要
#         self.web_hook_url = web_hook_url  # 机器人web_hook地址
#
#     # 获取token为上传图片时使用
#     def get_tenant_access_token(self):
#         url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
#         body = {
#             "app_id": self.app_id,
#             "app_secret": self.app_secret
#         }
#         r = requests.request(method='post', url=url, json=body)
#         print(r.json())
#         return r.json()['tenant_access_token']
#
#     # 上传图片生成image id
#     def uploadImage(self, image_rb):
#         tenant_access_token = self.get_tenant_access_token()
#         url = "https://open.feishu.cn/open-apis/im/v1/images"
#         form = {'image_type': 'message',
#                 'image': image_rb}  # image_rb:是以rb格式读的图片内容，也可以是ui自动截的图，直接传过来
#         multi_form = MultipartEncoder(form)
#         headers = {'Authorization': 'Bearer {}'.format(tenant_access_token), 'Content-Type': multi_form.content_type}
#         response = requests.request("POST", url, headers=headers, data=multi_form)
#         # print(response.headers['X-Tt-Logid'])  # for debug or oncall
#         print(response.json())  # Print Response
#         return response.json()['data']['image_key']
#
#     def send_post(self, title, content):
#         """
#         title: 发送消息的标题
#         content: 使用富文本格式:https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/im-v1/message/create_json
#         """
#         body = {
#             "msg_type": "post",
#             "content": {
#                 "post": {
#                     "zh_cn": {
#                         "title": title,
#                         "content": content
#                     }
#                 }
#             }
#         }
#         r = requests.request(method='post', url=self.web_hook_url, json=body)
#         print(r.json())
# for letter in 'Python':
#    if letter == '':
#       continue
#    print('当前字母 :%s' %letter)
# row = 1
# while row <= 9:
#     col = 1
#     while col <= row:
#         print('%d * %d = %d\t' % (row, col, col * row), end='')
#         col += 1
#     print('')
#     row += 1
import pytest
import pytest_check as check


def test_example():
    a = 1
    b = 2
    c = [2, 4, 6]
    check.greater(a, b)
    check.less_equal(b, a)
    check.is_in(a, c, "111")
    check.is_not_in(b, c, "222")


if __name__ == "__main__":
    pytest.main()
