# Minecraft 开服核心选择心得
## 一、主流核心概览
### 1. Vanilla（官方原版）

```适用场景：纯净生存服、小型好友服、技术测试服```

**优点**：
  - 官方出品，稳定性最高
  - 红石机制最纯正，无魔改
  - 更新最快，新特性第一时间体验
  
**缺点**：
  - 性能优化几乎为零
  - 不支持插件，管理全靠命令方块
  - 单核运行，无法利用多核CPU

> 个人心得： 除非是纯粹的原版红石服或者几个人联机玩，否则不建议用于正式开服。TPS掉起来非常感人。

### 2. Paper（最推荐）

```适用场景：90%的生存服、RPG服、小游戏服```

**优点**：
  - 性能优化极佳，同配置下比Spigot提升30-50%
  - 完全兼容Bukkit/Spigot插件生态
  - 异步区块加载，大幅减少卡顿
  - 活跃的社区和频繁的更新

**缺点**：
  - 对红石有轻微魔改（部分高频红石装置可能失效）
  - 某些极端生电装置需要调整

配置建议：
```yaml
settings:
  async-chunks: true  # 异步加载必开
  chunk-loading:
    player-max-concurrent-chunks-sends: 10
    
world-settings:
  default:
    optimize-explosions: true  # 爆炸优化
    mob-spawner-tick-rate: 2   # 刷怪笼优化
```
> 个人心得： 目前最均衡的选择。如果你不知道该选什么，选Paper准没错。生电服只要不用太极限的装置，Paper完全够用。

### 3. Purpur（Paper的增强版）

```适用场景：大型生存服、需要深度定制的服务器```

**优点**：
  - 继承Paper所有优化
  - 更多可配置项（生物上限、生成规则、游戏机制等）
  - 支持自定义生物行为、掉落物

**缺点**：
  - 配置项过多，新手容易调崩
  - 某些魔改可能影响原版体验

特色功能：
```yaml
world-settings:
  default:
    mobs:
      villager:
        brain-ticks: 2           # 村民AI优化
        use-brain-ticks-only-when-lagging: true
      enderman:
        allow-griefing: false    # 禁止末影人搬方块
```

> 个人心得： 适合有一定经验的服主。如果你需要微调游戏机制（比如关闭某些烦人的特性），Purpur比Paper更灵活。
### 4. Fabric（模组服首选）

```适用场景：模组服、生电服、技术向服务器```

**优点**：
  - 轻量级，加载速度极快
  - 对原版机制零魔改（生电服福音）
  - 模组生态丰富，性能优化模组多

**缺点**：
  - 插件生态薄弱（需要Sponge或Cardboard桥接）
  - 需要手动搭配优化模组
  - 版本更新后模组兼容性头疼
必装优化模组：
```
- Lithium（算法优化）
- Phosphor/Sodium（光影/渲染优化，服务端用Starlight）
- FerriteCore（内存优化）
- Chunky（预生成工具）
- Carpet（生电辅助，tick freeze等功能）
```
> 个人心得： 生电服首选。搭配Carpet mod可以实现tick冻结、假人挂机等功能。如果你主要玩原版+数据包，Fabric比Paper更适合。
###  5. Forge（老牌模组核心）

```适用场景：大型整合包、冒险模组服```

**优点**：
  - 模组生态最成熟，老牌模组多
  - 大型整合包兼容性最好

**缺点**：
  - 启动慢，吃内存
  - 性能优化不如Fabric
  - 版本更新滞后

> 个人心得： 如果你要开"龙之冒险"、"机械动力"这类大型整合包，Forge是唯一选择。纯技术向或轻量级模组服建议转Fabric。
### 6. Sponge

```适用场景：模组+插件混合服```

**优点**：
  - 唯一能在Forge/Fabric上运行Bukkit插件的方案
  - 有自己的插件生态

**缺点**：
  - 兼容性灾难，更新缓慢
  - 插件选择少，文档不全
  - 性能一般

> 个人心得： 除非必须同时用模组和Bukkit插件，否则不建议。可以用Cardboard（Fabric）或Mohist（Forge）作为替代。
### 7. Folia（新兴多线程核心）

```适用场景：超大型服务器（100+人）、生电分流服```

**优点**：
  - 真正的区域多线程，不再是单核游戏
  - 理论上支持数千玩家同时在线

**缺点**：
  - 插件兼容性极差（90%插件需要重写）
  - 仍处于实验阶段，bug较多
  - 红石机制有显著魔改

> 个人心得： 观望即可。除非你有技术团队维护定制插件，否则不建议生产环境使用。未来可期，但现在还不成熟。
## 二、选择决策树
flowchart TD
    Start[开什么类型的服？] --> A[纯净生存/小游戏/RLCraft类轻量整合]
    Start --> B[生电服/技术向/数据包服]
    Start --> C[大型模组整合包（ATM、Tekkit等）]
    Start --> D[模组+插件混合]
    Start --> E[超大型服务器（200+人）]
    
    A --> A1[推荐：Paper（通用）]
    A --> A2[推荐：Purpur（需要深度定制）]
    
    B --> B1[推荐：Fabric + Lithium + Carpet]
    
    C --> C1[推荐：Forge]
    
    D --> D1[Forge端方案]
    D --> D2[Fabric端方案]
    
    D1 --> D1a[Mohist/CatServer]
    D2 --> D2a[Cardboard（兼容性一般）]
    
    E --> E1[推荐：Folia（需定制插件）]
    E --> E2[推荐：多子服架构]
    
    E2 --> E2a[BungeeCord/Velocity]
## 三、性能优化通用建议
JVM参数（适用于所有核心）
```bash
java -Xms8G -Xmx8G -XX:+UseG1GC -XX:+ParallelRefProcEnabled \
     -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions \
     -XX:+DisableExplicitGC -XX:+AlwaysPreTouch \
     -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 \
     -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 \
     -XX:G1HeapWastePercent=5 -jar server.jar nogui
```
启动前必做:
- 预生成世界：用Chunky提前生成出生点及常用区域
- 限制视距：server.properties中view-distance=6-8足够
- 实体限制：spigot.yml中调整spawn-limits
- 定时重启：配合脚本每24小时自动重启释放内存
## 四、版本选择建议
| 版本 | 推荐度 | 说明 |
|------|------|------|
|1.20.4 |	⭐⭐⭐⭐⭐	| 当前最稳定，生态完善 |
|1.21+	| ⭐⭐⭐⭐	| 新内容多，但部分插件未更新 |
|1.12.2 |	⭐⭐⭐	| 老模组版本，经典但过时 |
|1.16.5 | ⭐⭐⭐	| 部分模组停留在该版本 |
|1.8.8	| ⭐⭐|	PVP服专用，过于老旧 |

## 五、总结

- 新手开服：Paper 1.20.4，插件丰富，社区支持多
- 生电玩家：Fabric + Carpet，机制纯正，功能强大
- 模组爱好者：Forge（大型包）或 Fabric（轻量/技术向）
- 追求极致性能：Purpur（调优后）或观望Folia发展

> 选核心没有绝对的好坏，只有适不适合你的服务器定位。建议先确定服务器类型，再选择对应生态最成熟的核心。
