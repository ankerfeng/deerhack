<%@ page import="java.sql.*" %>
<%@ page import="java.util.*" %>
<%@ page import="java.io.*" %>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%

try {
    /**start config **/
    String sql = request.getParameter("query");
    String driver = "com.mysql.jdbc.Driver";
    String url = "jdbc:mysql://127.0.0.1:3306/search?useUnicode=TRUE&characterEncoding=utf8";
    String username = "root";
    String password = "root";
    /**end config **/
    
    Class.forName(driver).newInstance();
    Connection conn = DriverManager.getConnection(url,username,password);
    
    Statement stmt = conn.createStatement();
    ResultSet rs = stmt.executeQuery(sql);
    ResultSetMetaData rsmd = rs.getMetaData();
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
    response.setStatus(200);
    e.printStackTrace();
}

out.println("<form action=\"\" method=\"\">" +
            "<input type=\"\" value=\"\" name=\"query\" size=20>" +
            "</form>");
%>
