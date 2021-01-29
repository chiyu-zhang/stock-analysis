# 股票分析
## 前言

### 什么是量化

　　我的理解，“量化”一词有两层释义。狭义上是指把思路变为计算机代码，包括通达信公式、python代码等；广义上是指在狭义释义的基础上，通过计算机自动完成整个选股和交易的过程。

### 为什么量化

　　然而量化又是投资过程中必须要完成的阶段。你有了一个选股思路，不管是长线投资的还是短线投机、不论是看基本面还是看技术面，总之你想把思路转化为选股策略，把思想转变为选股公式，这一过程本身就是量化。再之后，为了确定策略是否有效、收益率如何，又必然需要做策略回测来验证。最后，为了防止人性对交易过程的干扰，可以考虑使用自动化交易。

### 量化的优点

1. 选股。当把选股思路量化为代码后，计算机可以快速准确的帮你选出你想要的股票。
2. 下单速度。触发买入、卖出条件后，计算机可以在毫秒级别内完成下单操作。人为操作需要“打开交易软件-填股票代码-填金额-填数量-点下单”。这还没有考虑下单前，人们会来回犹豫所浪费的时间。

### 量化了就能赚钱？

　　python、量化过程、量化平台都只是工具，核心是交易策略，是交易思想。交易的目的是赚钱，不是学编程当程序员，也不是沉迷于玩数据中不可自拔，代码写的再高级精炼，不赚钱统统白搭。现在网上很多收费课程、量化平台，都是“卖铲子”的，核心的可以能稳定赚钱的量化策略，绝无一家提供。

　　就我个人而言，我不赞同完全把重心放在全自动量化交易上，而忽视基本面和技术面。对于短线来说，不确定性太多。比如，1分钟K线几乎处于“混沌”状态，根本没有逻辑和趋势可言。而周期越大的K线，越能体现出趋势和力度，突然反转的可能性越小。对于长线来说……还未听说过有把程序化交易用于长线的事例。

### 引文

> 交易这门手艺发展了这么多年，流派可谓五花八门，有看基本面搞价值投资的，有看K线搞技术指标的，有学江恩，缠论数波浪画中枢的，有分析资金面的，分析市场情绪的，有结合原始数据做日内波段的，有恨不得把服务器架在交易所对面做高频的，有搞一箱子GPU做automl，深度学习和强化学习的，有搞对冲的，搞多因子的，搞指数增强的，有搞MOM组合管理的，有搞一堆艰深晦涩的微分方程做衍生品套利的，当然，也有靠求神拜佛和拍脑门跺地板的。每种流派都有一些人奉为圭臬，还有一批人弃如敝履，而且时不时的还会冒出几个新的流派出来，令人眼花缭乱，有些摸不到头脑。
>
> 不知道哪个著名的人曾说过，如果你没有自己的思想，那你的脑子注定会成为其他人思想的跑马场。上面的这一堆思想和流派，既然能够出现并且流传下来，还能够有一批拥趸和死忠，也就表明它们确实是市场的本质或者圣杯在某个维度的一个映射或投影，但也仅仅只是一个投影而已。学习它们只是为了能够从更多的角度去窥视那个交易的圣杯，进而一点点的深化，完善和验证自己的交易思想和理论体系，最终通过一个承载着自己思想体系的工具来将思想兑换成实际的收益。在这个市面上出现的每一种付费编译的或者免费开源的交易软件都是固定的，即使在不断更新迭代也只是按照开发团队的思路来进行，包括QA在内，不可能有一个软件或者项目能够满足所有可能的交易思想，自然也就无法让你自由的学习，验证，归纳和吸收这些思想中的精华。因此，如果你没有定制化的开发交易工具的能力，而只能使用现有的工具的话，你的思想和自由意志就这样被别人的工具所局限住了。——[对QUANTAXIS的设计理念的思考和一些感悟](http://www.yutiansut.com:3000/topic/5f5ee1775778f910c1ba7a97)

## 项目介绍
- 使用python进行股票历史数据下载，策略回测，分析选股。除了策略以外，其他都可公开。
- 业余编程水平，需求导向。gitee主要作为云端git库使用。无任何指导服务。因此fork/issue都关了，对此项目感兴趣的朋友请自行克隆项目至本机娱乐。
- 力求选择最稳定可靠的数据获取方式。虽然网上有很多数据源平台，但都受制于“积分”、带宽、平台是否更新等，完全是把程序主动权交到了对方手里。因此大部分数据依靠本地通达信软件导出提供。感谢通达信，真是个好公司！不止数据容易提取，各种和谐加强版也很好用。
<img src="https://images.gitee.com/uploads/images/2021/0128/205808_1d56cbc4_5346376.png" alt="这个更新当日数据速度怎么受得了" title="QQ截图20210128205540.png" style="zoom:50%;" />
这个更新当日数据速度怎么受得了


## 软件架构
windows 10 20H2

通达信V7.52

python 3.8.5 (anaconda)

pytdx 1.72

ta-lib 0.4.19

其他缺什么库运行时报错自己pip安装一下

## 个人需求
- 两个核心需求：策略回测以及盘中选股。这又延伸出了数据采集、数据清洗、数据加工、行情监视等需求。
- 所有导入库、借鉴的代码都需开源，本地化，不云端。

