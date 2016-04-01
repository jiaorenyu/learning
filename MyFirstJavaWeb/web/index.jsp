<%--
  Created by IntelliJ IDEA.
  User: renyu
  Date: 2/18/16
  Time: 3:00 PM
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
  <head>
    <title></title>
  </head>
  <body>
  Hello World!

  <%
    response.sendRedirect("reg.jsp");
  %>
  <%!
    String welcome = "欢迎";
    public String printWelcome(String name) {
      return welcome + name + "!";
    }
    String name = "jiaorenyu";
  %>

  <%
    out.println(printWelcome("jiaorenyu"));
  %>

  你好<%=name%>
  </body>
</html>
