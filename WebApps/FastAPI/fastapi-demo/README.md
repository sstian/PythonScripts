
## 安装
```cmd
pip install fastapi

pip install "uvicorn[standard]"
```

## 运行
```cmd
> uvicorn main:app --reload

INFO:     Will watch for changes in these directories: ['D:\\Develop\\PythonScripts\\WebApps\\FastAPI\\fastapi-demo']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [21552] using WatchFiles
INFO:     Started server process [19268]
INFO:     Waiting for application startup.
INFO:     Application startup complete.   
```

## 交互式API文档
Swagger UI 自动生成：
http://127.0.0.1:8000/docs

ReDoc 自动生成：
http://127.0.0.1:8000/redoc

## 测试
使用 TestClient，先要安装 httpx
```cmd
pip install httpx
pip install pytest
```

```cmd
> pytest

D:\Develop\PythonScripts\WebApps\FastAPI\fastapi-demo>pytest
======================================================= test session starts ========================================================
platform win32 -- Python 3.13.5, pytest-8.4.1, pluggy-1.6.0
rootdir: D:\Develop\PythonScripts\WebApps\FastAPI\fastapi-demo
plugins: anyio-4.9.0
collected 1 item

test_main.py .                                                                                                                [100%]

======================================================== 1 passed in 2.20s =========================================================

```
