from removebg import RemoveBg
import base64

rmbg=RemoveBg('qVMCqDMp2NtncKXrqw3byKZr',False)
path=input("请输入文件地址：")
with open(path,"rb") as image_file:
  print("开始抠图")
  encoded_string = base64.b64encode(image_file.read())
  rmbg.remove_background_from_base64_img(encoded_string)
print("抠图完成")