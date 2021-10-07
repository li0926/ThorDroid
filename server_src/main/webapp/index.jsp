<!DOCTYPE html>
<html>
<head>
    <%@ page contentType="text/html;charset=UTF-8" language="java" session="true" %>
    <title>欢迎界面</title>
    <meta charset="UTF-8">
    <script src="https://libs.baidu.com/jquery/1.9.0/jquery.js"></script>
    <link rel = "icon"  type="image/x-ico" href = "${pageContext.request.contextPath}/img/logo_little.png">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
    <link href="https://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
</head>

<style>
    .footer{
        font: 13px "微软雅黑";
        text-align: center;
        bottom: 5px;
        width: 100%;
        color: #999;
        position: relative;
    }
    .hello {
        background-image: url("${pageContext.request.contextPath}/img/xw.png");
        padding: 20%;
        background-position:center;
        color:antiquewhite;
        background-attachment:fixed;
    }
    * {
        box-sizing: border-box;
    }

    body {
        font-family: Arial;
        background: #f1f1f1;
    }

    /* 头部标题 */
    .header {
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

    /* 创建两列 */
    /* Left column */
    .leftcolumn {
        float: left;
        width: 75%;
    }

    /* 右侧栏 */
    .rightcolumn {
        float: left;
        width:auto;
        background-color: #f1f1f1;
        padding-left: 20px;
    }

    /* 图像部分 */
    .fakeimg {
        background-color: #aaa;
        width: 100%;
        padding: 20px;
    }

    /* 文章卡片效果 */
    .card {
        background-color: white;
        padding: 20px;
        margin-top: 20px;
    }

    /* 列后面清除浮动 */
    .row:after {
        content: "";
        display: table;
        clear: both;
    }

    /* 底部 */


    /* 响应式布局 - 屏幕尺寸小于 800px 时，两列布局改为上下布局 */
    @media screen and (max-width: 800px) {
        .leftcolumn, .rightcolumn {
            width: 100%;
            padding: 0;
        }
    }

    /* 响应式布局 -屏幕尺寸小于 400px 时，导航等布局改为上下布局 */
    @media screen and (max-width: 400px) {
        .topnav a {
            float: none;
            width: 100%;
        }
    }

    /* 介绍中毛玻璃效果*/
    main{
        width: 90%;
        height: auto;
        line-height: 2;
        margin: auto;
        border-radius: 5px;
        background: rgba(255, 255, 255, .4);
        box-shadow: 3px 3px 6px 3px rgba(0, 0, 0, .3);
        overflow: hidden;

    }

</style>


<div class="hello" style="margin: 0px;color: #f1f1f1">
    <div class="animate__animated animate__fadeInUp">
        <img src="${pageContext.request.contextPath}/img/logo_bigwhite.png" width="30%">
        <h1>基于机器学习的多维度APK安全检测平台</h1>
        <br>
        <a href="${pageContext.request.contextPath}/main.jsp"
           class="wow fadeInUp smoothScroll btn btn-default section-btn animated"
           data-wow-delay="1s"
           style="visibility: visible; animation-delay: 1s; animation-name: fadeInUp;">
            开始使用</a>
        <a href="#content2"
           class="wow fadeInUp smoothScroll btn btn-default section-btn animated"
           data-wow-delay="1s"
           style="visibility: visible; animation-delay: 1s; animation-name: fadeInUp;">
            了解更多</a>
    </div>
    <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
    <br id="content2"><br><br><br><br><br><br><br>


    <div class="container marketing" style="width:auto">
        <!-- START THE FEATURETTES -->
        <hr class="featurette-divider">

        <div class="row featurette">
            <div class="col-md-7">
                </br></br>
                <h2 class="featurette-heading"><div style="color: #3aca7a">静态检测</div>与
                    <strong style="color: #35C4F0">机器学习</strong>结合

                    <span class="text-muted"></span></h2>
                <p class="lead">机器学习算法得到可靠的检测结果，传统静态检测为用户提供清晰丰富的报告。
                </p>
            </div>
            <div class="col-md-5">
                <img class="featurette-image img-responsive center-block" data-src="holder.js/500x500/auto" alt="500x500" src="img/hello2.png" data-holder-rendered="true">
            </div>
        </div>

        <hr class="featurette-divider">

        <div class="row featurette">
            <div class="col-md-7 col-md-push-5">
                </br></br>
                <h2 class="featurette-heading">鲁棒性良好 <strong style="color: #0e83f5">自适应</strong>式检测</span></h2>
                <p class="lead">系统根据提交APK的新特征，实现了自我调整。此外，ThorDroid可部署范围广，可以在各种规模上正确部署和运行</p>
            </div>
            <div class="col-md-5 col-md-pull-7">
                <img class="featurette-image img-responsive center-block" data-src="holder.js/500x500/auto" alt="500x500" src="img/hello3.png" data-holder-rendered="true">
            </div>
        </div>

        <hr class="featurette-divider">

        <div class="row featurette">
            <div class="col-md-7">
                </br></br>
                <h2 class="featurette-heading">对APK进行<strong >  打分</strong> <span class="text-muted"></span></h2>
                <p class="lead">除了提供详细的分析检测报告外，我们展示了对APK的综合打分以及敏感行为的“雷达图”</p>
            </div>
            <div class="col-md-5">
                <img class="featurette-image img-responsive center-block" data-src="holder.js/500x500/auto" alt="500x500" src="img/hello.png" data-holder-rendered="true">
            </div>
        </div>

        <hr class="featurette-divider">

        <!-- /END THE FEATURETTES -->
    </div>

    <!-- FOOTER -->
    <div class="footer">
        <p class="pull-right">
            <a ytag="20054" href="${pageContext.request.contextPath}/main.jsp" style="float:right;font-weight:bold;" class="evt_link1" title="开始使用">开始使用</a></p>

        <p>© 2021 ThorDroid Group <a href="#">Privacy</a> · <a href="#">Terms</a></p>
    </div>

</div><!-- /.container -->
<script>
    //平滑滑动
    $('a[href*=#],area[href*=#]').click(function() {      //若报错则改为$(document).on('click', 'a[href^="#"]', function () {
        if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
            var $target = $(this.hash);
            $target = $target.length && $target || $('[name=' + this.hash.slice(1) + ']');//获取到点击对应id的元素
            if ($target.length) {
                var targetOffset = $target.offset().top;
                $('html,body').animate({   //滑动效果主要用到jq的animate函数
                    scrollTop: targetOffset},500);
                return false;
            }}});
</script>
</body>
</html>