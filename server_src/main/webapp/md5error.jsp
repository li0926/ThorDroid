<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <%@ page contentType="text/html;charset=UTF-8" language="java" session="true" %>
    <title>主界面</title>
    <script src="http://libs.baidu.com/jquery/1.9.0/jquery.js"></script>
    <link rel="stylesheet" href="//apps.bdimg.com/libs/bootstrap/3.3.0/css/bootstrap.min.css">
    <script src="https://cdn.bootcdn.net/ajax/libs/spark-md5/3.0.0/spark-md5.min.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script src="https://cdn.bootcss.com/jquery/1.12.4/jquery.min.js"></script>
    <link href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
    <script src='//recaptcha.net/recaptcha/api.js'></script>
    <script src="https://cdn.staticfile.org/vue/2.4.2/vue.min.js"></script>
    <link rel = "icon"  type="image/x-ico" href="${pageContext.request.contextPath}/img/logo_little.png">
    <script>
        function verificationFile(file) {
            var fileTypes = [".apk", ".APK"];
            var filePath = file.value;
            var fileSize = 0;
            var fileMaxSize = 10240;//10M
            var filePath = file.value;
            //当括号里面的值为0、空字符、false 、null 、undefined的时候就相当于false
            if (filePath) {
                var isNext = false;
                var fileEnd = filePath.substring(filePath.length-4);
                for (var i = 0; i < fileTypes.length; i++) {
                    if (fileTypes[i] == fileEnd) {
                        isNext = true;
                        break;
                    }
                }
                if (!isNext) {
                    alert('仅支持 .apk文件');
                    file.value = "";
                    return false;
                }
                fileSize = file.files[0].size;
                var size = fileSize / 1024;
                if (size > fileMaxSize) {
                    alert("文件大小不能大于10M！");
                    file.value = "";
                    return false;
                } else if (size <= 0) {
                    alert("文件大小不能为0M！");
                    file.value = "";
                    return false;
                }
            } else {
                return false;
            }
        }
    </script>
    <script>
        function uploadFile() {
            var form = document.getElementById('upload'),
                formData = new FormData(form);
            $.ajax({
                url:"${pageContext.request.contextPath}/upload.do",
                type:"post",
                data:formData,
                processData:false,
                contentType:false,
                success:function(res){
                    if(res){
                        alert("上传成功！");
                    }
                    console.log(res);
                    $("#pic").val("");
                    $(".showUrl").html(res);
                    $(".showPic").attr("src",res);
                },
                error:function(err){
                    alert("网络连接失败,稍后重试",err);
                }

            })

        }
    </script>
    <script>
        var MMD5;
        function calculate(){
            var fileReader = new FileReader();
            blobSlice = File.prototype.mozSlice || File.prototype.webkitSlice || File.prototype.slice,
                file = document.getElementById("file").files[0],
                chunkSize = 2097152,
                // read in chunks of 2MB
                chunks = Math.ceil(file.size / chunkSize),
                currentChunk = 0,
                spark = new SparkMD5();

            fileReader.onload = function(e) {
                console.log("read chunk nr", currentChunk + 1, "of", chunks);
                spark.appendBinary(e.target.result); // append binary string
                currentChunk++;

                if (currentChunk < chunks) {
                    loadNext();
                }
                else {
                    console.log("finished loading");
                    MMD5=spark.end();
                    open_win(MMD5);
                    console.info("computed hash", spark.end()); // compute hash
                }
            };

            function loadNext() {
                var start = currentChunk * chunkSize,
                    end = start + chunkSize >= file.size ? file.size : start + chunkSize;
                fileReader.readAsBinaryString(blobSlice.call(file, start, end));
            };
            loadNext();
        }
    </script>
    <script>
        function sleep(d){
            for(var t = Date.now();Date.now() - t <= d;);
        }
        function open_win(MD5) {
            // sleep(3000);
            window.open("detail.jsp?md5="+MD5);
        }
    </script>

    <style>
        .upload-btn {
            display: none;
        }
        /*美化自定义按钮*/
        .file-input-trigger {
            padding: 2px 5px;
            border-radius: 5px;
            border: 1px solid #3888C7;
            background-color: #3888C7;
            outline: none;
            color: #fff;
            cursor: pointer;
        }
        .footer{
            font: 13px "微软雅黑";
            text-align: center;
            bottom: 5px;
            width: 100%;
            color: #999;
            padding-top: 30px;
            position: relative;
        }
    </style>
    <script>
        //这一块是有关文件上传按钮的

        $(function() {
            // 点击自定义的span标签触发input标签的点击事件
            $('#fileloadbutton').on('click', function() {
                $('#file').trigger('click')
            })
            // 文件改变时 将文件名称显示到p元素中
            $('#file').on('change', function(event) {
                var fileName = '您已选择文件：' + event.target.files[0].name
                $('#file-name').text(fileName)
                var visible=document.getElementById("submit");
                visible.removeAttribute("hidden");
            })
        })
    </script>

</head>

<body style="background-image: url('${pageContext.request.contextPath}/img/xw.png');
        background-position:center;
        background-attachment:fixed;">

