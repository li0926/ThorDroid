<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <%@ page contentType="text/html;charset=UTF-8" language="java" session="true" %>
    <title>检测结果</title>
    <script src="https://cdn.bootcdn.net/ajax/libs/spark-md5/3.0.0/spark-md5.min.js"></script>
    <script src="https://libs.baidu.com/jquery/2.0.0/jquery.min.js"></script>
    <script src="https://libs.baidu.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
    <link rel = "icon"  type="image/x-ico" href = "${pageContext.request.contextPath}/img/logo_little.png">
    <script src="https://cdn.bootcdn.net/ajax/libs/vue/2.4.2/vue.min.js"></script>
    <style>
        .a {
            width: 100%;
            overflow: hidden
        }

        .left,
        .right {
            float: left;
            display: inline-block
        }

        .left {
            width: 59%;
            border-right: 1px solid #8a8a8a
        }

        .right {
            width: 40%
        }


        body {
            padding-top: 70px;
            padding-bottom: 30px;
        }

        body,
        .navbar-fixed-top,
        .navbar-fixed-bottom {
            min-width: 970px;
        }

        /* Don't let the lead text change font-size. */
        .lead {
            font-size: 16px;
        }

        /* Finesse the page header spacing */
        .page-header {
            margin-bottom: 30px;
        }
        .page-header .lead {
            margin-bottom: 10px;
        }


        /* Non-responsive overrides
         *
         * Utilize the following CSS to disable the responsive-ness of the container,
         * grid system, and navbar.
         */

        /* Reset the container */
        .container {
            width: 970px;
            max-width: none !important;
        }

        /* Demonstrate the grids */
        .col-xs-4 {
            padding-top: 15px;
            padding-bottom: 15px;
            background-color: #eee;
            background-color: rgba(86,61,124,.15);
            border: 1px solid #ddd;
            border: 1px solid rgba(86,61,124,.2);
        }

        .container .navbar-header,
        .container .navbar-collapse {
            margin-right: 0;
            margin-left: 0;
        }

        /* Always float the navbar header */
        .navbar-header {
            float: left;
        }

        /* Undo the collapsing navbar */
        .navbar-collapse {
            display: block !important;
            height: auto !important;
            padding-bottom: 0;
            overflow: visible !important;
            visibility: visible !important;
        }

        .navbar-toggle {
            display: none;
        }
        .navbar-collapse {
            border-top: 0;
        }

        .navbar-brand {
            margin-left: -15px;
        }

        /* Always apply the floated nav */
        .navbar-nav {
            float: left;
            margin: 0;
        }
        .navbar-nav > li {
            float: left;
        }
        .navbar-nav > li > a {
            padding: 15px;
        }

        /* Redeclare since we override the float above */
        .navbar-nav.navbar-right {
            float: right;
        }

        /* Undo custom dropdowns */
        .navbar .navbar-nav .open .dropdown-menu {
            position: absolute;
            float: left;
            background-color: #fff;
            border: 1px solid #ccc;
            border: 1px solid rgba(0, 0, 0, .15);
            border-width: 0 1px 1px;
            border-radius: 0 0 4px 4px;
            -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, .175);
            box-shadow: 0 6px 12px rgba(0, 0, 0, .175);
        }
        .navbar-default .navbar-nav .open .dropdown-menu > li > a {
            color: #333;
        }
        .navbar .navbar-nav .open .dropdown-menu > li > a:hover,
        .navbar .navbar-nav .open .dropdown-menu > li > a:focus,
        .navbar .navbar-nav .open .dropdown-menu > .active > a,
        .navbar .navbar-nav .open .dropdown-menu > .active > a:hover,
        .navbar .navbar-nav .open .dropdown-menu > .active > a:focus {
            color: #fff !important;
            background-color: #428bca !important;
        }
        .navbar .navbar-nav .open .dropdown-menu > .disabled > a,
        .navbar .navbar-nav .open .dropdown-menu > .disabled > a:hover,
        .navbar .navbar-nav .open .dropdown-menu > .disabled > a:focus {
            color: #999 !important;
            background-color: transparent !important;
        }

        /* Undo form expansion */
        .navbar-form {
            float: left;
            width: auto;
            padding-top: 0;
            padding-bottom: 0;
            margin-right: 0;
            margin-left: 0;
            border: 0;
            -webkit-box-shadow: none;
            box-shadow: none;
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

        /* Copy-pasted from forms.less since we mixin the .form-inline styles. */
        .navbar-form .form-group {
            display: inline-block;
            margin-bottom: 0;
            vertical-align: middle;
        }

        .navbar-form .form-control {
            display: inline-block;
            width: auto;
            vertical-align: middle;
        }

        .navbar-form .form-control-static {
            display: inline-block;
        }

        .navbar-form .input-group {
            display: inline-table;
            vertical-align: middle;
        }

        .navbar-form .input-group .input-group-addon,
        .navbar-form .input-group .input-group-btn,
        .navbar-form .input-group .form-control {
            width: auto;
        }

        .navbar-form .input-group > .form-control {
            width: 100%;
        }

        .navbar-form .control-label {
            margin-bottom: 0;
            vertical-align: middle;
        }

        .navbar-form .radio,
        .navbar-form .checkbox {
            display: inline-block;
            margin-top: 0;
            margin-bottom: 0;
            vertical-align: middle;
        }

        .navbar-form .radio label,
        .navbar-form .checkbox label {
            padding-left: 0;
        }

        .navbar-form .radio input[type="radio"],
        .navbar-form .checkbox input[type="checkbox"] {
            position: relative;
            margin-left: 0;
        }

        .navbar-form .has-feedback .form-control-feedback {
            top: 0;
        }

        /* Undo inline form compaction on small screens */
        .form-inline .form-group {
            display: inline-block;
            margin-bottom: 0;
            vertical-align: middle;
        }

        .form-inline .form-control {
            display: inline-block;
            width: auto;
            vertical-align: middle;
        }

        .form-inline .form-control-static {
            display: inline-block;
        }

        .form-inline .input-group {
            display: inline-table;
            vertical-align: middle;
        }
        .form-inline .input-group .input-group-addon,
        .form-inline .input-group .input-group-btn,
        .form-inline .input-group .form-control {
            width: auto;
        }

        .form-inline .input-group > .form-control {
            width: 100%;
        }

        .form-inline .control-label {
            margin-bottom: 0;
            vertical-align: middle;
        }

        .form-inline .radio,
        .form-inline .checkbox {
            display: inline-block;
            margin-top: 0;
            margin-bottom: 0;
            vertical-align: middle;
        }
        .form-inline .radio label,
        .form-inline .checkbox label {
            padding-left: 0;
        }

        .form-inline .radio input[type="radio"],
        .form-inline .checkbox input[type="checkbox"] {
            position: relative;
            margin-left: 0;
        }

        .form-inline .has-feedback .form-control-feedback {
            top: 0;
        }
        canvas {
            position: relative;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
        }
        .headline
        {
            padding:5px;
            text-align:center;
            border:solid 1px #c3c3c3;
        }
    </style>
</head>
<body style="background-image: url('img/pic.png');background-size:cover;">
<body style="background-color: #F2F5A9; ">
<script src="getUrlParam.js"></script>
<script type="text/javascript">
    var md5;
    $(function(){
        md5 = UrlParm.parm("md5");
    })
    var obj;
    $(document).ready(function(){
        var statis="processing";
        loadData(md5);
        var interval = setInterval(function(){
            loadData(md5);
        }, 10000);
        function loadData(hash_md5){
            $.ajax({
                url:"${pageContext.request.contextPath}/ajax",
                data:{"filemd5":hash_md5},
                success:function (data){
                    console.log(data)
                    obj = JSON.parse(data);
                    if(obj.status=="processed")
                    {
                        clearInterval(interval);

                        var visible=document.getElementById("result");
                        visible.removeAttribute("hidden");
                        var unvisible=document.getElementById("waiting");
                        unvisible.setAttribute("hidden",true);
                        //调成两列
                        riskfun=obj.Risk_Function;
                        var str_before=" ";
                        var str_after=" ";
                        var riskfunction=new Object();
                        function getStr(string,str){
                            str_before = string.split(str)[0];
                            str_after = string.split(str)[1];
                        }
                        for ( var i = 0; i <riskfun.length; i++){
                            getStr(riskfun[i],"+");
                            riskfunction[str_before]=str_after;
                        }

                        var vc=new Vue({
                            el: '#result',
                            data:{
                                MD5:obj.MD5,
                                NAME:obj.name,
                                SIZE:obj.size,
                                UPLOADDATE:obj.UploadDate,
                                PACKAGENAME:obj.packagename,

                                PERMISSION:obj.permission,
                                RISKFUNCTION:riskfunction,
                                Activities:obj.activities,

                                TelephonyIdentifiersLeakage:obj.TelephonyIdentifiersLeakage,
                                DeviceSettingsHarvesting:obj.DeviceSettingsHarvesting,
                                LocationLookup:obj.LocationLookup,
                                ConnectionInterfacesExfiltration:obj.ConnectionInterfacesExfiltration,
                                TelephonyServicesAbuse:obj.TelephonyServicesAbuse,
                                CodeExecution:obj.CodeExecution,
                                PimDataLeakage:obj.PimDataLeakage,
                                SuspiciousConnectionEstablishment:obj.SuspiciousConnectionEstablishment,
                                AudioVideoEavesdropping:obj.AudioVideoEavesdropping,

                                MinSdkVersion:obj.MinSdkVersion,
                                TargetSdkVersion:obj.TargetSdkVersion,
                                APISCORE:obj.score_api,
                                PERSCORE:obj.score_per
                            }
                        });
                        panel();
                        radar();
                        score2();
                        hidden();
                    }
                }
            })
        }
    })

    function hidden(){
        if(obj.TelephonyIdentifiersLeakage==""){
            var hidden_TIL=document.getElementById("TIL");
            hidden_TIL.setAttribute("hidden",true);
        }
        if(obj.DeviceSettingsHarvesting==""){
            var hidden_DSH=document.getElementById("DSH");
            hidden_DSH.setAttribute("hidden",true);
        }
        if(obj.LocationLookup==""){
            var hidden_LL=document.getElementById("LL");
            hidden_LL.setAttribute("hidden",true);
        }
        if(obj.ConnectionInterfacesExfiltration==""){
            var hidden_CIE=document.getElementById("CIE");
            hidden_CIE.setAttribute("hidden",true);
        }
        if(obj.TelephonyServicesAbuse==""){
            var hidden_TSA=document.getElementById("TSA");
            hidden_TSA.setAttribute("hidden",true);
        }
        if(obj.AudioVideoEavesdropping==""){
            var hidden_AVE=document.getElementById("AVE");
            hidden_AVE.setAttribute("hidden",true);
        }

        if(obj.SuspiciousConnectionEstablishment==""){
            var hidden_SCE=document.getElementById("SCE");
            hidden_SCE.setAttribute("hidden",true);
        }
        if(obj.PimDataLeakage==""){
            var hidden_PDL=document.getElementById("PDL");
            hidden_PDL.setAttribute("hidden",true);
        }
        if(obj.CodeExecution==""){
            var hidden_CE=document.getElementById("CE");
            hidden_CE.setAttribute("hidden",true);
        }

    }


    function score2(){
        var score_a=obj.score_api;
        if (score_a>30){
            document.getElementById("api_score").className = "progress-bar progress-bar-warning";
        }
        if (score_a>60){
            document.getElementById("api_score").className = "progress-bar progress-bar-info";
        }

        if (score_a>80){
            document.getElementById("api_score").className = "progress-bar progress-bar-success";
        }

        var score_p=obj.score_per;
        if (score_p>30){
            document.getElementById("permission_score").className = "progress-bar progress-bar-warning";
        }
        if (score_p>60){
            document.getElementById("permission_score").className = "progress-bar progress-bar-info";
        }
        if (score_p>80){
            document.getElementById("permission_score").className = "progress-bar progress-bar-success";
        }
        score_a=score_a+"%";
        score_p=score_p+"%";

        $("#api_score").width(score_a);
        $("#permission_score").width(score_p);
    }


    function radar() {
        var canvas1 = document.getElementById('myCanvas');
        //var mW = 200;
        //var mH = 200;
        var mData = [['电话短信', obj.a1],
            ['建立连接,发送通知', obj.a3],
            ['收集账户信息', obj.a2],
            ['音频视频', obj.a4],
            ['获取地理位置', obj.a5],
            ['命令行代码执行', obj.a6]];
        /*   var mData = [['A', 12],
              ['B', 45],
              ['C', 45],
              ['D', 34],
              ['E', 88],
              ['F', 87]];*/
        var mCount = mData.length; //边数
        var mCenter = 300 / 2; //中心点
        var mRadius = mCenter - 50; //半径(减去的值用于给绘制的文本留空间)
        var mAngle = Math.PI * 2 / mCount; //角度
        var mCtx = null;
        var mColorPolygon = '#B8B8B8'; //多边形颜色
        var mColorLines = '#B8B8B8'; //顶点连线颜色
        var mColorText = '#000000';

        //初始化
        mCtx = canvas1.getContext('2d');
        drawPolygon(mCtx);
        drawLines(mCtx);
        drawText(mCtx);
        drawRegion(mCtx);
        drawCircle(mCtx);

        // 绘制多边形边
        function drawPolygon(ctx) {
            ctx.save();
            ctx.strokeStyle = mColorPolygon;
            var r = mRadius / mCount; //单位半径
            //画6个圈
            for (var i = 0; i < mCount; i++) {
                ctx.beginPath();
                var currR = r * (i + 1); //当前半径
                //画6条边
                for (var j = 0; j < mCount; j++) {
                    var x = mCenter + currR * Math.cos(mAngle * j);
                    var y = mCenter + currR * Math.sin(mAngle * j);

                    ctx.lineTo(x, y);
                }
                ctx.closePath()
                ctx.stroke();
            }
            ctx.restore();
        }

        //顶点连线
        function drawLines(ctx) {
            ctx.save();

            ctx.beginPath();
            ctx.strokeStyle = mColorLines;

            for (var i = 0; i < mCount; i++) {
                var x = mCenter + mRadius * Math.cos(mAngle * i);
                var y = mCenter + mRadius * Math.sin(mAngle * i);

                ctx.moveTo(mCenter, mCenter);
                ctx.lineTo(x, y);
            }

            ctx.stroke();

            ctx.restore();
        }

        //绘制文本
        function drawText(ctx) {
            ctx.save();

            var fontSize = mCenter / 12;
            ctx.font = fontSize + 'px Microsoft Yahei';
            ctx.fillStyle = mColorText;

            for (var i = 0; i < mCount; i++) {
                var x = mCenter + mRadius * Math.cos(mAngle * i);
                var y = mCenter + mRadius * Math.sin(mAngle * i);

                if (mAngle * i >= 0 && mAngle * i <= Math.PI / 2) {
                    ctx.fillText(mData[i][0], x, y + fontSize);
                } else if (mAngle * i > Math.PI / 2 && mAngle * i <= Math.PI) {
                    ctx.fillText(mData[i][0], x - ctx.measureText(mData[i][0]).width, y + fontSize);
                } else if (mAngle * i > Math.PI && mAngle * i <= Math.PI * 3 / 2) {
                    ctx.fillText(mData[i][0], x - ctx.measureText(mData[i][0]).width, y);
                } else {
                    ctx.fillText(mData[i][0], x, y);
                }

            }

            ctx.restore();
        }

        //绘制数据区域
        function drawRegion(ctx) {
            ctx.save();

            ctx.beginPath();
            for (var i = 0; i < mCount; i++) {
                var x = mCenter + mRadius * Math.cos(mAngle * i) * mData[i][1] / 100;
                var y = mCenter + mRadius * Math.sin(mAngle * i) * mData[i][1] / 100;

                ctx.lineTo(x, y);
            }
            ctx.closePath();
            ctx.fillStyle = 'rgba(255,50,50,0.3)';
            ctx.fill();

            ctx.restore();
        }

        //画点
        function drawCircle(ctx) {
            ctx.save();

            var r = mCenter / 50;
            for (var i = 0; i < mCount; i++) {
                var x = mCenter + mRadius * Math.cos(mAngle * i) * mData[i][1] / 100;
                var y = mCenter + mRadius * Math.sin(mAngle * i) * mData[i][1] / 100;

                ctx.beginPath();
                ctx.arc(x, y, r, 0, Math.PI * 2);
                ctx.fillStyle = 'rgba(255,15,13,0.61)';
                ctx.fill();
            }

            ctx.restore();
        }
    }




    function panel() {
        var canvas = document.getElementById('canvas'),
            ctx = canvas.getContext('2d'),
            cWidth = canvas.width,
            cHeight = canvas.height,
            score = obj.score,
            stage = ['高度危险', '危险', '较安全', '安全', '极好'],
            radius = 150,
            deg0 = Math.PI / 9,
            deg1 = Math.PI * 11 / 45;
        score=score*5+400;
        if(score < 400 || score > 900) {
            alert('信用分数有错（超过范围）');
        } else {
            var dot = new Dot(),
                dotSpeed = 0.03,
                textSpeed = Math.round(dotSpeed * 100 / deg1),
                angle = 0,
                credit = 400;

            (function drawFrame() {
                ctx.save();
                ctx.clearRect(0, 0, cWidth, cHeight);
                ctx.translate(cWidth / 2, cHeight *2 /3);
                ctx.rotate(8 * deg0);

                dot.x = radius * Math.cos(angle);
                dot.y = radius * Math.sin(angle);

                var aim = (score - 400) * deg1 / 100;
                if(angle < aim) {
                    angle += dotSpeed;
                }
                dot.draw(ctx);

                if(credit < score - textSpeed) {
                    credit += textSpeed;
                } else if(credit >= score - textSpeed && credit < score) {
                    credit += 1;
                }
                text(credit);

                ctx.save();
                ctx.beginPath();
                ctx.lineWidth = 3;
                ctx.strokeStyle = 'rgba(1, 2, 100, .5)';
                ctx.arc(0, 0, radius, 0, angle, false);
                ctx.stroke();
                ctx.restore();

                window.requestAnimationFrame(drawFrame);

                ctx.save(); //中间刻度层
                ctx.beginPath();
                ctx.strokeStyle = 'rgba(149, 175, 192, .2)';
                ctx.lineWidth = 10;
                ctx.arc(0, 0, 135, 0, 11 * deg0, false);
                ctx.stroke();
                ctx.restore();

                ctx.save(); // 刻度线
                for(var i = 0; i < 6; i++) {
                    ctx.beginPath();
                    ctx.lineWidth = 2;
                    ctx.strokeStyle = 'rgba(0, 0, 0, .4)';
                    ctx.moveTo(140, 0);
                    ctx.lineTo(130, 0);
                    ctx.stroke();
                    ctx.rotate(deg1);
                }
                ctx.restore();

                ctx.save(); // 细分刻度线
                for(i = 0; i < 25; i++) {
                    if(i % 5 !== 0) {
                        ctx.beginPath();
                        ctx.lineWidth = 2;
                        ctx.strokeStyle = 'rgba(2, 75, 55, .1)';
                        ctx.moveTo(140, 0);
                        ctx.lineTo(133, 0);
                        ctx.stroke();
                    }
                    ctx.rotate(deg1 / 5);
                }
                ctx.restore();

                {
                    ctx.save(); //信用分数
                    ctx.rotate(Math.PI / 2);
                    for(i = 0; i < 6; i++) {
                        ctx.fillStyle = 'rgba(2, 75, 55, .7)';
                        ctx.font = '10px Microsoft yahei';
                        ctx.textAlign = 'center';
                        ctx.fillText(0 + 20 * i, 0, -115);//表盘数字相关
                        ctx.rotate(deg1);
                    }
                    ctx.restore();

                    ctx.save(); //分数段
                    ctx.rotate(Math.PI / 2 + deg0);
                    for(i = 0; i < 5; i++) {
                        ctx.fillStyle = 'rgba(255, 255, 255, .4)';
                        ctx.font = '10px Microsoft yahei';
                        ctx.textAlign = 'center';
                        ctx.fillText(stage[i], 5, -115);
                        ctx.rotate(deg1);
                    }
                    ctx.restore();

                    ctx.save(); //信用阶段及评估时间文字
                    ctx.rotate(10 * deg0);;
                    ctx.font = '28px Microsoft yahei';
                    ctx.textAlign = 'center';
                    if(score < 500) {
                        ctx.fillStyle = '#c0392b'
                        ctx.fillText('危险', 0, 40);
                    } else if(score < 600 && score >= 500) {
                        ctx.fillStyle = '#e74c3c';
                        ctx.fillText('存在风险', 0, 40);
                    } else if(score < 700 && score >= 600) {
                        ctx.fillStyle = '#f39c12';
                        ctx.fillText('中等', 0, 40);
                    } else if(score < 800 && score >= 700) {
                        ctx.fillStyle = '#badc58';
                        ctx.fillText('较安全', 0, 40);
                    } else if(score <= 900 && score >= 800) {
                        ctx.fillStyle = '#6ab04c';
                        ctx.fillText('安全', 0, 40);
                    }
                }
                ctx.fillStyle = '#000000';
                ctx.font = '14px Microsoft yahei';
                var date = new Date();

                ctx.fillText(formatDate(date), 0, 60);

                ctx.fillStyle = '#721111';
                ctx.font = '14px Microsoft yahei';
                ctx.fillText('评分', 0, -60);
                ctx.restore();

                // ctx.save(); //最外层轨道
                ctx.beginPath();
                ctx.strokeStyle = 'rgba(1, 5, 5, .4)';
                ctx.lineWidth = 3;
                ctx.arc(0, 0, radius, 0, 11 * deg0, false);
                ctx.stroke();
                ctx.restore();
            })();
        }

        function Dot() {
            this.x = 0;
            this.y = 0;
            this.draw = function(ctx) {
                ctx.save();
                ctx.beginPath();
                ctx.fillStyle = 'rgba(1, 2, 3, .7)';
                ctx.arc(this.x, this.y, 3, 0, Math.PI * 2, false);
                ctx.fill();
                ctx.restore();
            };
        }

        function text(process) {
            process=(process-400)/5;
            ctx.save();
            ctx.rotate(10 * deg0);
            if(score < 500) {
                ctx.fillStyle = '#c0392b';
            } else if(score < 600 && score >= 500) {
                ctx.fillStyle = '#e74c3c';
            } else if(score < 700 && score >= 600) {
                ctx.fillStyle = '#f39c12';
            } else if(score < 800 && score >= 700) {
                ctx.fillStyle = '#badc58';
            } else if(score <= 900 && score >= 800) {
                ctx.fillStyle = '#6ab04c';
            }

            ctx.font = '80px Microsoft yahei';
            ctx.textAlign = 'center';
            ctx.textBaseLine = 'top';
            ctx.fillText(process, 0, 10);
            ctx.restore();
        }

        function formatDate(date) {
            var myyear = date.getFullYear();
            var mymonth = date.getMonth() + 1;
            var myweekday = date.getDate();

            if (mymonth < 10) {
                mymonth = "0" + mymonth;
            }
            if (myweekday < 10) {
                myweekday = "0" + myweekday;
            }
            return ("检测时间:"+myyear + "-" + mymonth + "-" + myweekday);
        }
    };
</script>
<!-- Fixed navbar -->
<nav class="navbar navbar-default navbar-fixed-top" >
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

<div class="page-header" id="waiting">

    <div  style="background-image: url('img/xingkong.gif')">
        <div class="container" >
            <br>
            <br>
            <h1 style="color: #000000">正在检测中，<br>马上为您呈现结果...</h1>
            <br>
            <br>
        </div>
    </div>
    <div align="center">
        <img src="img/loading3.gif" style="text-align:center;width:25%">
    </div>
</div>
<div class="container">
    <div id="result" hidden>
        <div style="width: auto;height:300px">
            <canvas id="canvas" width=600 height=260 style="margin: 0px;border: 0px;"></canvas>
        </div>


        <h2 style="color: rgb(48, 51, 107);"><strong>详细得分<sup href="#" data-toggle="tooltip" title="我们的算法主要分为两部分，上面的得分是由以下两部分的综合得到的" class="tooltip-test"><small style="color:blue">[?]</small></sup></h2>

        <div style="display: inline">
            <h4 style="color:#1e6fb7;width: 25%;float:left"><strong>&nbsp基于API序列:</strong>{{APISCORE}}</h4>
            <div style="width: 70%;float:right;margin:10px" class="progress">
                <div id="api_score" class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="60"
                     aria-valuemin="0" aria-valuemax="100" style="width: 1%;margin: auto">
                    <span class="sr-only">API序列得分</span>
                </div>
            </div>

        </div>
        <div style="display: inline">
            <h4 style="color:#1e6fb7;width: 25%;float:left"><strong>&nbsp基于 权限&nbsp&nbsp&nbsp:</strong>{{PERSCORE}}</h4>
            <div style="width: 70%;float:right;margin:10px" class="progress">
                <div id="permission_score" class="progress-bar progress-bar-danger" role="progressbar"
                     aria-valuenow="60"
                     aria-valuemin="0" aria-valuemax="100" style="width: 1%;">
                    <span class="sr-only">权限得分</span>
                </div>
            </div>
        </div>
        <br><br><br>



        <div class="a">

            <div class="left">
                <br><br><br><br>

                <h2 style="color:#30336b"><strong>基本信息</strong></h2>
                <div class="tab">
                    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                        <tbody>
                        <tr>
                            <td style="word-break:break-word;" width="20%">
                                <p><strong>文件名称:</strong></p>
                            </td>
                            <td style="word-break:break-word;" width="80%">
                                <p>{{NAME}}</p>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <p><strong>MD5值:</strong></p>
                            </td>
                            <td>
                                <p>{{MD5}}</p>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <p><strong>文件大小:</strong></p>
                            </td>
                            <td>
                                <p>{{SIZE}}MB</p>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <p><strong>上传时间:</strong></p>
                            </td>
                            <td>
                                <p>{{UPLOADDATE}}</p>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <p><strong>包名:</strong></p>
                            </td>
                            <td>
                                <p>{{PACKAGENAME}}</p>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <p><strong>最低SDK版本</strong></p>
                            </td>
                            <td>
                                <p>{{MinSdkVersion}}</p>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="right">
                <div style="float:right;height:340px;">
                    <canvas id="myCanvas" width=320 height="260"></canvas>
                </div>
            </div>
        </div>




        <hr />
        <details>
            <summary style="width:50%;color: #0e83f5" class="headline"><strong>点击展开详细检测报告</strong></summary>
            <hr />
            <h2 style="color: #30336b" class="headline"><strong>使用权限</strong></h2>
            <p>
            <li v-for="value in PERMISSION">
                {{value}}
            </li>
            </p>

            <h2 style="color: #30336b" class="headline"><strong>Activities</strong></h2>
            <p>
            <li v-for="value in Activities">
                {{value}}
            </li>
            </p>


            <h2 style="color: #30336b" class="headline"><strong>危险函数</strong></h2>
            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                <tbody >
                <tr>
                    <th style="width:50%">函数名称</th>
                    <th style="width:50%">危险信息</th>
                </tr>
                <tr v-for="(key,value) in RISKFUNCTION" style="color: red">
                    <td>
                        {{value}}
                    </td>
                    <td>
                        {{key}}
                    </td>
                </tr>
                </tbody>
            </table>

            <div id="TIL">
                <h2 style="color: #30336b" class="headline"><strong>读取电话信息</strong></h2>
                <p>
                <li v-for="value in TelephonyIdentifiersLeakage">
                    {{value}}
                </li>
                </p>
            </div>

            <div id="DSH">
                <h2 style="color: #30336b" class="headline"><strong>收集设备信息</strong></h2>
                <p>
                <li v-for="value in DeviceSettingsHarvesting">
                    {{value}}
                </li>
                </p>
            </div>

            <div id="LL">
                <h2 style="color: #30336b" class="headline"><strong>获取定位</strong></h2>
                <p>
                <li v-for="value in LocationLookup">
                    {{value}}
                </li>
                </p>
            </div>

            <div id="CIE">
                <h2 style="color: #30336b" class="headline"><strong>读取连接信息</strong></h2>
                <p>
                <li v-for="value in ConnectionInterfacesExfiltration">
                    {{value}}
                </li>
                </p>
            </div>

            <div id="TSA">
                <h2 style="color: #30336b" class="headline"><strong>电话服务滥用</strong></h2>
                <p>
                <li v-for="value in TelephonyServicesAbuse">
                    {{value}}
                </li>
                </p>
            </div>

            <div id="AVE">
                <h2 style="color: #30336b" class="headline"><strong>音频视频窃听</strong></h2>
                <p>
                <li v-for="value in AudioVideoEavesdropping">
                    {{value}}
                </li>
                </p>
            </div>

            <div id="SCE">
                <h2 style="color: #30336b" class="headline"><strong>建立可疑连接</strong></h2>
                <p>
                <li v-for="value in SuspiciousConnectionEstablishment">
                    {{value}}
                </li>
                </p>
            </div>

            <div id="PDL">
                <h2 style="color: #30336b" class="headline"><strong>Pim数据泄露</strong></h2>
                <p>
                <li v-for="value in PimDataLeakage">
                    {{value}}
                </li>
                </p>
            </div>

            <div id="CE">
                <h2 style="color: #30336b" class="headline"><strong>代码执行</strong></h2>
                <p>
                <li v-for="value in CodeExecution">
                    {{value}}
                </li>
                </p>
            </div>
        </details>
    </div>
</div>

<!-- Modal -->
<div class="modal fade" id="myModal2" role="dialog">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" style="">&times;</button>
                <h4 class="modal-title"></h4>
            </div>
            <div class="modal-body">
                <p>
                    本平台由全国大学生信息安全作品赛"消毒小分队"开发
                </p>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
            </div>
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
                    <h4 class="modal-title">联系方式</h4>
                </div>
                <div class="modal-body">
                    <p>thordroid@163.com
                    </p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- /container -->
<div class="footer" style="position: relative;">
    <div style="/* width: 1000px; */margin: 0 auto;">
        © 2021 ThorDroid Group.
    </div>
</div>

<script src="http://libs.baidu.com/jquery/1.9.0/jquery.js"></script>
<script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')</script>

</body>
</html>

