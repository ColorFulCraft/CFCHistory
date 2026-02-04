# 创建必要目录
mkdir -p stats bin

echo "开始编译 MCPing.java..."

# 编译Java文件
javac -d bin src/MCPing.java

if [ $? -ne 0 ]; then
    echo "编译失败！"
    exit 1
fi

echo "编译成功！"
echo "正在ping服务器 mc.cfcmc.cc:25565..."

# 运行程序
java -cp bin MCPing stats/server.json

if [ $? -ne 0 ]; then
    echo "运行失败！"
    exit 1
fi

echo "数据已保存到 stats/server.json"

# 显示结果
echo -e "\n📊 服务器状态："
cat stats/server.json | python3 -m json.tool || cat stats/server.json