<nav class="navbar navbar-default navbar-fixed-top">
    <div class="container">
        <div class="navbar-header">
            <!-- The mobile navbar-toggle button can be safely removed since you do not need it in a non-responsive implementation -->
            <a href="${pageContext.request.contextPath}/main.jsp">
                <img src="${pageContext.request.contextPath}/img/logo1.png" style="height:55px;"/>
            </a>
        </div>

        <!-- Note that the .navbar-collapse and .collapse classes have been removed from the #navbar -->
        <div id="navbar">

            <ul class="nav navbar-nav">
                <li class="active"><a href="#">主页</a></li>
                <li>  <a data-toggle="modal" data-target="#myModal2">关于我们</a></li>
                <li>  <a data-toggle="modal" data-target="#myModal">联系我们</a></li>
            </ul>
            <form class="navbar-form navbar-right" action="${pageContext.request.contextPath}/search.do" >
                <div class="form-group">
                    <input type="text" class="form-control" placeholder="输入MD5搜索报告" name="searched">
                </div>
                <button type="submit" class="btn btn-default">提交</button>
            </form>
        </div><!--/.nav-collapse -->
    </div>
</nav>

<br>

<div class="container">
    <br><br>
    <div class="row marketing jumbotron">
        <div class="span12">
            <h1>
                抱歉
            </h1>
            <h2>
                没有找到相关信息或提交的APK暂时无法分析
            </h2>
        </div>

    </div>


    <div class="row marketing jumbotron">
        <div id="option2" class="col-lg-6" style="padding: 40px">
            <h2>上传<strong>.apk文件</strong></h2>
            <div class="alert alert-warning">
                <strong>警告！</strong>请注意您的个人隐私保护<br>
            </div>
            <form id="upload" enctype="multipart/form-data" method="post">
                <button type="button" id="fileloadbutton" class="btn btn-lg btn-primary" style="position: relative;overflow: hidden;">选择文件
                    <input type="file"  name="file" id="file" style="position: absolute;left: 0;right: 0;top: 0;bottom: 0;opacity: 0;" onchange="verificationFile(this)" display="none"/>
                </button>
                <h5 id="file-name"></h5>
                <div hidden="hidden" id="submit" >
                    <%--            <div class="g-recaptcha" data-sitekey="6LdJ6cUaAAAAAPm3CBG_Xkv8AibQvKqBDqQjD_Tg"></div>--%>
                    <input type="button"  class="btn btn-lg btn-primary" value="提交" onclick="uploadFile();calculate()"/>
                </div>
            </form>
        </div>
        <div class="col-lg-4">
            <img style="width: 300px" src="${pageContext.request.contextPath}/img/upload.png" data-holder-rendered="true">
        </div>
    </div>

    <div class="row marketing jumbotron">
        <div id="option1" class="col-lg-6" style="padding:40px">
            <h2>搜索已有报告：</h2><br/><br/>

            <form class="form-inline" action="${pageContext.request.contextPath}/search.do">
                <div class="form-group">
                    <label class="sr-only" for="exampleInputAmount"></label>
                    <div class="input-group">
                        <div class="input-group-addon">MD5:</div>
                        <input type="text" class="form-control" id="exampleInputAmount" placeholder="请在此处输入MD5" name="searched">
                    </div>
                </div>
                <button type="submit" class="btn btn-primary">搜索</button>
            </form>
        </div>
        <div class="col-lg-4">
            <img style="width: 300px" src="${pageContext.request.contextPath}/img/search.gif" data-holder-rendered="true">
        </div>
    </div>
</div>

<div class="container">
    <!-- Modal -->
    <div class="modal fade" id="myModal" role="dialog">
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" style="">&times;</button>
                    <h4 class="modal-title">Modal Header</h4>
                </div>
                <div class="modal-body">
                    <p>我们来自
                    </p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Modal -->
<div class="modal fade" id="myModal2" role="dialog">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" style="">&times;</button>
                <h4 class="modal-title">Modal Header</h4>
            </div>
            <div class="modal-body">
                <p>

                    我们将传统的静态检测和机器学习有机结合，通过静态检测技术寻找恶意软件中的危险权限、危险函数以及密码学误用等内容来保障检测报告的可阅读性，通过机器学习算法对函数信息以及权限信息等加以更深层次的提取来保证检测结果的正确性，静态检测的结果为机器学习提供了信息来源，同时机器学习过程中所得的一些信息也帮助静态检测完成了更多的危险函数提取。如此形成的良性循环，帮助整个系统无论在正确性还是可视性上都有着良好的表现，我们将开发的系统命名为ThorDroid，它具有良好的可移植性，不仅可以部署在服务器上，也可以部署在移动设备以及物联网设备上，用户可以根据使用的操作系统的环境来决定安装的ThorDroid的版本(是否需要静态检测)。
                </p>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
            </div>
        </div>
    </div>
</div>
</div>




<div class="footer" style="position: relative;">
    <div style="/* width: 1000px; */margin: 0 auto;">
        © 2021 ThorDroid Group.
    </div>
</div>

<br/>


</body>
</html>