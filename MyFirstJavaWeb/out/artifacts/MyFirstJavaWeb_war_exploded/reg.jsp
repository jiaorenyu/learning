<%--
  Created by IntelliJ IDEA.
  User: renyu
  Date: 2/23/16
  Time: 8:59 AM
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title></title>
</head>
<body>
  <h1>用户注册</h1>
  <hr>
  <form name="reg" action="request.jsp" method="post">
    <table>
      <tr>
        <td>用户名</td>
        <td><input type="text" name="username" /></td>
      </tr>
      <tr>
        <td>爱好</td>
        <td>
          <input type="checkbox" name="favorite" value="read">读书
          <input type="checkbox" name="favorite" value="run">跑步
        </td>
      </tr>
      <tr>
        <td colspan="2"><input type="submit" value="提交"/></td>
      </tr>
    </table>
  </form>

  <a href="request.jsp?username=测试">传参</a>
</body>
</html>
