# python环境搭配
1. 安装 uv（管理python版本）: curl -LsSf https://astral.sh/uv/install.sh | sh
2. 安装python版本：uv python install 3.12;  查看版本：uv python list
3. 验证：python --version

# 工作流
1. `uv init`
1. 创建当前项目的虚拟环境，指定python版本，类似 node_modules (只用一次);  
```zsh
# 不要开代理
uv venv --python 3.12 (如果全局没有安装 3.12  这一步它会自动帮你下载 Python 3.12，不用你操心)
```
2. 激活环境 (每次开发前)：`source .venv/bin/activate`
3. 退出环境：`deactivate`
3. 安装依赖: `uv add langchain-community pypdf` (此时包会装在这个 venv 文件夹里，不污染全局)
4. 执行python文件: `uv run [your python file path]`