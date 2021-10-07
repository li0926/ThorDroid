<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <meta charset="utf-8">
    <title>Title</title>
<%--    <link rel="stylesheet" href="//apps.bdimg.com/libs/bootstrap/3.3.0/css/bootstrap.min.css">--%>
    <link href="https://libs.baidu.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet">
<%--    <script src="https://cdn.bootcdn.net/ajax/libs/spark-md5/3.0.0/spark-md5.min.js"></script>--%>
    <script src="https://libs.baidu.com/jquery/1.9.0/jquery.js"></script>
<%--    <script src="//apps.bdimg.com/libs/bootstrap/3.3.0/css/bootstrap.min.js"></script>--%>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script src="https://cdn.staticfile.org/vue/2.4.2/vue.min.js"></script>


    <link rel="icon" type="image/x-ico" href="${pageContext.request.contextPath}/img/logo_little.png"/>
    <style>
        li:hover { background-color:#87CEEB;}
        a:hover { TEXT-DECORATION:none }
    </style>
    <script type="text/javascript">
        $(document).ready(function () {
            loadData();
            function loadData() {
                $.ajax({
                    url: "${pageContext.request.contextPath}/ListAPK",//请求后台
                    //data: {"filemd5": hash_md5},
                    success: function (data) {
                        console.log(data)
                        obj = JSON.parse(data);
                        var vm = new Vue({
                            el: '#vue_det',
                            data: {
                                apks:obj.apkList//用vue处理 后台返回的信息
                            }
                        })
                    }
                })
            }
        })

        //实现搜索
        function myFunction() {
            console.log("123");
            // 声明变量
            var input, filter, ul, li, a, i;
            input = document.getElementById('myInput');
            filter = input.value.toUpperCase();
            ul = document.getElementById("myUL");
            li = ul.getElementsByTagName('li');

            // 循环所有列表，查找匹配项
            for (i = 0; i < li.length; i++) {
                a = li[i].getElementsByTagName("a")[0];
                if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
                    li[i].style.display = "";
                } else {
                    li[i].style.display = "none";
                }
            }
        }



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
                <img src="${pageContext.request.contextPath}/img/logo1.png" style="height:65px">
            </a>
        </div>
        <!-- Note that the .navbar-collapse and .collapse classes have been removed from the #navbar -->
        <div id="navbar">
            <ul class="nav navbar-nav">
                <li class="active"><a href="#">主页</a></li>
                <li><a data-toggle="modal" data-target="#myModal2">关于我们</a></li>
                <li><a data-toggle="modal" data-target="#myModal">联系我们</a></li>
            </ul>

            <form class="navbar-form navbar-right" action="${pageContext.request.contextPath}/search.do">
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
    <br> <br> <br>
    <div class="row marketing jumbotron">

        <div class="col-lg-8">
            <h1><br>
                通过<strong style="color: #35C4F0"> 文件名 </strong>或
                <strong style="color: #00b3b4"> MD5 </strong></h1>

            <h2>搜索我们的<strong>数据库中已有的报告</strong></h2>

        </div>
        <div class="col-lg-4">
            <img style="width: 300px" src="${pageContext.request.contextPath}/img/detect.png" data-holder-rendered="true">
        </div>


        <input type="text" id="myInput" class="form-control" style="width: 50%;float:center;" onkeyup="myFunction()"
               placeholder=" MD5 / Package Name ">
        <br>
        <h3 style="color: #30336b"> &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp MD5&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
            Package Name &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
            Score</h3>

        <hr/>
        <div id="vue_det" style="font-family:Simsun">
            <ul id="myUL">
                <li v-for="apk in apks" style="list-style-type:none ;width: 80%">
                    <div style="display: inline-block;">
                        <a :href="'${pageContext.request.contextPath}/detail.jsp?md5='+apk.MD5">

                            {{apk.MD5}}&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp{{apk.Name}}
                        </a>
                    </div>
                    <div style="display: inline-block;float: right">{{apk.RiskLevel}}</div>
                </li>
            </ul>
        </div>
    </div>


    <br><br>

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

</body>
</html>