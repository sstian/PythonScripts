"""
2019.11.24 21:21
制作模块
"""


from distutils.core import setup

setup(name="hm_message",
      version="1.0",
      description="it's send& receive",
      long_description="完整的发送接收模块",
      author="Sears Tian",
      author_email="st.tian@foxmail.com",
      url="www.snowflake.com",
      py_modules=["hm_message.send_message",
                  "hm_message.receive_message"])
