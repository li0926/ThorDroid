package sdu.edu.servlet;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.sun.org.apache.bcel.internal.generic.NEW;
import sdu.edu.pojo.APK;
import sdu.edu.service.QueryService;
import sdu.edu.tools.JsonConvert;
import sdu.edu.tools.JsonConvert.*;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.Connection;

public class AjaxServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String md5 = req.getParameter("filemd5");
        QueryService queryService = new QueryService();
        APK apk = queryService.query(md5);
        if(apk==null){
            apk = new APK();
            apk.setStatus("processing");
            resp.getWriter().write(JSON.toJSONString(apk));
        }
        else{
            if(apk.getStatus().equals("error")){
                resp.sendRedirect("md5error.jsp");
            }
            else {
                String JsonData = JSON.toJSONString(apk);
                JSONObject jsonResult= JSONObject.parseObject(JsonData);
                JsonData = JsonConvert.ConvertData(apk.getBehavior_scores(),jsonResult);
                JsonData = JsonData.replace("mD5", "MD5");
                JsonData = JsonData.replace("riskLevel", "score");
                JsonData = JsonData.replace("uploadDate", "UploadDate");
                JsonData = JsonData.replace("risk_Function", "Risk_Function");
                JsonData = JsonData.replace("minSdkVersion","MinSdkVersion");
                JsonData = JsonData.replace("audioVideoEavesdropping","AudioVideoEavesdropping");
                JsonData = JsonData.replace("telephonyIdentifiersLeakage","TelephonyIdentifiersLeakage");
                JsonData = JsonData.replace("deviceSettingsHarvesting","DeviceSettingsHarvesting");
                JsonData = JsonData.replace("locationLookup","LocationLookup");
                JsonData = JsonData.replace("connectionInterfacesExfiltration","ConnectionInterfacesExfiltration");
                JsonData = JsonData.replace("telephonyServicesAbuse","TelephonyServicesAbuse");
                JsonData = JsonData.replace("pimDataLeakage","PimDataLeakage");
                JsonData = JsonData.replace("suspiciousConnectionEstablishment","SuspiciousConnectionEstablishment");
                JsonData = JsonData.replace("suspiciousConnectionEstablishment","SuspiciousConnectionEstablishment");
                JsonData = JsonData.replace("codeExecution","CodeExecution");
                JsonData = JsonData.replace("aPI_score","score_api");
                JsonData = JsonData.replace("permission_score","score_per");
                resp.getWriter().write(JsonData);
            }
        }


    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        doGet(req,resp);
    }
}
