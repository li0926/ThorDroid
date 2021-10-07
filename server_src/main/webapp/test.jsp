<html>
<head>
    <title>reCAPTCHA demo: Simple page</title>
    <script src="https://www.recaptcha.net/recaptcha/api.js" async defer></script>
</head>
<body>
<form action="${pageContext.request.contextPath}/check.do" method="POST">
    <div class="g-recaptcha" data-sitekey="6LdJ6cUaAAAAAPm3CBG_Xkv8AibQvKqBDqQjD_Tg"></div>
    <br/>
    <input type="submit" value="Submit">
</form>
</body>
</html>