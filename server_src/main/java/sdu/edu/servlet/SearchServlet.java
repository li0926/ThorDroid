package sdu.edu.servlet;

import sdu.edu.pojo.APK;
import sdu.edu.service.QueryService;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class SearchServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String uploadmd5 = req.getParameter("searched");
        QueryService queryService = new QueryService();
        APK apk = queryService.query(uploadmd5);
        if(apk==null){
            resp.sendRedirect("md5error.jsp");
        }
        else{
            req.getSession().setAttribute("md5",uploadmd5);
            resp.sendRedirect("searchdetail.jsp");
        }
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        doGet(req,resp);
    }
}
