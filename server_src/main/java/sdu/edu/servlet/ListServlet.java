package sdu.edu.servlet;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;
import java.sql.*;

public class ListServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        Connection dbconn = null;
        String dburl = "jdbc:mysql://localhost:3667/thordroid?useUnicode=true&characterEncoding=utf-8&useSSL=false";
        String username = "root";
        String password = "root";
        try{
            Class.forName("com.mysql.jdbc.Driver");
            dbconn = DriverManager.getConnection(dburl, username, password);
            System.out.println("Database connected.");
        }catch(ClassNotFoundException e1){
            System.out.println(e1 + "Driver not find.");
        }catch(SQLException e2){
            System.out.println(e2);
        }


        resp.setContentType("text/html");
        PrintWriter pw = resp.getWriter();

        try{
            String sql = "select * from apk_db";
            PreparedStatement pstmt = dbconn.prepareStatement(sql);
            ResultSet result = pstmt.executeQuery();
            JSONArray jsonArray = new JSONArray();
            while(result.next()){
                JSONObject jsonObject = new JSONObject();
                jsonObject.put("MD5", result.getString("md5"));
                jsonObject.put("Name", result.getString("packagename"));
                jsonObject.put("RiskLevel", result.getInt("risklevel"));
                jsonArray.add(jsonObject);
            }
            JSONObject apkList = new JSONObject();
            apkList.put("apkList", jsonArray);
            pw.append(apkList.toString());
        }catch (SQLException e){
            e.printStackTrace();
        }
        pw.flush();
    }
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // TODO Auto-generated method stub
        doGet(request, response);
    }
}
