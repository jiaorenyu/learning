<%--
  Created by IntelliJ IDEA.
  User: renyu
  Date: 2/23/16
  Time: 9:05 AM
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title></title>
</head>
<body>
  <h1>request内置对象</h1>
  <%
      request.setCharacterEncoding("utf-8");
  %>
  用户名:<%=request.getParameter("username") %> <br>
  爱好:<%
      String[] favorites = request.getParameterValues("favorite");
      if (favorites!=null) {
          for (String fa : favorites) {
              out.println(fa + "&nbsp &nbsp");
          }
      }
  %>
</body>
</html>
