<!DOCTYPE html>
<html>
<head>
    <%@ page contentType="text/html;charset=UTF-8" language="java" session="true" %>
    <meta charset="utf-8">
    <title>404</title>
    <script src="http://libs.baidu.com/jquery/1.9.0/jquery.js"></script>
    <link rel="stylesheet" href="//apps.bdimg.com/libs/bootstrap/3.3.0/css/bootstrap.min.css">
    <style>
        /* 头部标题 */
        .header{
            padding: 30px;
            text-align: right;
            background: white;
        }

        .header h1 {
            font-size: 50px;
            text-align: center;
        }

        /* 导航条 */
        .topnav {
            overflow: hidden;
            background-color: #333;
        }

        /* 导航条链接 */
        .topnav a {
            float: left;
            display: block;
            color: #f2f2f2;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
        }

        /* 链接颜色修改 */
        .topnav a:hover {
            background-color: #ddd;
            color: black;
        }
        .footer {
            padding: 20px;
            text-align: center;
            background: #ddd;
            margin-top: 20px;
        }
    </style>
</head>
<div class="topnav" id="content">
    <a href="#">链接</a>
    <a href="#">链接</a>
    <a href="#">链接</a>
    <a href="#" style="float:right">链接</a>
</div>

<div class="container">
    <br><br>
    <div class="jumbotron">
        <div class="row">
            <div class="col-xs-6"> <img src="${pageContext.request.contextPath}/img/404.png" style="width:100%"></div>
            <div class="col-xs-6" style="top:5%">
                <br><br><br><br>
                <h1>很抱歉，</h1>
                <h2>你要查找的网页找不到</h2></div>
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