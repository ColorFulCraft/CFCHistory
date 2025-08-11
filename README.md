<div align="center">
  <img src="https://github.com/ColorFulCraft/CFCHistory/raw/main/pictures/icon.jpg" alt="ColorFulCraft Icon" width="150">
  
  # ✨ ColorFulCraft｜多彩工艺✨
  *默认文档*  |  *[维护文档](readme_admin.md)* | *[图片展示](pictures.md)*
</div>

---
> 最后更新时间：2025-08-11
> 文档维护：ColorFulCraft 管理组
---

## 1. 服务器简介
- **英文全称**：ColorFulCraft Network  
- **中文昵称**：多彩工艺  
- **成立日期**：2022-07-22  
- **服务器定位**：纯净生存 / 生电友好 / 建筑友好 / 养老社区  
- **当前版本**：Java Edition 1.21.X（推荐）
> 查看服务器团队及其及其现状
> [戳我](docs/about.md)
---

## 2. 怎么玩
| 项目 | 地址/端口 |
| --- | --- |
| 直连 IP | `mc.cfcmc.cc` |
| 备用移动 IP1 | `120.220.76.232:38888` |
| 官方 QQ 群 | 584937263 |
| 官网 | [戳我](https://blog.xhil.cn/)|

## 3. 服务器历史大事记
| 日期 | 事件 |
| --- | --- |
| 2022-07-25 | 服务器正式开服，采用纯生存玩法。 |
| 详细内容 | [请戳我](docs/Directory.md) |

---

## 📈 仓库 Star 历史
[![Star History Chart](https://api.star-history.com/svg?repos=ColorFulCraft/CFCHistory&type=Date)](https://star-history.com/#ColorFulCraft/CFCHistory&Date)

---

## 🗓️ 最近提交
![Alt](https://repobeats.axiom.co/api/embed/a30781bf5e8a72396572aed91c5588cc9e496ca0.svg "Repobeats analytics image")

<!-- 服务器实时状态监控 -->
<style>
        body_status {
            width: 100%;
            margin: 0 auto;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: white;
            min-height: 100vh;
        }
        .header {
            text-align: center;
            margin-bottom: 30px;
        }
        .header h1 {
            margin: 0;
            font-size: 2.2rem;
            background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }
        .header p {
            margin-top: 5px;
            color: rgba(255,255,255,0.7);
        }
        .cards-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-bottom: 30px;
        }
        .status-card {
            padding: 20px;
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 10px;
            background: rgba(255,255,255,0.05);
            backdrop-filter: blur(10px);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .status-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }
        .server-info {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
            padding-bottom: 15px;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }
        .server-logo {
            width: 50px;
            height: 50px;
            margin-right: 15px;
            border-radius: 8px;
            object-fit: cover;
        }
        .server-name {
            font-size: 1.3rem;
            font-weight: 600;
            margin: 0;
            color: white;
        }
        .server-description {
            font-size: 0.9rem;
            color: rgba(255,255,255,0.7);
            margin: 5px 0 0;
        }
        .status-item {
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
            padding: 8px 0;
        }
        .status-label {
            font-weight: 500;
            color: rgba(255,255,255,0.8);
        }
        .status-value {
            font-weight: 600;
            color: white;
        }
        .ping-good {
            color: #4caf50;
        }
        .ping-medium {
            color: #ff9800;
        }
        .ping-bad {
            color: #f44336;
        }
        .refresh-btn {
            display: block;
            margin: 0 auto;
            padding: 12px 24px;
            background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
            color: white;
            border: none;
            border-radius: 30px;
            cursor: pointer;
            font-weight: 600;
            font-size: 1rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(79, 172, 254, 0.3);
        }
        .refresh-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(79, 172, 254, 0.4);
        }
        .refresh-btn:active {
            transform: translateY(0);
        }
        .loading, .error {
            text-align: center;
            padding: 40px;
            grid-column: span 2;
        }
        .error {
            color: #ff6b6b;
        }
        @media (max-width: 768px) {
            .cards-container {
                grid-template-columns: 1fr;
            }
            .loading, .error {
                grid-column: span 1;
            }
        }
    </style>
<body_status>
    <div class="header">
        <h1>服务器状态监控</h1>
        <p>实时获取服务器运行状态</p>
    </div>
    
    <div class="cards-container" id="status-container">
        <div class="loading">
            <svg width="50" height="50" viewBox="0 0 50 50" xmlns="http://www.w3.org/2000/svg">
                <circle cx="25" cy="25" r="20" stroke="rgba(255,255,255,0.2)" stroke-width="5" fill="none"></circle>
                <circle cx="25" cy="25" r="20" stroke="#4facfe" stroke-width="5" stroke-linecap="round" fill="none" stroke-dasharray="125" stroke-dashoffset="100">
                    <animateTransform attributeName="transform" type="rotate" from="0 25 25" to="360 25 25" dur="1s" repeatCount="indefinite"></animateTransform>
                </circle>
            </svg>
            <p>正在获取服务器状态...</p>
        </div>
    </div>
    <br>
    <button id="refresh-btn" class="refresh-btn">刷新状态</button>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            fetchServerStatus();
            
            document.getElementById('refresh-btn').addEventListener('click', fetchServerStatus);
        });

        function fetchServerStatus() {
            const statusContainer = document.getElementById('status-container');
            statusContainer.innerHTML = `
                <div class="loading">
                    <svg width="50" height="50" viewBox="0 0 50 50" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="25" cy="25" r="20" stroke="rgba(255,255,255,0.2)" stroke-width="5" fill="none"></circle>
                        <circle cx="25" cy="25" r="20" stroke="#4facfe" stroke-width="5" stroke-linecap="round" fill="none" stroke-dasharray="125" stroke-dashoffset="100">
                            <animateTransform attributeName="transform" type="rotate" from="0 25 25" to="360 25 25" dur="1s" repeatCount="indefinite"></animateTransform>
                        </circle>
                    </svg>
                    <p>正在获取服务器状态...</p>
                </div>
            `;
            
            // Fetch both servers' data
            Promise.all([
                fetch('https://list.mczfw.cn/api/mc.cfcmc.cc'),
                fetch('https://list.mczfw.cn/api/mm.rainplay.cn:20478')
            ])
            .then(responses => Promise.all(responses.map(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })))
            .then(data => {
                displayServerStatus(data[0], data[1]);
            })
            .catch(error => {
                console.error('获取服务器状态出错:', error);
                statusContainer.innerHTML = `
                    <div class="error">
                        <h3>加载服务器状态失败</h3>
                        <p>请稍后再试</p>
                        <p><small>错误: ${error.message}</small></p>
                    </div>
                `;
            });
        }

        function getPingClass(ping) {
            if (ping < 100) return 'ping-good';
            if (ping < 200) return 'ping-medium';
            return 'ping-bad';
        }

        function displayServerStatus(mainServerData, testServerData) {
            const statusContainer = document.getElementById('status-container');
            
            statusContainer.innerHTML = `
                <div class="status-card">
                    <div class="server-info">
                        <img src="${mainServerData.logo}" alt="Server Logo" class="server-logo">
                        <div>
                            <h3 class="server-name" style="color:white">ColorFulCraft</h3>
                            <p class="server-description">主服务器</p>
                        </div>
                    </div>
                    
                    <div class="status-item">
                        <span class="status-label">在线玩家:</span>
                        <span class="status-value">${mainServerData.p} / ${mainServerData.mp}</span>
                    </div>
                    <div class="status-item">
                        <span class="status-label">服务器延迟:</span>
                        <span class="status-value ${getPingClass(mainServerData.ping)}">${mainServerData.ping} ms</span>
                    </div>
                    <div class="status-item">
                        <span class="status-label">服务器类型:</span>
                        <span class="status-value">${mainServerData.mod}</span>
                    </div>
                    <div class="status-item">
                        <span class="status-label">服务器地址:</span>
                        <span class="status-value">mc.cfcmc.cc</span>
                    </div>
                </div>
                
                <div class="status-card">
                    <div class="server-info">
                        <div style="width: 50px; height: 50px; margin-right: 15px; display: flex; align-items: center; justify-content: center; background: rgba(255, 152, 0, 0.1); border-radius: 8px;">
                            <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#ff9800" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                                <polyline points="14 2 14 8 20 8"></polyline>
                                <line x1="16" y1="13" x2="8" y2="13"></line>
                                <line x1="16" y1="17" x2="8" y2="17"></line>
                                <polyline points="10 9 9 9 8 9"></polyline>
                            </svg>
                        </div>
                        <div>
                            <h3 class="server-name" style="color:white">开发测试服</h3>
                            <p class="server-description">测试新功能</p>
                        </div>
                    </div>
                    
                    <div class="status-item">
                        <span class="status-label">在线玩家:</span>
                        <span class="status-value">${testServerData.p} / ${testServerData.mp}</span>
                    </div>
                    <div class="status-item">
                        <span class="status-label">服务器延迟:</span>
                        <span class="status-value ${getPingClass(testServerData.ping)}">${testServerData.ping} ms</span>
                    </div>
                    <div class="status-item">
                        <span class="status-label">服务器类型:</span>
                        <span class="status-value">${testServerData.mod}</span>
                    </div>
                    <div class="status-item">
                        <span class="status-label">服务器地址:</span>
                        <span class="status-value">mm.rainplay.cn:20478</span>
                    </div>
                </div>
            `;
        }
    </script>
</body_status>
