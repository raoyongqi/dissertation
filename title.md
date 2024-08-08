# 基于R的植物病害分析与预测模型构建


# Plant Disease Prediction Analysis Based on R
- [第一章 前言](#第一章-前言)
- [第二章 技术路线](#第二章-技术路线)
- [第三章 预处理](#第三章-预处理)
- [第四章 数据分析](#第四章-数据分析)
- [第五章 可视化](#第五章-可视化)


## 备忘录

做一个按钮，点击后可以隐藏没有选中的项
## 摘要
通过收集和预处理植物病害相关的数据，如气象条件、土壤性质等，项目应用R的各种分析工具进行数据清洗、特征提取和可视化。在建模阶段，使用R中的机器学习算法，如随机森林、xgboost，进行模型训练和评估。并使用R进行可视化。

## Abstract

Through collecting and preprocessing data related to plant diseases, including meteorological conditions, soil properties , the project will employ various analysis tools in R for data cleaning, feature extraction, and visualization. During the modeling phase, machine learning algorithms such as random forests and xgboost in R will be utilized for model training and evaluation，visualization.

## 第一章 前言

### 1.1研究背景


植物在生长过程中容易受到包括病原真菌和卵菌在内的多种病原体的侵害，进而引起形态异常、功能受损和生理受限，发生植物病害。病原真菌如锈菌、白粉菌以及卵菌中的疫霉菌和霜霉菌是导致植物病害的主要原因之一。锈病、白粉病和叶斑病等是植物病害的主要类型。锈病通常表现为叶片和茎秆上的小斑点，严重时会导致叶片脱落和植株枯死。白粉病则主要表现为植物表面覆盖一层白色粉状物，严重影响光合作用。叶斑病导致叶片上出现各种颜色的斑点，逐渐扩散并导致叶片枯萎。

病原物大体分为两类:一类病原物杀死寄主，然后从上面获得营养物质，即所谓的死体营养寄生物; 另一类是需要获得寄主以完成它们的生活史，即活体营养寄生物。
活体病原菌的一个短暂阶段代表了半活体营养病原菌。这类真菌在开始转向杀死寄主之前具有一个活体营养生长阶段。和半活体营养病原菌相比，专性活体病原菌需要活的寄主植物完成生活史。主要的植物病害包括锈病、白粉病、叶斑病和其他病害。

最新研究表明，气候变化和全球变暖导致温度的升高和部分地区降水格局的改变，正在加剧这些病害的发生和传播。温暖潮湿的环境有利于病原体的繁殖和扩散，导致病害在更大范围内更频繁地发生。例如，科学家发现全球变暖导致的温度升高和降水模式的改变，正促使一些病原真菌和卵菌向新的地理区域扩展，这些区域以前并不适合它们的生存和繁殖。气候变化还影响了植物的生理状态，使其更易受到病害侵染。实际上 , 温度和降水是影响叶片真菌病害的主要环境因子。 叶片真菌病害往往在高温、高湿的环境下较为严重。根据样点，使用机器学习、空间插值等方法预测全国病害有助于更好地认识到中国范围内病害的空间格局。

植物病害对全球农业生产力和粮食安全构成重大挑战。及时准确地预测这些病害对于有效的病害管理和减轻策略至关重要。近年来，数据收集技术的进步促使了多样化数据集的获取，涵盖了气象条件、土壤特性、植物物种信息以及植物病害严重程度。


### 1.2国内外研究现状


植物病理学家Sarah J. Gurr等人使用广义线性模型，研究发现真菌和昆虫每年向两极迁移7公里。相反，蠕虫（线虫）显示出向低纬度地区移动的趋势。对于其他分类群，如螨虫、细菌、双翅目、半翅目、膜翅目、等翅目、卵菌、原生动物、缨翅目和病毒，没有观察到显著的纬度变化趋势。气候变化可能对不同害虫分类群的地理分布产生了影响，其中一些群体正逐渐向两极迁移以适应新的环境条件。


Anne Ebeling等的研究通过对不同植物类型在不同年均温度和年均降水条件下受病害和无脊椎动物损害的分析，揭示了它们对环境变化的不同响应。研究发现，杂草在年均降水增加和年均温度升高的条件下，表现出显著的病害和无脊椎动物损害增加的趋势，尤其在高温高湿的环境中更为明显。相反，草类和豆科植物对这些因素的响应相对稳定，没有显示出明显的损害程度增加趋势。

Deepa S. Pureswaran等人探讨了气候变化对森林害虫的影响。他们综合了2013-2017年间的最新文献，包括之前的相关综述，深入讨论了气候变化如何影响昆虫的分布范围、数量、森林生态系统以及昆虫群落的影响。研究发现，气候变化可以促进害虫爆发或破坏食物链，从而减少害虫爆发的严重程度。通过广义线性模型和大尺度空间分析，研究揭示了气候变化对不同昆虫类群的地理分布和生态影响。

### 1.3 研究区概况

青藏高原是世界上最高和最大的高原，被誉为“世界屋脊”和“第三极”。它主要包括了藏高原及其周围的三大山脉：喜马拉雅山脉、横断山脉和中亚山脉。青藏高原的地形复杂多样，以高山、冰川、湖泊和河流为主要特征。

喜马拉雅山脉是世界上最高的山脉，拥有众多海拔超过8000米的高峰，其中包括世界最高峰珠穆朗玛峰。喜马拉雅山脉的存在极大地影响了青藏高原的气候和水文状况。横断山脉则位于青藏高原的东南部，其纵向延伸的山脉和峡谷构成了复杂的地形。中亚山脉包括天山山脉、帕米尔高原等，分布在青藏高原的西北部，连接了中亚地区。

青藏高原的水文资源丰富，许多大河的源头都位于此，如长江、黄河、雅鲁藏布江、印度河和恒河。这些河流不仅为高原地区提供了水源，还对下游地区的生态和经济产生了重要影响。高原上分布着众多湖泊，包括纳木错、玛旁雍错等，这些湖泊大多为高山冰川融水形成。

## 第二章 技术路线

### 2.1 技术路线概要

在前后端开发和集成学习的整合中，可以实现高效的数据处理、模型训练和预测结果展示。


在数据预处理阶段，后端服务器会对用户上传的数据进行清洗、格式化和特征提取。这些预处理步骤对于保证模型预测的准确性至关重要。完成预处理后，数据被传递给集成学习模型进行预测。集成学习模型可以由多种机器学习算法组成，如随机森林、梯度提升（如XGBoost）和神经网络等。

集成学习的核心在于结合多个弱学习器的预测结果以提高整体模型的性能。通常的方法包括Bagging、Boosting和Stacking。在Bagging方法中，多个模型并行训练，最终预测结果通过平均或投票的方式决定。Boosting则是通过逐步调整模型权重，关注前一阶段预测错误的数据，提高整体模型的准确性。Stacking是一种更为复杂的方法，通过训练一个元模型来组合多个初级模型的输出。

训练完成的模型可以保存到文件系统或数据库中，以便后续的快速加载和更新。每次用户发起预测请求时，后端服务器会加载最新的模型进行预测。预测结果经过处理后，通过API返回给前端，前端将结果以可视化的形式展示给用户。

通过这种技术路线，前后端和集成学习的整合不仅提高了数据处理和模型预测的效率，还提升了用户体验。前端提供了直观的交互界面，后端确保了数据处理和模型训练的可靠性，集成学习则增强了模型的预测性能。这种整合方法在实际应用中具有广泛的潜力，特别是在需要高精度预测的场景下。




### 2.2前端


#### 2.2.1 前端简介

前端方便了数据的展示和内容的拆分与维护。前端指的是浏览器的显示的内容，通过使用js、ts技术可以在网页上做出许多美观实用的图片，也可以在前端完成用户的交互工作，比如说下载图片、下载图片等。本文拟采用react完成直观的交互，比如说数据的上传、下载，结果的展示和下载等。

#### 2.2.2 React简介

React 是一个用于构建用户界面的 JavaScript 库。它由 Facebook 开发并开源。

- **组件化**：使用组件来构建用户界面。
- **虚拟 DOM**：提高性能。
- **单向数据流**：易于调试。


它主要专注于构建单页面应用程序（SPA），通过组件化的方式提高了代码的可复用性和可维护性。
React 的核心思想是组件化开发，将用户界面拆分为独立的组件，每个组件负责管理自己的状态和渲染逻辑。
React 的另一个显著特点是虚拟 DOM（Virtual DOM）。它通过在内存中维护一个虚拟 DOM 树来实现高效的 DOM 更新，通过比较前后两次虚拟 DOM 的差异，最小化了实际 DOM 操作的次数，从而提升了性能。
React 不仅可以用于 Web 应用程序的开发，还可以用于移动应用程序开发（React Native）以及静态网站的生成（Next.js）。由于其灵活性和高效性，React 在现代前端开发中得到了广泛应用，并成为了构建复杂用户界面的首选工具之一。

新建一个react项目
```bash
npx create-react-app my-react-app
```

### 2.3后端

#### 2.3.1 后端简介
后端指的是网页后台中配合前端完成数据处理，和保存到数据库的一系列内容，常用的后端有Java开发的spring 系列后端 ，js后端node.js，和python的fastapi。

#### 2.3.2 fastapi
在本文中，后端开发使用Python的FastAPI框架来构建RESTful API服务。FastAPI 是一个现代、快速（高性能）、基于标准 Python 类型提示的 Web 框架，用于构建 APIs，采用了 Python 3.6+ 版本。fastapi具有与 Node.js 和 Go 相媲美的高性能，因为它基于 Starlette 和 Pydantic 这两个高性能工具。在实际应用中，FastAPI 用于处理前端发送的数据请求，进行数据预处理并调用集成学习模型进行预测。例如，可以定义一个端点接收 JSON 格式的输入数据，进行数据预处理后调用模型进行预测，最后将预测结果返回前端。



```bash
pip install fastapi uvicorn
```

![alt text](pic/fastapi.png)
#### 2.3.3 mysql

FastAPI 与关系型数据库（如PostgreSQL）或非关系型数据库（如MongoDB）配合使用，可以有效管理和存储训练数据。训练数据可以存储在关系型数据库如PostgreSQL或非关系型数据库如MongoDB中，在本文中使用mysql将数据保存在数据库中。后端的另一个重要功能是管理模型的训练和更新。
MySQL 是一种开源的关系型数据库管理系统（RDBMS），它使用结构化查询语言（SQL）来访问、管理和操作数据库。MySQL 以其可靠性、可扩展性和易用性著称，已成为用于 Web 应用程序的最流行数据库之一，广泛应用于从小型初创公司到大型企业的各类组织。MySQL 支持多用户访问多个数据库，使其成为各种应用需求的多功能解决方案。
它基于客户端-服务器模型，服务器负责处理数据库管理任务，客户端与服务器接口以执行查询。MySQL 高度兼容多种操作系统，包括 Windows、Linux 和 macOS，并与许多编程语言无缝集成，如 PHP、Python 和 Java。
该数据库提供强大的功能，如符合 ACID 的事务、复制、集群和对大规模数据库的支持，确保数据完整性、高可用性和性能。MySQL 的架构旨在处理各种数据库任务，从简单的读密集型操作到复杂的写密集型事务。其性能优化工具和技术，如索引、缓存和查询优化，有助于高效的数据处理。
此外，MySQL 的活跃社区和广泛的文档提供了强有力的支持和持续的改进，使其成为在多种环境中进行数据库管理的可靠选择。






### 2.4 集成学习方法

### 2.4.1 随机森林

随机森林是一种集成学习方法，它通过构建多个决策树并结合其结果来进行分类或回归任务。该算法由Leo Breiman在2001年提出，旨在通过降低模型的方差来提高预测的准确性和鲁棒性。

- **方法与特点**：随机森林是一种集成学习方法，通过构建多个独立且不修剪的决策树并结合其结果进行分类或回归任务。该算法通过随机选取训练数据的子集和特征来生成每棵树，从而降低各棵树之间的相关性，提高模型的鲁棒性和准确性。


- **优势与性能**：随机森林具有良好的抗过拟合能力和较高的泛化性能，特别适用于处理高维数据和缺失值。它能够自动处理大规模数据集，并提供特征重要性评估，帮助理解和解释模型的决策过程。此外，随机森林易于并行化，能够有效利用现代计算资源。



随机森林通过随机选取训练数据的子集和特征来生成每棵树，使得各棵树之间的相关性降低，从而提升整体模型的性能。每棵决策树独立生长，且不会进行修剪，最终通过多数表决或平均值来汇总各个树的预测结果。随机森林具有良好的抗过拟合能力和较高的泛化性能，尤其在处理高维数据和缺失值时表现优异。其主要优势在于能够自动处理大规模数据集，并提供特征重要性评估，帮助理解和解释模型的决策过程。此外，随机森林易于并行化，能够有效利用现代计算资源，适用于各种应用领域，包括金融、医疗、生物信息学和图像处理等。



### 2.5 数据的采集方法

包括直接下载，调用api，和直接爬取数据。

### 2.6 数据的可视化方法
前端有许多优秀的库，比如说leaflet，echarts，可以用于展示图片。

## 第三章 预处理

### 3.1 预处理步骤概要

根据研究目标，本文需要进行特征选择、数据采集和数据整合。


数据整合，将数据自不同来源的数据整合到一起。数据整合的过程包括数据表的合并、连接或关联，以创建一个包含完整信息的数据集。



### 3.2 特征选择


#### 3.2.1 需求分析


我们拿到的数据集，如果是excel支持的格式，
往往包含很多列，但实际上用到的可能就只有几列。
因此，我们往往要选取数据集的子列作为我们分析的内容。
这一步主观性比较大，因为我们往往是根据主观意愿来选取我们要分析的内容。
如果需要选取数据集的列比较少，或者都位于excel表的一侧我们可以较为快速地选取。

#### 3.2.2 可复用选取特征的网页搭建


利用react可以轻松构建这样一个可复用的react项目。
先将数据上传，
根据需求选择子列，当选择的列较多时通过点击"全选/全不选"按钮进行全选或全不选，然后下载。

后端会将上传的文件保存在本地。
```
upload_path = file_manager.save_uploaded_file(file)
```

然后将文件的列名返回给前端

```
df = pd.read_excel(upload_path)
columns = [{'key': str(i), 'name': col, 'editable': True} for i, col in enumerate(df.columns)]

return {"columns": columns, "filename": os.path.splitext(file.filename)[0]}
```

下载时，后端会读取需要下载的文件,根据列名取出excel中相应的列，并返回前端。

```
selected_file = os.path.join(download_subdir, file_list[0])
df = pd.read_excel(selected_file)
selected_df = df[columns]

output_path = os.path.join(file_manager.upload_dir, f"selected_{filename}.xlsx")
selected_df.to_excel(output_path, index=False)

return FileResponse(output_path, filename=f"selected_{filename}.xlsx", media_type='application/octet-stream')
```
下载的文件将会保存在浏览器默认的保存路径下。
![alt text](pic/2f6eee87f07f43a74892d29c453584c.png)



### 3.3 收集数据



#### 3.3.2 收集全球植被分类图



全球草地概况是一个复杂而广泛的主题，涵盖了草地类型、分布、生态功能以及它们在不同国家和地区的重要性。草地是地球上重要的陆地生态系统之一，它们覆盖了地球表面的大约30%，仅次于森林和沙漠。草地生态系统包括热带草原、温带草原、寒带苔原等，它们在不同的气候条件下形成并支持着多样的生物多样性。

草地在生态系统中扮演着多种角色。首先，它们是重要的碳汇，能够吸收大气中的二氧化碳并将其储存在植被和土壤中。其次，草地是许多野生动植物的栖息地，为它们提供了食物和庇护所。此外，草地还有助于防止土壤侵蚀，通过根系固定土壤，减少水土流失。在农业方面，草地是畜牧业的基础，为牲畜提供食物来源。通常，草地在全球的分布受到气候、地形和人类活动等多种因素的影响。例如，在非洲的萨瓦纳地区、北美的大草原以及南美的潘帕斯草原都是草地生态系统的典型代表。

至于中国，它拥有世界上最大的草地面积之一，约占全球草地面积的10%左右。


中国的草地主要分布在西部和北部地区，中国的草地资源非常丰富，草地类型多样，这些地区包括主要分布在内蒙古草原、青藏高原草地、新疆草地、东北草地和黄土高原草地等区域。这些草地生态系统在地理上呈现出明显的纬度和海拔梯度。

内蒙古高原是中国最大的草地区域之一，这里的草地以温带草原为主，是重要的畜牧业基地。内蒙古的草地覆盖了广阔的平原和低山丘陵地带，为众多的牲畜提供了丰富的食物资源。内蒙古自治区是中国最大的草原分布区，涵盖了呼伦贝尔草原、锡林郭勒草原和阿拉善草原。呼伦贝尔草原以其平坦广袤的草地和优质的牧草著称，是优良的天然牧场。锡林郭勒草原以丰富的生物多样性和独特的自然景观闻名，而阿拉善草原则以其干旱和半干旱的生态环境为特色。

青藏高原则以其高海拔草地著称，这里的草地属于高山草甸类型，由于海拔高，气候寒冷，草地生长的植物种类相对较少，但它们对于维持高原生态系统的稳定和生物多样性具有重要作用。青藏高原位于中国西南部，草地主要集中在青海省、西藏自治区和四川省的部分地区。这里的草地包括高寒草甸和高寒草原，以高寒冷湿的气候和复杂的地形为特征，是许多珍稀野生动物的栖息地，如藏羚羊和野牦牛。

新疆地区则有干旱和半干旱的草地，这里的草地生态系统适应了干旱的环境条件，多为耐旱和耐盐碱的植物种类。新疆的草地在支持当地畜牧业和保护生态平衡方面发挥着关键作用。新疆维吾尔自治区的草地主要分布在天山山脉和阿尔泰山脉地区，包括天山草甸草原和阿尔泰山草原。这里的草地气候干旱，植被稀疏，但却是重要的畜牧业基地。

东北地区的草地主要集中在吉林省和黑龙江省的部分地区，如松嫩平原和三江平原，受季风气候影响，夏季湿润，适宜草原植物生长。

黄土高原位于中国西北部，草地主要分布在陕西省和甘肃省的部分地区，由于气候干旱，多为干旱草原和荒漠草原，植被稀疏，土壤贫瘠。


然而，草地生态环境也面临着过度放牧、气候变化和土地荒漠化等挑战，需要加强保护和可持续管理。
整体来看，中国的草地生态系统在地理分布上呈现出多样化的特点，从温带草原到高山草甸，再到干旱草原，它们不仅为畜牧业提供了基础，对水土保持、防风固沙和维护生物多样性具有重要作用，对于维持区域乃至全球的生态平衡具有不可替代的作用。同时，这些草地也是中国重要的自然景观和生态旅游资源，对于促进地方经济发展和生态旅游具有重要意义。

![alt text](pic/image.png)


![alt text](pic/china.png)


#### 3.3.2 批量下载worldClimate数据


```R
加载必要的包
library(geodata)
library(openxlsx)

# 设置工作目录
setwd("C:/Users/r/Desktop/r_climate/data")

# 读取 Excel 文件中的经纬度数据
data <- read.xlsx("lon_lat.xlsx", sheet = 1)
names(data) <- tolower(names(data))

# 检查是否包含 'lon' 和 'lat' 列
if(!all(c('lon', 'lat') %in% names(data))) {
  stop("Excel 文件需要包含 'lon' 和 'lat' 列")
}

# 定义要下载的气候变量
variables <- c("bio", "elev", "prec", "srad", "tavg", "tmax", "tmin", "vapr", "wind")

# 定义一个函数来下载和提取单个样点的数据
download_and_extract <- function(lon, lat, var, res = 10) {
  clim_data <- geodata::worldclim_global(var = var, res = res, path = ".")
  return(raster::extract(clim_data, matrix(c(lon, lat), ncol = 2)))
}

# 初始化结果数据框
result <- data

# 迭代每个气候变量，下载并提取数据
for (var in variables) {
  all_clim_values <- NULL
  
  for (i in 1:nrow(data)) {
    lon <- data$lon[i]
    lat <- data$lat[i]
    
    clim_values <- download_and_extract(lon, lat, var)
    
    if (is.null(all_clim_values)) {
      all_clim_values <- clim_values
    } else {
      all_clim_values <- rbind(all_clim_values, clim_values)
    }
  }
  
  # 给提取到的数据添加前缀
  colnames(all_clim_values) <- paste(var, colnames(all_clim_values), sep = "_")
  
  # 将提取到的数据与原始样点数据合并
  result <- cbind(result, all_clim_values)
}

# 保存结果到新的 Excel 文件
output_file_path <- "climate_data.xlsx"
write.xlsx(result, output_file_path, row.names = FALSE)

# 完成
cat("气候数据已成功保存到", output_file_path)
```
关于WorldClim的19种生物气候变量可参阅：
```

https://www.worldclim.org/data/bioclim.html.
```



图中的颜色表示特定气候变量的数值范围，从深紫色到黄色的渐变色条表示数值从低到高的变化。例如，太阳辐射图中，紫色区域表示较低的辐射值，而黄色区域表示较高的辐射值。不同时间段的太阳辐射数据图显示了全年不同月份的太阳辐射分布情况。类似地，平均气温图展示了不同月份的气温分布情况。

这种空间分布图对于理解气候模式和趋势非常有用。例如，通过观察太阳辐射的季节性变化，可以分析不同区域的太阳能潜力，进而影响能源政策的制定。同样，通过分析气温的空间分布，可以了解温度的季节性变化，帮助农业、生态和城市规划等领域进行相应调整。

根据WorldClim数据集的文献，这类气候数据通常通过全球气象站点的观测数据进行插值，生成高分辨率的气候图层。这些数据广泛用于生态和环境科学研究，如物种分布模型、气候变化影响评估等。高分辨率气候图层能够提供详细的区域气候信息，使得研究人员可以在较小的地理尺度上进行精细化分析，从而获得更精确的结果。

总体来看，这些气候变量的空间分布图不仅展示了不同时间点和气候变量的空间变化，还为进一步的气候研究提供了宝贵的数据支持。通过这些图，可以更直观地理解和分析气候变化对不同区域的影响，为相关领域的决策提供科学依据。
这张图展示了某一地理区域的多个气候变量的空间分布情况。图像中包含了2个不同的气候变量，每个变量分别在一个子图中呈现，通过观察图像，我们可以发现青藏高原的草地具有较高的海拔和较低的年最高温等。结合WorldClim数据集（可参见WorldClim官方网站），这些变量反映了不同的气候特征。通过颜色的渐变可以看出不同变量在不同区域的变化情况。这些数据有助于理解该区域的气候特征，并可用于气候研究、生态模型以及环境管理等领域



![alt text](pic/worldClim.png)


### 3.3.3 土壤数据处理


该文件讨论了协调世界土壤数据库 （HWSD） 的创建和目的。该数据库是 FAO（联合国粮食及农业组织）和 IIASA（国际应用系统分析研究所）以及其他合作伙伴（如 ISRIC – 世界土壤信息和欧洲土壤局网络 （ESBN） 的合作成果。

在全面更新全球农业生态区研究的背景下，联合国粮食及农业组织（FAO）和国际应用系统分析研究所（IIASA）认识到，迫切需要整合全球现有的区域和国家土壤信息更新，并将其与1971-1981年间编制的、但大部分已不再反映当前土壤资源实际状况的1:5,000,000比例尺FAO-UNESCO世界土壤图相结合。为此，他们与主要负责开发区域土壤和地形数据库（SOTER）的国际土壤参考资料和信息中心（ISRIC）以及近年来对欧洲和欧亚北部土壤信息进行重大更新的欧洲土壤局网络（ESBN）建立了合作伙伴关系。此外，通过与中国科学院土壤科学研究所的合作，将1:1,000,000比例尺的中国土壤图纳入其中，成为重要补充。

为了以统一的方式估算土壤属性，研究团队利用实际土壤剖面数据和土壤传递规则的开发，与ISRIC和ESBN合作，借鉴了WISE土壤剖面数据库以及Batjes等人（1997; 2002）和Van Ranst等人（1995）的早期工作。国际应用系统分析研究所（IIASA）负责确保数据的和谐化和在地理信息系统（GIS）中的输入，而所有合作伙伴则负责数据库的验证。

该产品的主要目的是为模型构建者提供实用工具，并为农业生态区划、粮食安全和气候变化影响等前瞻性研究服务。因此，选择了大约1公里（30弧秒×30弧秒）的分辨率。生成的栅格数据库由21,600行和43,200列组成，其中包含2.21亿个网格单元，覆盖了全球陆地。

在协调一致的全球土壤数据库（HWSD）中，识别出超过16,000个不同的土壤制图单元，这些单元与协调一致的属性数据相关联。标准化的结构允许将属性数据与GIS相结合，以显示或查询土壤单元的组成以及选定土壤参数的特征（如有机碳、pH值、蓄水能力、土壤深度、阳离子交换能力、粘土含量、总可交换养分、石灰和石膏含量、钠交换百分比、盐度、质地类别和粒度分布）。

然而，所提供信息的可靠性存在差异：仍使用世界土壤图的部分地区（如北美、澳大利亚、西非（不包括塞内加尔和冈比亚）和南亚）被认为可靠性较低，而大多数由SOTER数据库覆盖的地区（如南部和东部非洲、拉丁美洲和加勒比地区、中欧和东欧）被认为具有最高可靠性。

土壤质地是描述土壤中不同粒径矿物颗粒相对比例的土壤属性。根据颗粒大小，土壤颗粒被分为不同的组别，称为土壤分离物（粘土、粉砂和砂土）。这些分离物的粒径范围决定了土壤的质地类别，如砂土、粘土、壤土等，这些类别可以通过土壤质地三角形图来表示。土壤质地类别与特定的分离物比例范围相对应。例如，粗质地土壤含有较大比例的砂土，中等质地土壤主要由粉砂构成，而细质地土壤则以粘土为主。图中还提到了土壤质地三角形，这是一种图解工具，用于根据土壤分离物的比例确定土壤的质地类别。
不同土壤分类系统中非土壤单元和相位的统一编码系统。由于不同来源数据库中非土壤单元和相位的编码存在差异，因此需要一个统一的编码系统来整合这些信息。例如，沙丘和流沙在不同的分类系统中有不同的编码，但在统一数据库中被赋予了新的编码"ST"。同样，盐滩、岩石碎片、内陆水域、冰川和永久积雪、无数据、未勘测、城市、人为干扰、沼泽、鱼塘和岛屿等非土壤单元都有相应的新编码。这些编码包括但不限于：沙丘和流沙（ST）、盐滩（RK）、岩石碎片（WRs）、内陆水域（WR）、冰川和永久积雪（GG）、无数据（NI）、未勘测（NS）、城市（UR）、人为干扰（HD）、沼泽（MA）、鱼塘（FP）、岛屿（IS）等。某些土壤属性，这些属性是土壤单元定义固有的，并且对土壤的农业使用具有相关性，包括"vertic"、"gelic"和"petric"属性。其中，"petric"属性特指含有石灰石的土壤（petric Calcisols）和含石膏的土壤（petric Gypsisols），这些分类遵循的是FAO-90的土壤分类体系。


Harmonized World Soil Database

In the context of a complete update of the global agro-ecological zones study, FAO and IIASA 
recognized that there was an urgent need to combine existing regional and national updates of soil 
information worldwide and incorporate these with the information contained within the 1:5 000 000 
scale FAO-UNESCO Soil Map of the World (FAO, 1971-1981), which was in large parts no longer 
reflecting the actual state of the soil resources. In order to do this, partnerships were sought with the 
ISRIC – World Soil Information who had been largely responsible for the development of regional 
Soil and Terrain databases (Sombroek, 1984) and with the European Soil Bureau Network (ESBN) 
who had undertaken a major update of soil information for Europe and northern Eurasia in recent 
years (ESB, 2004). The incorporation of the 1:1,000,000 scale Soil Map of China (Shi et al., 2004) 
was an essential addition obtained through the cooperation with the Institute of Soil Science, Chinese 
Academy of Sciences. In order to estimate soil properties in a harmonized way, the use of actual soil 
profile data and the development of pedotransfer rules was undertaken in cooperation with ISRIC and 
ESBN drawing on the WISE soil profile database and earlier work of Batjes et al. (1997; 2002) and 
Van Ranst et al.(1995).. 
The harmonization and data entry in a GIS was assured at the International Institute for Applied 
System Analysis (IIASA) and verification of the database was undertaken by all partners. As the 
product has as its main aim to be of practical use to modelers and is to serve perspective studies in 
agro-ecological zoning, food security and climate change impacts (among others) a resolution of about 
1 km (30 arc seconds by 30 arc seconds) was selected1
. The resulting raster database consists of 21600 
rows and 43200 columns, of which 221 million grid cells cover the globe’s land territory. 
Over 16000 different soil mapping units are recognized in the Harmonized World Soil Database 
(HWSD). which are linked to harmonized attribute data. Use of a standardized structure allows linkage 
of the attribute data with GIS to display or query the composition in terms of soil units and the 
characterization of selected soil parameters (organic Carbon, pH, water storage capacity, soil depth, 
cation exchange capacity of the soil and the clay fraction, total exchangeable nutrients, lime and 
gypsum contents, sodium exchange percentage, salinity, textural class and granulometry). 
Reliability of the information presented here is variable: the parts of the database that still make use of 
the Soil Map of the World such as North America, Australia, West Africa (excluding Senegal and 
Gambia) and South Asia are considered less reliable, while most of the areas covered by SOTER 
databases are considered to have the highest reliability (Southern and Eastern Africa, Latin America 
and the Caribbean, Central and Eastern Europe). 
Further expansion and update of the HWSD is foreseen for the near future, notably with the excellent 
databases held in the USA: Natural Resources Conservation Service US General Soil Map 
(STATSGO) http://www.ncgc.nrcs.usda.gov/products/datasets/statsgo, Canada: Agriculture and AgriFood Canada: The National Soil Database (NSDB) http://sis.agr.gc.ca/cansis/nsdb and Australia: 
CSIRO, aclep, natural Heritage Trust and National Land and Water Resources Audit: ASRIS 
http://www.asris.csiro.au/index_other.html, and with the recently released SOTER database for 
Central Africa (FAO/ISRIC/University Gent, 2007). 
The database content is discussed in Chapter 2 and the harmonization process in Chapter 3. Annex 1 
gives a historical overview of the development of the Soil Map of the World, the Soil and Terrain 
Databases (SOTER), the Geographic Database for Europe, the Soil Map of China, and ISRIC-WISE 
database, while Annex 2 to 4 give detailed instructions on how to use the GIS software and the viewer. 
 
1 Note: Original data were mapped respectively at scales of 1:5,000,000 for the Soil Map of the World and 
between 1:1,000,000 and 1:5,000,000 for the various SOTER regional studies and 1:1,000,000 the European Soil 
Map and the Soil Map of China. The pixel size has been selected to ensure compatibility with important 
inventories such as the slope and aspect database (based on 90 m resolution SRTM data) and GLC 2000/2005 
land cover data available at 30 arc seconds. The HWSD by necessity presents therefore multiple grid cells with 
identical attributes occurring in individual soil mapping units as provided on the original vector map
MU_GLOBAL - the harmonized soil mapping unit identifier of HWSD providing the link to 
the GIS layer; 
− MU_SOURCE1 and MU_SOURCE2- the mapping unit identifiers in the source database; 
− SEQ – the sequence of the soil unit in the soil mapping unit composition; 
− SHARE - % of the soil unit/topsoil texture combination in the soil mapping unit; and the 
− Soil unit symbol using the FAO-74 classification system or the FAO-90 classification system 
(SU_SYM74 resp. SU_SYM90) or FAO-85 interim system (SU_SYM85).
![alt text](pic/1722382718420.jpg)
![alt text](pic/1722382670272.jpg)
![alt text](pic/761ad8d49e0b335943e63818403e0f5.png)
![alt text](pic/image.png)
### 3.3.4 使用箱线图观察数据分布

箱线图的中间线通常表示中位数，而箱子的上下边缘则分别表示第一四分位数和第三四分位数，箱子外的“须”则可以表示数据的最小值和最大值，或者表示异常值，这些信息有助于我们更深入地理解数据的分布情况。

前端结合echarts可以展示一系列代表各种植物病害严重程度指标的箱线图。这些指标包括群落病害严重度、群落病害严重度直接效应和群落死体病害严重度等。这些图表植物病害严重程度的分布和变异性。


后端代码参考
```python

@app.get("/fetch_label_box")
def fetch_data(db: Session = Depends(get_db)):
    try:
        UploadedLabel = Base.classes.uploaded_label
        if not UploadedLabel:
            raise HTTPException(status_code=404, detail="No mysql upload_label table")
        data = db.query(UploadedLabel).all()
        if not data:
            raise HTTPException(status_code=404, detail="No data found")
        result = [item.__dict__ for item in data]
        for item in result:
            item.pop('_sa_instance_state', None)
        return {"columns": list(result[0].keys()), "rows": result}
    finally:
        db.close()


```


![alt text](pic/boxplot.png)
world climate数据集中包含了多种气象要素，如温度（tmax表示最高温度，tmin表示solar radiation，tavg表示平均气温）、生物量（bio）、太阳辐射（srad）、风速（wind）、降水量（prec）和相对湿度（vapr）等。每个变量都有多个不同的观测值，例如tmax_wc2.1_10m_tmax_01可能表示在特定高度（10m）上测量的最高温度数据。


![alt text](pic/image2.png)



## 第四章 数据分析


### 4.1 随机森林变量重要性图输出与分析
为了完成完成随机森林的构建，可以使用python的scikit-learn库来实现。
群落病害相关性分析：重要变量的详细结果
在分析群落活体病害严重度（ComminityDisease_Biotroph）、群落死体病害严重度（ComminityDisease_Necrotroph）、群落病害严重度间接效应（PL_indirect）和群落病害严重度直接效应（PL_direct）时，随机森林模型的重要性图揭示了一些关键变量。
从图中可以看出，四个分析模型中，一些变量在病害严重度的影响上具有显著的权重。在图表中，红色柱子表示选择的变量，这些变量主要源于WorldClim数据。具体来看：
ComminityDisease_Biotroph：在左上图中，'lon'（经度）和 'srad'（solar radiation）是两个重要变量，尤其是'lon'，其对活体病害严重度的重要性权重超过0.2，显示出明显的影响。
ComminityDisease_Necrotroph（群落死体病害严重度）：右上图同样显示，'lon'（经度）和 'srad'（solar radiation）占据了显著的权重。特别是 'srad'，其权重超过0.3，表明在死体病害严重度中温度因素起着重要作用。
PL_direct（群落病害严重度直接效应）：在左下图中，经度和solar radiation再次显示出高权重，'lon'的重要性接近0.2，而'srad'也表现出显著影响。PL_indirect（群落病害严重度间接效应）：右下图中，经度和solar radiation继续占据主要位置，显示出相似的趋势。经度和'srad'的权重分别约为0.15和0.1。
总的来看，这些图表展示了经度（lon）和solar radiation（srad）在群落病害严重度的不同方面的重要性。研究表明，地理位置和气候条件（尤其是温度）对病害发生和发展有着关键影响。具体的WorldClim数据变量选择显示了气候数据在预测病害严重度中的关键作用，为进一步的生态学和病理学研究提供了重要参考。
```python
   
def train_and_save_models():

    feature_df = pd.read_sql("SELECT * FROM uploaded_feature", engine)
    feature_df = feature_df.drop(columns=["id"])  # 移除id列
    label_df = pd.read_sql("SELECT * FROM uploaded_label", engine)
    label_df = label_df.drop(columns=["id"])  # 移除id列

    for label_column in label_df.columns:
        X = feature_df
        y = label_df[label_column]

        model = RandomForestRegressor()
        model.fit(X, y)

        joblib.dump(model, f"{MODEL_DIR}/model_{label_column}.joblib")

def load_models():
    models = {}
    for file in os.listdir(MODEL_DIR):
        if file.endswith(".joblib"):
            label = file.replace("model_", "").replace(".joblib", "")
            models[label] = joblib.load(f"{MODEL_DIR}/{file}")
    return models

@app.get("/feature_importances")
async def feature_importances() -> Dict[str, List]:
    try:
        if not os.listdir(MODEL_DIR):
            train_and_save_models()

        models = load_models()
        feature_df = pd.read_sql("SELECT * FROM uploaded_feature", engine)
        feature_df = feature_df.drop(columns=["id"])  # 移除id列
        importances = []

        for label, model in models.items():
            feature_importance = [{"feature": feature, "importance": importance} for feature, importance in zip(feature_df.columns, model.feature_importances_)]
            importances.append({"label": label, "importances": feature_importance})

        return {"data": importances}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
```



## 第五章 可视化



#### 5.1 展示样点信息

中国的地理空间位置跨越了亚洲的东部，东临太平洋，西接中亚，北濒蒙古高原，南界东南亚。中国的地形地貌极为复杂多样，从东部的沿海平原到西部的高原和山脉，再到北部的沙漠和草原，形成了丰富的自然景观。

植被特征方面，中国的植被类型随着气候和地形的变化而变化。东部沿海地区多为温带落叶阔叶林和混交林，中部地区则以温带草原和落叶阔叶林为主，西部高原地区则以高山草甸和灌木丛为主。南部地区则有热带雨林和亚热带常绿阔叶林。

山林水域情况在中国也非常丰富。东部的长江、黄河等大河贯穿多个省份，为周边地区提供了灌溉和水资源。西部的青藏高原是亚洲多条大河的发源地，拥有众多的湖泊和冰川。此外，中国的山脉，如喜马拉雅山、天山、秦岭等，不仅是重要的自然屏障，也是生物多样性的宝库。

![alt text](pic/c7206bc5b298a12a59f741388f4b963.png)



### 5.1 在R中绘图

在R中可以使用ggplot包来绘图。
```
ggplot(data = NULL, mapping = aes(), ..., environment = parent.frame())
```
### 5.1 结果
结果
![alt text](pic/result.png)


## 参考文献


Hadley Wickham.(2023)R for Data Science Import, Tidy, Transform, Visualize, and Model Data. O’Reilly, Sebastopol, CA.

Antonanzas-Torres, F. (2014). Geostatistics examples in R: Ordinary kriging, universal kriging and inverse distance weighted.

Ledell, E., Gill, N., Aiello, S., Fu, A., Candel, A., Click, C., Kraljevic, T.,Nykodym, T., Aboyoun, P., & Kurka, M. (2020)interface for the‘H2O’ scalable machine learning platform
Malczewski, J., & Rinner, C. (2016). Multicriteria decision analysis in geographic information science. New York: Springer.

Pebesma, E. J., & Wesseling, C. G. (1998). Gstat: a program for geostatistical modelling, prediction and simulation. Computers & Geosciences, 24(1), 1731.
Sagheb-Talebi, K., Pourhashemi, M., & Sajedi, T. (2014). Forests of Iran: A treasure from the past, a hope forthe future. Springer.

Williams, G. (2011). Data mining with rattle and R. The art of excavating data for knowledge discovery series(1st ed.). New York: Springer-Verlag.

Liu X, Chen LF, Zhou SR (2020) The relationship between biodiversity and infectious disease: Progress, challenge and perspective. Biodiversity Science, 28, 1376–1390.

Felicia Keesing (2010) Impacts of biodiversity on the emergence and transmission of infectious diseases Nature

B.M.库克(1988)植物病害流行学(原书第二版) 科学出版社 

刘向, 刘木, 肖瑶 (2022)叶片病原真菌对植物种共存的影响 : 进展与挑战 兰州大学草种创新与地农业生态系统全国重点实验室 生态学院 , 兰州 730000 
